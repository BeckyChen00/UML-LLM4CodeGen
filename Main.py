import yaml

import problemSet
import prompt
import importlib.util

name = "R9_BeWellApp"
rawFilePath = f"problemSet/{name}.py"
resultPath = f"problem/{name}_Result.md"

temperatureList = [0]
model = "gpt-3.5-turbo-0125"
# "gpt-4o-mini"
# "gpt-3.5-turbo-0125"
# "deepseek-ai/DeepSeek-R1"
# "gpt-4o-mini"
# "gpt-3.5-turbo-0125"
# "deepseek-r1" "deepseek-reasoner"
# "deepseek-coder"



spec = importlib.util.spec_from_file_location("data", rawFilePath)
data = importlib.util.module_from_spec(spec)
spec.loader.exec_module(data)



# for version1 in data.version1List[0]:
for description in [data.descriptionList[0]]:
    for temperature in temperatureList:
        for uml in data.umlList:
            # uml = data.uml.replace("{version2}", version2)
            resultBasedSysUML = demo.codeBasedSysUml(description,uml,temperature,model)

            
            with open(resultPath, 'a', encoding='utf-8') as f:
                f.write(f"# Version(sys+uml) Model: {model} Temperature: {temperature}\n")
                f.write(f"## Description:\n{description}\n")
                f.write(f"## UML:\n{uml}\n")
                # f.write(f"## Model:\n{model}\n")
                # f.write(f"## Temperature:\n{temperature}\n")
                f.write(f"## Result:\n{resultBasedSysUML}\n")
                f.write(f"\n{'-'*50}\n")
                
        
        resultBasedSys = demo.codeGenBasedSys(description,temperature,model)
        with open(resultPath, 'a', encoding='utf-8') as f:
            f.write(f"# Version(sys) Model: {model} Temperature: {temperature}\n")
            f.write(f"## Description:\n{description}\n")
            f.write(f"## UML:\n")
            # f.write(f"## Model:\n{model}\n")
            # f.write(f"## Temperature:\n{temperature}\n")
            f.write(f"## Result:\n{resultBasedSys}\n")
            f.write(f"\n{'-'*50}\n")



