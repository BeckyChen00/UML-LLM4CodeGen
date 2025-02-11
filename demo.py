import openai
from openai import OpenAI
import re
import nltk.translate.bleu_score as bleu
import numpy as np
import data

openai = OpenAI(base_url='https://www.DMXapi.com/v1/', api_key='sk-HXJ9ubNKq2k13zlfTzr1xsL35CSzXeaAxkHKE0O6jOgYZ2GO')
def codeGen(description,UML):
    prompt = """根据输入提供的<系统功能需求>以及<UML类图>，生成一个完整的Java代码，请不要修改方法名称。具体要求如下：
1. 输入： 
- 系统功能需求：{description}
- UML类图（PlantUml语法）：{UML}

2. 输出：
- 生成Java代码，包含类、属性、方法以及业务逻辑实现，并且代码需要体现类之间的关系（继承、关联、聚合等）。
- 代码应尽可能减少错误，符合Java编码规范和最佳实践。
- 代码应包含必要的注释。

3. 指导步骤：
- 根据系统文本需求，识别系统中的主要实体和功能模块。
- 使用面向对象方法论，设计类、属性、方法以及类之间的关系。
- 生成Java代码框架，确保代码结构清晰、模块化，并符合高内聚低耦合的原则。
    """

    message = [
        {"role":"system","content":"你是一个专业的软件开发助手，擅长使用面向对象方法论设计和实现Java代码。"},
        {"role":"user","content":prompt.format(description=description,UML=UML)}
        ]
    codeGen = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=message,
        max_tokens=3000,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    ) 
    # print(f"AI output: {codeGen}")
    
    codeGenAnswer, i_tokens, o_tokens, total_tokens = codeGen.choices[0].message.content,codeGen.usage.prompt_tokens,codeGen.usage.completion_tokens,codeGen.usage.total_tokens
    print(f"AI answer: {codeGenAnswer}, \ninput tokens: {i_tokens}, \noutput tokens: {o_tokens}, \ntotal tokens: {total_tokens}")
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
            model="gpt-3.5-turbo-0125",
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

    # 根据需求和设计生成代码
    code = codeGen(data.University_description,data.Uni_UML)
   
    # 评估代码质量
    codeEvalAI(data.University_description,code)


