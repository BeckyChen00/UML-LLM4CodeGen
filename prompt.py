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
task_prompt = "# Task: \nBased on the <System functional requirements> {} provided as input, generate a complete Java code."
input_Prompt = """
## Input:
- System functional requirements: {description}
"""
uml_prompt = "- UML class diagram (in plantuml format): {UML}"
note_1 = """
## Note:
- Generate Java code, including classes, fields, and implementation of methods.
- You are free to add helper methods and fields in the code if needed.
- Code should be as error-free as possible and conform to Java coding standards and best practices.
- The code should include necessary comments."""

note_2 = "- You are encouraged to use the methods defined in <UML class diagram> to implement the code."


def codeBasedSysUml(description,UML,temperature=0,model="gpt-3.5-turbo-0125")->str:
    prompt = task_prompt.format("and <UML class diagram>") + input_Prompt.format(description=description) + uml_prompt.format(UML=UML) + note_1 + note_2
    
    message = [
        {"role":"system","content":"You are a professional software engineer with expertise in programming using UML and Java."},
        {"role":"user","content":prompt}
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
    return prompt, codeGenAnswer


def codeGenBasedSys(description,temperature=0,model="gpt-3.5-turbo-0125")->str:
    prompt = task_prompt.format("") + input_Prompt.format(description=description)+  note_1

    message = [
        {"role":"system","content":"You are a professional software engineer with expertise in programming using UML and Java."},
        {"role":"user","content":prompt}
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
    return prompt, codeGenAnswer



 