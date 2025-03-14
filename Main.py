import os
import yaml

import problemSet
import prompt
import importlib.util

name = "experience5"
rawFilePath = f"problemSet/{name}.py"
resultPath = f"result/{name}_Result.md"

temperatureList = [0.7]
modelList = ["gpt-3.5-turbo-0125"]
# "gpt-3.5-turbo-0125"
# "deepseek-ai/DeepSeek-R1"
# "gpt-4o-mini"
# "gpt-3.5-turbo-0125"
# "deepseek-r1" "deepseek-reasoner"
# "deepseek-coder"



spec = importlib.util.spec_from_file_location("data", rawFilePath)
data = importlib.util.module_from_spec(spec)
spec.loader.exec_module(data)

if not os.path.exists(resultPath):
    # 如果文件不存在，创建并写入内容
    with open(resultPath, "w", encoding="utf-8") as file:
        file.write("")

description = data.descriptionList[0]      
uml = data.umlList[0]

for temperature in temperatureList:
    for model in modelList:
        
        # inputPromptSysUML, resultBasedSysUML = prompt.codeBasedSysUml(description,uml,temperature,model)        
        # with open(resultPath, 'a', encoding='utf-8') as f:
        #     f.write(f"# Version(sys+uml) Model: {model} Temperature: {temperature}\n")
        #     f.write(f"## Prompt:{inputPromptSysUML}\n")
        #     # f.write(f"## Model:\n{model}\n")
        #     # f.write(f"## Temperature:\n{temperature}\n")
        #     f.write(f"## Result:\n{resultBasedSysUML}\n")
        #     f.write(f"\n{'-'*50}\n")
            
    
        inputPromptSys, resultBasedSys = prompt.codeGenBasedSys(description,temperature,model)
        with open(resultPath, 'a', encoding='utf-8') as f:
            f.write(f"# Version(sys) Model: {model} Temperature: {temperature}\n")
            f.write(f"## Prompt: {inputPromptSys}\n")
            # f.write(f"## Model:\n{model}\n")
            # f.write(f"## Temperature:\n{temperature}\n")
            f.write(f"## Result:\n{resultBasedSys}\n")
            f.write(f"\n{'-'*50}\n")



