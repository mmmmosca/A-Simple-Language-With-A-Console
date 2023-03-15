memory=[]
lables=[]

while True:
    code = input(">> ")
    if code.startswith("say"):
        if "remember" in code:
            if "last" in code:
                print(memory[len(memory)-1])
            else:
                index = int(code.replace("remember","").replace("say","").strip())
                print(memory[index])
        elif "recall" in code:
            index = lables.index(code.replace("say","").replace("recall","").strip())
            print(memory[index])
        else:
            print(code.replace("say","").strip())

    if code.startswith("tell"):
        memory.append(input(code.replace("tell","").strip()))

    if code.startswith("store"):
        memory.append(code.replace("store","").strip())

    if code.startswith("label"):
        lables.append(code.replace("label","").strip())

    if code.startswith("forget"):
        if "all" in code:
            memory.clear()
            lables.clear()
        else:
            memory = memory[:-1]
            lables = lables[:-1]