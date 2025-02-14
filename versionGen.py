import yaml

import problemSet
import demo
import problemSet.data1 as data


with open('problem/data1_BasedSyS2.md', 'w', encoding='utf-8') as f:
    f.write("")
with open('problem/data1_BasedSySUML.md', 'w', encoding='utf-8') as f:
    f.write("")


i,j=0,0
tem = 0
model = "gpt-3.5-turbo-0125"
for version1 in data.version1List:
    j+=1

    description = data.description.replace("{version1}",version1)
        # {version23} 内容替换为 version2
    
    i=0
    for version2 in data.version2List:
        i+=1
        uml = data.uml.replace("{version2}", version2)
        resultBasedSysUML = demo.codeBasedSysUml(description,uml,tem,model)

        with open('problem/data1_BasedSyS2.md', 'a', encoding='utf-8') as f:
            f.write(f"# version {j}.{i}\n")
            f.write(f"## Description:\n{description}\n")
            f.write(f"## UML:\n{uml}\n")
            f.write(f"## Model:\ngpt-3.5-turbo-0125\n")
            f.write(f"## Temperature:\n0\n")
            f.write(f"## Result:\n{resultBasedSysUML}\n")
            f.write(f"\n{'-'*50}\n")
    
    resultBasedSys = demo.codeGenBasedSys(description,tem,model)
    with open('problem/data1_BasedSyS2.md', 'a', encoding='utf-8') as f:
            f.write(f"# version {j}.0\n")
            f.write(f"## Description:\n{description}\n")
            f.write(f"## UML:\n")
            f.write(f"## Model:\ngpt-3.5-turbo-0125\n")
            f.write(f"## Temperature:\n0\n")
            f.write(f"## Result:\n{resultBasedSys}\n")
            f.write(f"\n{'-'*50}\n")

