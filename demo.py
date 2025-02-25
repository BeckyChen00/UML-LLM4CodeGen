import openai
from openai import OpenAI
import re
import nltk.translate.bleu_score as bleu
import numpy as np
import problemSet

 
# openai = OpenAI(base_url='https://api.siliconflow.cn/v1',    api_key='sk-apbldvpwfpikpvqryyvtxfpsmgkhtrsvwdzyyqmvwbbroafh')

openai = OpenAI(base_url='https://www.DMXapi.com/v1/', api_key='sk-HXJ9ubNKq2k13zlfTzr1xsL35CSzXeaAxkHKE0O6jOgYZ2GO')
# sk-apbldvpwfpikpvqryyvtxfpsmgkhtrsvwdzyyqmvwbbroafh
# 定义全局变量
base_prompt = """Based on the <System functional requirements> and <UML class diagram> provided as input, generate a complete Java code.
# Input:
- System functional requirements: {description}
"""
uml_prompt = """
- UML class diagram (in plantuml format): {UML}
#Note:
...
- You are encouraged to use the methods defined in the class diagram to implement the code.
"""
note = """
# Note:
- Generate Java code, including classes, fields, and methods.
- You are free to add helper methods and fields in the code if needed.
- Code should be as error-free as possible and conform to Java coding standards and best practices.
- The code should include necessary comments."""

uml_note = """- You are encouraged to use the methods defined in the class diagram to implement the code."""


def codeBasedSysUml(description,UML,temperature=0,model="gpt-3.5-turbo-0125")->str:
    prompt = base_prompt + uml_prompt + note + uml_note
    
    message = [
        {"role":"system","content":"You are a professional software engineer with expertise in programming using UML and Java."},
        {"role":"user","content":prompt.format(description=description,UML=UML)}
        ]
    # print(f"[Sys+UML] AI input: {message}")
    codeGen = openai.chat.completions.create(
        model=model,
        messages=message,
        max_tokens=3000,
        temperature=temperature,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stream=False,
    ) 
    # print(f"AI output: {codeGen}")
    
    codeGenAnswer, i_tokens, o_tokens, total_tokens = codeGen.choices[0].message.content,codeGen.usage.prompt_tokens,codeGen.usage.completion_tokens,codeGen.usage.total_tokens
    print(f"[Sys+UML] AI answer: {codeGenAnswer}, \ninput tokens: {i_tokens}, \noutput tokens: {o_tokens}, \ntotal tokens: {total_tokens}")
    return codeGenAnswer


def codeGenBasedSys(description,temperature=0,model="gpt-3.5-turbo-0125")->str:
    prompt = base_prompt + note

    message = [
        {"role":"system","content":"You are a professional software engineer with expertise in programming using UML and Java."},
        {"role":"user","content":prompt.format(description=description)}
        ]
    # print(f"[Sys] AI input: {message}")
    codeGen = openai.chat.completions.create(
        model=model,
        messages=message,
        max_tokens=3000,
        temperature=temperature,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stream=False,
    ) 
    
    codeGenAnswer, i_tokens, o_tokens, total_tokens = codeGen.choices[0].message.content,codeGen.usage.prompt_tokens,codeGen.usage.completion_tokens,codeGen.usage.total_tokens
    print(f"[Sys] AI answer: {codeGenAnswer}, \ninput tokens: {i_tokens}, \noutput tokens: {o_tokens}, \ntotal tokens: {total_tokens}")
    return codeGenAnswer



 