import yaml


print("hello world")

# output 'prompt.yaml' file :'sys_UML_prompt' . 'prompt'
sys_uml = {'sys_UML_prompt': 'prompt'}  # Define sys_uml with appropriate content

with open("prompt.yaml", "w") as f:
    yaml.dump(sys_uml, f)
