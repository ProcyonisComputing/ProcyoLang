try:
    import os
    import sys
    import time
    from platform import processor, system, version
    import matplotlib.pyplot as plt
    import psutil
    import importlib
except:
    print("\033[91m[!] Error: Initialization of core libraries failed!\033[0m")
    sys.exit(1)

lvar = {}
ladr = {}
lact = {}
lfor = {}
floatNotCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "'", '"', ",", "/", "\\", "<", ">", ";", ":", "[", "]", "{", "}", "-", "_", "+", "=", "(", ")", "!", "@", "#", "$", "%", "^", "&", "*", "~", "`", "|"]
alphabetAll = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
isIncluded = False
arith = ["%", "^", "*", "-", "+", "/"]

def displayVar():
    print(lvar)

def varOps(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        op = param.split(" ")[0]
        varn = param[2:].split(",")
        varn = [x.strip() for x in varn]
        if op == "+":
            res = 0
            for i in range(0, len(varn)):
                res += lvar[varn[i]]
            display(res)
        elif op == "-":
            res = lvar[varn[0]]
            for i in range(1, len(varn)):
                res -= lvar[varn[i]]
            display(res)
        elif op == "*":
            res = 1
            for i in range(0, len(varn)):
                res *= lvar[varn[i]]
            display(res)
        elif op == "/":
            res = lvar[varn[0]]
            for i in range(1, len(varn)):
                res /= lvar[varn[i]]
            display(res)
        elif op == "%":
            res = lvar[varn[0]]
            for i in range(1, len(varn)):
                res %= lvar[varn[i]]
            display(res)
        elif op == "^":
            res = lvar[varn[0]]
            for i in range(1, len(varn)):
                res **= lvar[varn[i]]
            display(res)
        else:
            displayError("Invalid operation passed!")
            return None
            

def inputTake(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        varName, textShow = param.split(" ")
        varName = varName.strip()
        textShow = textShow.strip()
        if textShow in lvar:
            lvar[varName] = input(lvar[textShow]).replace("|s|", " ")
            return None
        elif textShow.isdigit():
            lvar[varName] = input(int(textShow)).replace("|s|", " ")
            return None
        elif textShow.startswith("'") and textShow.endswith("'"):
            textShow = textShow.replace("|s|", ' ')
            lvar[varName] = input(textShow[1:-1]).replace("|s|", " ")
            return None
        elif textShow.startswith('"') and textShow.endswith('"'):
            textShow = textShow.replace("|s|", ' ')
            lvar[varName] = input(textShow[1:-1]).replace("|s|", " ")
            return None

def clrScr():
    os.system("cls" if sys.platform == "win32" else "clear")

def displayDType():
    for i in lvar:
        if type(lvar[i]) == int:
            print(f"{i} -> Integer")
        elif type(lvar[i]) == float:
            print(f"{i} -> Floating Point")
        elif type(lvar[i]) == str:
            print(f"{i} -> String")
        elif type(lvar[i]) == list:
            print(f"{i} -> Array")
        elif type(lvar[i]) == bool:
            print(f"{i} -> Boolean")
        elif lvar[i] == None:
            print(f"{i} -> None")
        elif type(lvar[i]) == complex:
            print(f"{i} -> Complex")
        else:
            print(f"{i} -> Unknown/Other")

def typeCast(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        newdtype, VarName = param.split(" ")
        newdtype = newdtype.strip()
        VarName = VarName.strip()
        if VarName in lvar:
            if newdtype == "int":
                try:
                    lvar[VarName] = int(lvar[VarName])
                except:
                    displayError("Invalid datatype for this type!")
                    return None
                return None
            elif newdtype == "float":
                try:
                    lvar[VarName] = float(lvar[VarName])
                except:
                    displayError("Invalid datatype for this type!")
                    return None
                return None
            elif newdtype == "str":
                try:
                    lvar[VarName] = str(lvar[VarName])
                except:
                    displayError("Invalid datatype for this type!")
                    return None
                return None
            elif newdtype == "list":
                try:
                    lvar[VarName] = list(lvar[VarName])
                except:
                    displayError("Invalid datatype for this type!")
                    return None
                return None
            elif newdtype == "bool":
                try:
                    lvar[VarName] = bool(lvar[VarName])
                except:
                    displayError("Invalid datatype for this type!")
                    return None
                return None
            elif newdtype == "complex":
                try:
                    lvar[VarName] = complex(lvar[VarName])
                except:
                    displayError("Invalid datatype for this type!")
                    return None
                return None
            else:
                displayError("Invalid data type passed!")
                return None

def binView(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        if param in lvar:
            print(bin(lvar[param]))
            return None
        elif param.isdigit():
            print(bin(int(param)))
            return None
        else:
            displayError("Variable does not exist!")
            return None

def typeView(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        if param in lvar:
            if type(lvar[param]) == int:
                print("Integer")
            elif type(lvar[param]) == float:
                print("Floating Point")
            elif type(lvar[param]) == str:
                print("String")
            elif type(lvar[param]) == list:
                print("Array")
            elif type(lvar[param]) == bool:
                print("Boolean")
            elif lvar[param] == None:
                print("None")
            elif type(lvar[param]) == complex:
                print("Complex")
            return None
        elif param.isdigit():
            print(type(int(param)))
            return None
        elif param == "True" or param == "False" or param == "None" or param == "NIL" or param == "NULL":
            print("Boolean")
        else:
            displayError("Variable does not exist!")
            return None

def octView(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        if param in lvar:
            print(oct(lvar[param]))
            return None
        elif param.isdigit():
            print(oct(int(param)))
            return None
        else:
            displayError("Variable does not exist!")
            return None

def hexView(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        if param in lvar:
            print(hex(lvar[param]))
            return None
        elif param.isdigit():
            print(hex(int(param)))
            return None
        else:
            displayError("Variable does not exist!")
            return None

def decView(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        if param in lvar:
            print(int(lvar[param], 0))
            return None
        elif param.isdigit():
            print(int(param, 0))
            return None
        else:
            displayError("Variable does not exist!")
            return None

def displayAdr():
    print(ladr)

def displayAct():
    print(lact)

def display(param):
    param = str(param)
    if param in lact:
        print(lact[param])
    elif param in lvar:
        print(lvar[param])
    elif param in ladr:
        print(ladr[param])
    elif param.startswith('"') and param.endswith('"'):
        try:
            print(param[1:-1].replace('|s|', ' '))
        except:
            print(param[1:-1])
    elif param.startswith("'") and param.endswith("'"):
        try:
            print(param[1:-1].replace('|s|', ' '))
        except:
            print(param[1:-1])
    elif param.isdigit():
        print(param)
    elif param == "True":
        print(True)
    elif param == "False":
        print(False)
    elif param == "None":
        print(None)
    elif param == "NULL":
        print(None)
    elif param == "NILL":
        print(None)
    elif param in alphabetAll:
        displayError("Invalid value passed!")
    else:
        try:
            print(eval(param))
        except:
            print(param)

def displayError(param):
    print(f"\033[91m[!] Syntax Error in line {lineCount}: " + param + "\033[0m")

def displayWarning(param):
    print(f"\033[93m[!] Warning in line {lineCount}: " + param + "\033[0m")

def displaySuccess(param):
    print("\033[92m[+] Success: " + param + "\033[0m")

def ver():
    display("ProcyoLang\nVersion: 1.0.3 Beta 1\nGautham Nair")

def var(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        varName, varValue = param.split("=")
        varName = varName.strip()
        varValue = varValue.strip()
        if varName in lvar:
            displayWarning("Variable already exists! use `varupd" + varName + " = " + varValue + "` to update the value.")
            return None
        else:
            if varValue.isdigit():
                lvar[varName] = int(varValue)
                ladr[varName] = id(lvar[varName])
                return None
            elif varValue in lvar:
                lvar[varName] = lvar[varValue]
                ladr[varName] = id(lvar[varName])
                return None
            else:
                if varValue.startswith('"') and varValue.endswith('"'):
                    lvar[varName] = varValue.replace('"', '')
                    ladr[varName] = id(lvar[varName])
                    return None
                elif varValue.startswith("'") and varValue.endswith("'"):
                    lvar[varName] = varValue.replace("'", '')
                    ladr[varName] = id(lvar[varName])
                    return None
                else:
                    if varValue == "True":
                        lvar[varName] = True
                        ladr[varName] = id(lvar[varName])
                        return None
                    elif varValue == "False":
                        lvar[varName] = False
                        ladr[varName] = id(lvar[varName])
                        return None
                    elif varValue == "None":
                        lvar[varName] = None
                        ladr[varName] = id(lvar[varName])
                        return None
                    elif varValue == "NULL":
                        lvar[varName] = None
                        ladr[varName] = id(lvar[varName])
                        return None
                    elif varValue == "NILL":
                        lvar[varName] = None
                        ladr[varName] = id(lvar[varName])
                        return None
                    elif "," in varValue:
                        val = varValue.strip()
                        val0 = val.split(",")
                        val0 = [x.strip() for x in val0]
                        for i in range(0, len(val0)):
                            if val0[i].isdigit():
                                val0[i] = int(val0[i])
                                return None
                            else:
                                if val0[i].startswith('"') and val0[i].endswith('"'):
                                    val0[i] = val0[i].replace('"', '')
                                elif val0[i].startswith("'") and val0[i].endswith("'"):
                                    val0[i] = val0[i].replace("'", '')
                                else:
                                    if val0[i] == "True":
                                        val0[i] = True
                                    elif val0[i] == "False":
                                        val0[i] = False
                                    elif val0[i] == "None":
                                        val0[i] = None
                                    elif val0[i] == "NULL":
                                        val0[i] = None
                                    elif val0[i] == "NILL":
                                        val0[i] = None
                                    else:
                                        displayError("Invalid value passed!")
                                        return None
                        lvar[varName] = val0
                        ladr[varName] = id(lvar[varName])
                        return None
                    elif "." in varValue and varValue not in floatNotCase:
                        dotCount = 0
                        for i in range(0, len(varValue)):
                            if varValue[i] == ".":
                                dotCount += 1
                            else:
                                continue
                        if dotCount == 1:
                            lvar[varName] = float(varValue)
                            ladr[varName] = id(lvar[varName])
                            return None
                        else:
                            displayError("Invalid value passed!")
                            return None
                    else:
                        displayError("Invalid value passed!")
                        return None

def varUpd(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        varName, varValue = param.split("=")
        varName = varName.strip()
        varValue = varValue.strip()
        if varName not in lvar:
            displayError("Variable does not exist! use `var" + varName + " = " + varValue + "` to create the variable.")
            return None
        else:
            if varValue.isdigit():
                lvar[varName] = int(varValue)
                ladr[varName] = id(lvar[varName])
                return None
            else:
                if varValue.startswith('"') and varValue.endswith('"'):
                    lvar[varName] = varValue.replace('"', '')
                    ladr[varName] = id(lvar[varName])
                    return None
                elif varValue.startswith("'") and varValue.endswith("'"):
                    lvar[varName] = varValue.replace("'", '')
                    ladr[varName] = id(lvar[varName])
                    return None
                else:
                    if varValue == "True":
                        lvar[varName] = True
                        ladr[varName] = id(lvar[varName])
                        return None
                    elif varValue == "False":
                        lvar[varName] = False
                        ladr[varName] = id(lvar[varName])
                        return None
                    elif varValue == "None":
                        lvar[varName] = None
                        ladr[varName] = id(lvar[varName])
                        return None
                    elif varValue == "NULL":
                        lvar[varName] = None
                        ladr[varName] = id(lvar[varName])
                        return None
                    elif varValue == "NILL":
                        lvar[varName] = None
                        ladr[varName] = id(lvar[varName])
                        return None
                    elif "." in varValue and varValue not in floatNotCase:
                        dotCount = 0
                        for i in range(0, len(varValue)):
                            if varValue[i] == ".":
                                dotCount += 1
                            else:
                                continue
                        if dotCount == 1:
                            lvar[varName] = float(varValue)
                            ladr[varName] = id(lvar[varName])
                            return None
                        else:
                            displayError("Invalid value passed!")
                            return None
                    else:
                        displayError("Invalid value passed!")
                        return None

def varArray(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        varDecl, varArrayValue = param.split("=", 1)
        varName = varDecl.strip()
        varArrayValue = varArrayValue.strip()
        varArrayValueArray = [x.strip() for x in varArrayValue.split(",")]
        
        lvar[varName] = varArrayValueArray
        
        for i in range(0, len(varArrayValueArray)):
            if  varArrayValueArray[i].startswith("'") or varArrayValueArray[i].startswith('"') and varArrayValueArray[i].endswith("'") or varArrayValueArray[i].endswith('"'):
                lvar[varName][i] = varArrayValueArray[i].replace('"', '').replace("'", '')

            elif varArrayValueArray[i].isdigit():
                lvar[varName][i] = int(varArrayValueArray[i])
            elif "." in varArrayValueArray[i]:
                floatDotCount = 0
                for j in range(0, len(varArrayValueArray[i])):
                    if varArrayValueArray[i][j] == ".":
                        floatDotCount += 1
                    else:
                        continue
                if floatDotCount == 1:
                    lvar[varName][i] = float(varArrayValueArray[i])
                else:
                    displayError("Invalid value passed!")
            elif varArrayValueArray[i] in lvar:
                lvar[varName][i] = lvar[varArrayValueArray[i]]
        
        ladr[varName] = id(lvar[varName])
        return None
                    
def forLoop(param):
    iteratorVar, forCommand, times, action = param.split(" ", 3)
    iteratorVar = iteratorVar.strip()
    forCommand = forCommand.strip()
    times = times.strip()
    action = action.strip()
    
    if forCommand == "from":
        start, end = times.split("~")
        start = int(start)
        end = int(end)
        for i in range(start, end + 1):
            if action.startswith("display->"):
                display(action[9:])
            elif action.startswith("var->"):
                var(action[5:])
            elif action.startswith("varupd->"):
                varUpd(action[8:])
            else:
                displayError("Invalid command passed for for loop!")
    elif forCommand == "till":
        times = int(times)
        for i in range(0, times + 1):
            if action.startswith("display->"):
                display(action[9:])
            elif action.startswith("var->"):
                var(action[5:])
            elif action.startswith("varupd->"):
                varUpd(action[8:])
            else:
                displayError("Invalid command passed for for loop!")
    elif forCommand == "noDuckTill":
        times = int(times)
        for i in range(1, times + 1):
            if action.startswith("display->"):
                display(action[9:])
            elif action.startswith("var->"):
                var(action[5:])
            elif action.startswith("varupd->"):
                varUpd(action[8:])
            else:
                displayError("Invalid command passed for for loop!")
    else:
        displayError("Invalid command passed for for loop!")


def act(param):
    varName, varActValue = param.split("=")
    varName = varName.strip()
    varActValue = varActValue.strip()
    if varName not in lvar:
        displayError("Variable does not exist! use `var" + varName + " = [value]` to create the variable.")
        return None
    else:
        lact[varName] = varActValue
        return None

def killAct(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        if param in lact:
            del lact[param]
            return None
        else:
            displayError("Variable does not exist or not yet an actor!")
            return None

def kill(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        if param in lvar:
            del lvar[param]
            del ladr[param]
            del lact[param]
            return None
        else:
            displayError("Variable does not exist!")
            return None

def killActAll(param):
    lact.clear()
    return None

def killAll(param):
    lvar.clear()
    ladr.clear()
    lact.clear()
    return None

def plot(param):
    if param == None:
        displayError("No variable name passed!")
        return None
    else:
        if param in lvar:
            if type(lvar[param]) == list:
                plt.plot(lvar[param])
                plt.show()
                return None
            else:
                displayError("Invalid value passed!")
                return None
        else:
            displayError("Variable does not exist!")
            return None

def ProcyoLang(filename):
    try:
        with open(filename, "r") as f:
            global lineCount
            lineCount = 0
            for line in f:
                lineCount += 1
                line = line.strip()
                if line.startswith("#"):
                    continue
                elif line == "display @var":
                    displayVar()
                elif line == "display @adr":
                    displayAdr()
                elif line == "display @act":
                    displayAct()
                elif line == "display @dtype":
                    displayDType()
                elif line.startswith("bin "):
                    binView(line[4:])
                elif line.startswith("oct "):
                    octView(line[4:])
                elif line.startswith("hex "):
                    hexView(line[4:])
                elif line.startswith("dec "):
                    decView(line[4:])
                elif line == "ver":
                    ver()
                elif line.startswith("var "):
                    var(line[4:])
                elif line.startswith("var[] "):
                    varArray(line[6:])
                elif line.startswith("varupd "):
                    varUpd(line[7:])
                elif line.startswith("display "):
                    display(line[8:])
                elif line.startswith("act "):
                    act(line[4:])
                elif line.startswith("type "):
                    typeView(line[5:])
                elif line.startswith("killact "):
                    killAct(line[8:])
                elif line.startswith("kill "):
                    kill(line[5:])
                elif line.startswith("typecast "):
                    typeCast(line[9:])
                elif line.startswith("adr "):
                    display(id(lvar[line[4:]]))
                elif line == None:
                    continue
                elif line.startswith("+ ") or line.startswith("- ") or line.startswith("* ") or line.startswith("/ ") or line.startswith("% ") or line.startswith("** ") or line.startswith("^ "):
                    varOps(line)
                elif line.startswith("system "):
                    os.system(line[7:])
                elif line == "killactall":
                    killActAll()
                elif line.startswith("input "):
                    inputTake(line[6:])
                elif line == "killall":
                    killAll()
                elif line == "clrscr" or line == "cls" or line == "clear" or line == "clrScr" or line == "clearScr" or line == "clrScreen" or line == "clearScreen":
                    clrScr()
                elif line.startswith("plot "):
                    plot(line[5:])
                elif line.startswith("for "):
                    forLoop(line[4:])
    except:
        print("\033[91m[!] Error: No such file found!\033[0m")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("ProcyoLang 1.0.3 Beta 1")
        print("\033[91m[!] Error: No input file specified!\033[0m")
        print("Usage: pl <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    if filename == "-v" or filename == "-ver" or filename == "--v" or filename == "--ver":
        ver()
        sys.exit(0)
    else:
        ProcyoLang(filename)
        sys.exit(0)