import openai
from openai import OpenAI
import re
import nltk.translate.bleu_score as bleu
import numpy as np
import data
description = data.description
uml = data.uml

openai = OpenAI(base_url='https://www.DMXapi.com/v1/', api_key='sk-HXJ9ubNKq2k13zlfTzr1xsL35CSzXeaAxkHKE0O6jOgYZ2GO')
# sk-apbldvpwfpikpvqryyvtxfpsmgkhtrsvwdzyyqmvwbbroafh
# 定义全局变量
base_prompt = """Based on the <System functional requirements> and <UML class diagram> provided as input, generate a complete Java code.
# Input:
- System functional requirements: {description}
"""
uml_prompt = """
- UML class diagram (in plantuml format): {UML}
"""
note = """
# Note:
- Generate Java code, including classes, properties, methods, and business logic implementations.
- Do not modify the method signatures defined in the class diagram. You are free to add any additional methods and fields in the code as needed.
- Code should be as error-free as possible and conform to Java coding standards and best practices.
- The code should include necessary comments."""

def codeBasedSysUml(description,UML,temperature=0,model="gpt-3.5-turbo-0125")->str:
    prompt = base_prompt + uml_prompt + note
    
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
    ) 
    
    codeGenAnswer, i_tokens, o_tokens, total_tokens = codeGen.choices[0].message.content,codeGen.usage.prompt_tokens,codeGen.usage.completion_tokens,codeGen.usage.total_tokens
    print(f"[Sys] AI answer: {codeGenAnswer}, \ninput tokens: {i_tokens}, \noutput tokens: {o_tokens}, \ntotal tokens: {total_tokens}")
    return codeGenAnswer




def codeEvalAI(description,code):
    prompt = """判断以下代码是否能无错误地覆盖<系统功能需求>，包括语法正确性、逻辑正确性、可维护性与可读性。并请你给这段代码打个分数：1-10分，分数越高代码质量越高。
    # 系统功能需求：
    {description}
    # 代码：
    {code}

    # 输出：
    xx/10分
    """
    codeClean = code.partition("```java")[2].partition("```")[0]
    message = [
        {"role":"system","content":"你是一个专业的Java代码评估专家。"},
        {"role":"user","content":prompt.format(description=description, code=codeClean)}]
    codeEval = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=message,
            max_tokens=3000,
            temperature=0,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

    codeEvalAnswer, i_tokens, o_tokens, total_tokens = codeEval.choices[0].message.content,codeEval.usage.prompt_tokens,codeEval.usage.completion_tokens,codeEval.usage.total_tokens
    print(f"AI answer: {codeEvalAnswer}, input tokens: {i_tokens}, output tokens: {o_tokens}, total tokens: {total_tokens}")



def codeEvalBLEU(code_candidate,code_reference):
    """BLEU适用于评估机器翻译的代码质量"""
    # 分行代码? 分类？
    code_candidate = code_candidate.replace("\n","")
    code_reference = code_reference.replace("\n","")

    # 候选文本和参考文本
    candidate =""" """
    reference =""" """
    # 将文本分割成单词列表
    reference_list = [reference.split()]
    candidate_list = candidate.split()

    # 计算BLEU分数
    score = bleu.sentence_bleu(reference_list, candidate_list)





if __name__ == '__main__':

    # 根据需求生成设计
    # UMLGen = UNLGen(description)
    temperature = 0
    model_list = ["gpt-3.5-turbo-0125","gpt-4o-mini", "gpt"]

    # 根据需求和设计生成代码
    with open('codeGen.txt', 'w', encoding='utf-8') as f:
        f.write("")
    with open('codeBasedSys.txt', 'w', encoding='utf-8') as f:
        f.write("")

    # for model in model_list:
    for i in range(2):
        codeGen = codeBasedSysUml(description,uml,temperature)
        with open('codeGen.txt', 'a', encoding='utf-8') as f:
            f.write(f"Run {i+1} - codeGen:\n")
            f.write(codeGen)
            f.write(f"\n{'-'*50}\n")

        codeBasedSys = codeGenBasedSys(description,temperature)
        with open('codeBasedSys.txt', 'a', encoding='utf-8') as f:
            f.write(f"Run {i+1} - codeBasedSys:\n")
            f.write(codeBasedSys)
            f.write(f"\n{'-'*50}\n")


   
    # 评估代码质量
    # codeEvalAI(data.University_description,code)


