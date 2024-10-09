<<<<<<< Updated upstream
import os
import sys
import time
from platform import processor, system, version
import matplotlib.pyplot as plt
import psutil
import importlib
=======
try:
    import os
    import sys
    import matplotlib.pyplot as plt
except:
    print("\033[91m[!] Error: Initialization of core libraries failed!\033[0m")
    sys.exit(1)
>>>>>>> Stashed changes

lvar = {}
ladr = {}
lact = {}
<<<<<<< Updated upstream
lfor = []
isIncluded = False
=======
lfor = {}
floatNotCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "'", '"', ",", "/", "\\", "<", ">", ";", ":", "[", "]", "{", "}", "-", "_", "+", "=", "(", ")", "!", "@", "#", "$", "%", "^", "&", "*", "~", "`", "|"]
alphabetAll = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "'", '"', ",", "/", "\\", "<", ">", ";", ":", "[", "]", "{", "}", "-", "_", "+", "=", "(", ")", "!", "@", "#", "$", "%", "^", "&", "*", "~", "`", "|", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
arith = ["%", "^", "*", "-", "+", "/"]
>>>>>>> Stashed changes

def for_run(param):
    if param.startswith("print->"):
        if param[7:].startswith('"') and param[-1] == '"':
            print(param[8:-1].replace("|s|", " "))
        elif param[7:].isdigit():
            print(param[7:])
        elif param[7:] in lvar:
            print(lvar[param[7:]])
        elif param[7:] in ladr:
                print(ladr[param[7:]])
        else:
            print("\033[91mError : Invalid Variable\033[1;37m")
    elif param.startswith("var->"):
        varn, value = param[5:].split("=")
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
            pass
        elif value in '.':
            value = float(value)
        else:
            value = int(value)
        lvar[varn] = value
        ladr[varn] = id(lvar[varn])
    elif param.startswith("var[]->"):
        varn, val = param[6:].split("=")
        varn = varn.strip()
        val = val.strip()
        val0 = val.split(",")
        val0 = [x.strip() for x in val0]
        for i in range(0, len(val0)):
            if val0[i].isdigit():
                val0[i] = int(val0[i])
            else:
<<<<<<< Updated upstream
                if val0[i].startswith('"'):
                    if val0[i].endswith('"'):
                        val0[i] = val0[i].replace('"', '')
=======
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
    display("ProcyoLang\nVersion: 2.0.1 Beta 2\nGautham Nair")

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
>>>>>>> Stashed changes
                    else:
                        pass
                else:
                    pass
        if val == "" or val == " ":
            print("\033[91mError : Invalid Syntax\033[1;37m")
        else:
            lvar[varn] = val0
            ladr[varn] = id(lvar[varn])
    elif param.startswith("act->"):
        actn, value = param[5:].split("=")
        if actn in lvar:
            lvar[actn] = value
        else:
            print("\033[91mError : Invalid Variable\033[1;37m")
    elif param.startswith("killact->"):
        del lact[param[9:]]
    elif param.startswith("kill->"):
        del lvar[param[5:]]
        del ladr[param[5:]]
    else:
        print("\033[91mError : Invalid Command\033[1;37m")



def run_file(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.rstrip()
                if line.startswith("#"):
                    pass
                elif line == "":
                    pass
                elif line == " ":
                    pass
                elif line.startswith("print "):
                    if line[6:].isdigit():
                        print(line[6:])
                    elif line[6:] in lvar:
                        print(lvar[line[6:]])
                    elif line[6:].startswith('"'):
                        if line.endswith('"'):
                            print(line[7:-1])
                        else:
                            print(line)
                            print("\033[91mError : Invalid Syntax\033[1;37m")
                    else:
                        print("\033[91mNo such variable found to print\033[1;37m")
                elif line.startswith("echo "):
                    print(line[5:])
                elif line.startswith("use "):
                    libName = line[4:]
                    libName = libName.strip(" ")
                    try:
                        lib = importlib.import_module(libName)
                        isIncluded = True
                    except:
                        print("\033[91mError : Library not found\033[1;37m")
                elif line.startswith(libName + "."):
                    if isIncluded:
                        func_args = []
                        if "," in line:
                            func_name, func_args_non_seperated = line[len(libName) + 1:].split(" ")
                            func_args = func_args_non_seperated.split(",")
                            for i in range(0, len(func_args)):
                                if func_args[i].isdigit():
                                    func_args[i] = int(func_args[i])
                                else:
                                    pass
                        else:
                            try:
                                func_name, func_args = line[len(libName) + 1:].split(" ")
                                print(func_args)
                                if func_args.isdigit():
                                    func_args = int(func_args)
                            except:
                                func_name = line[len(libName) + 1:]
                        if func_args != []:
                            func = getattr(lib, func_name)
                            if callable(func):
                                func(func_args)
                            else:
                                print("\033[91mError : No such routine found in module\033[1;37m")
                        else:
                            func = getattr(lib, func_name)
                            if callable(func):
                                func()
                            else:
                                print("\033[91mError : No such routine found in module\033[1;37m")
                    else:
                        print("\033[91mError : Library not included\033[1;37m")
                elif line.startswith("which "):
                    if line[6:] == "cpu" or line[6:] == "CPU":
                        print(platform.processor())
                    elif line[6:] == "os" or line[6:] == "OS":
                        print(platform.system() + " " + platform.version())
                    else:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                elif line.startswith("timeout("):
                    if line.endswith(")"):
                        try:
                            delay(int(line[8:-1]))
                        except:
                            print("\033[91mError : Invalid Syntax\033[1;37m")
                    else:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                elif line.startswith("var "):
                    if line[4] == " ":
                        print("\033[91mError : Invalid Syntax")
                    elif line[4] in ["-", "+", "/", "*", "!", "@", "#", "$", "%", "^", "&", "`", "~", ".", ",", "\\", "{", "}", "[", "]", ";", ":", "'", '"', "|", "<", ">", "?", "(", ")"]:
                        print("\033[91mError : Invalid start of variable name\033[1;37m")
                    else:
                        varn, val = line[4:].split("=")
                        varn = varn.strip(" ")
                        val = val.strip(" ")
                        if varn in lvar:
                            print("\033[93mVariable already exists, use varupd to update variable content\033[1;37m")
                        else:
                            if val == " ":
                                print("\033[91mError : Invalid Syntax\033[1;37m")
                            elif val.startswith('"'):
                                if val.endswith('"'):
                                    lvar[varn] = val[1:-1]
                                    ladr[varn] = id(lvar[varn])
                                else:
                                    print("\033[91mError : Invalid Syntax\033[1;37m")
                            elif val.isalpha() == False:
                                if "." in val:
                                    j = 0
                                    for i in val:
                                        if i == ".":
                                            j += 1
                                        else:
                                            pass
                                    if j == 1:
                                        lvar[varn] = float(val)
                                        ladr[varn] = id(lvar[varn])
                                    else:
                                        print("\033[91mError : Invalid Syntax\033[1;37m")
                                else:
                                    lvar[varn] = int(val)
                                    ladr[varn] = id(lvar[varn])
                            elif val.startswith("'"):
                                if val.endswith("'"):
                                    lvar[varn] = val[1:-1]
                                    ladr[varn] = id(lvar[varn])
                                else:
                                    print("\033[91mError : Invalid Syntax\033[1;37m")
                            else:
                                print("\033[93mUnknown datatype\033[93m")
                elif line.startswith("varupd "):
                    varn, val = line[7:].split("=")
                    varn = varn.strip(" ")
                    val = val.strip(" ")
                    del lvar[varn]
                    del ladr[varn]
                    if val == " ":
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                    elif val.startswith('"'):
                        if val.endswith('"'):
                            lvar[varn] = val[1:-1]
                            ladr[varn] = id(lvar[varn])
                        else:
                            print("\033[91mError : Invalid Syntax\033[1;37m")
                    elif val.isalpha() == False:
                        if "." in val:
                            j = 0
                            for i in val:
                                if i == ".":
                                    j += 1
                                else:
                                    pass
                            if j == 1:
                                lvar[varn] = float(val)
                                ladr[varn] = id(lvar[varn])
                            else:
                                print("\033[91mError : Invalid Syntax\033[1;37m")
                        else:
                            lvar[varn] = int(val)
                            ladr[varn] = id(lvar[varn])
                    elif val.startswith("'"):
                        if val.endswith("'"):
                            lvar[varn] = val[1:-1]
                            ladr[varn] = id(lvar[varn])
                        else:
                            print("\033[91mError : Invalid Syntax\033[1;37m")
                    else:
                        print("\033[93mUnknown datatype\033[93m")
                elif line.startswith("if "):
                    condition, action, terminate, els, action2  = line[3:].split(" ")
                    if terminate != ";":
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                        pass
                    else:
                        try:
                            var, var1 = condition.split("==")
                            if var in lvar and var1 in lvar:
                                if lvar[var] == lvar[var1]:
                                    if action.startswith("print"):
                                        action, value = action.split("->")
                                        if value == var:
                                            print(lvar[var])
                                        elif value == var1:
                                            print(lvar[var1])
                                        elif value.isdigit():
                                            print(value)
                                        elif value in lvar:
                                            print(lvar[value])
                                        elif value.startswith('"') and value.endswith('"'):
                                            value = value.replace("|s|", " ")
                                            print(value[1:-1])
                                        else:
                                            print("\033[91mError : Invalid Syntax\033[1;37m")
                                    else:
                                        print("\033[91mError : Invalid Syntax\033[1;37m")
                                else:
                                    if action2.startswith("print"):
                                        action2, value = action2.split("->")
                                        if value == var:
                                            print(lvar[var])
                                        elif value == var1:
                                            print(lvar[var1])
                                        elif value.isdigit():
                                            print(value)
                                        elif value in lvar:
                                            print(lvar[value])
                                        elif value.startswith('"') and value.endswith('"'):
                                            value = value.replace("|s|", " ")
                                            print(value[1:-1])
                                        else:
                                            print("\033[91mError : Invalid Syntax\033[1;37m")
                            else:
                                print("\033[91mVariable not found\033[1;37m")
                        except:
                            var, var1 = condition.split("!=")
                            if var in lvar and var1 in lvar:
                                if lvar[var] != lvar[var1]:
                                    if action.startswith("print"):
                                        action, value = action.split("->")
                                        if value == var:
                                            print(lvar[var])
                                        elif value == var1:
                                            print(lvar[var1])
                                        elif value.isdigit():
                                            print(value)
                                        elif value in lvar:
                                            print(lvar[value])
                                        elif value.startswith('"') and value.endswith('"'):
                                            value = value.replace("|s|", " ")
                                            print(value[1:-1])
                                        else:
                                            print("\033[91mError : Invalid Syntax\033[1;37m")
                                    else:
                                        print("\033[91mError : Invalid Syntax\033[1;37m")
                                else:
                                    if action2.startswith("print"):
                                        action2, value = action2.split("->")
                                        if value == var:
                                            print(lvar[var])
                                        elif value == var1:
                                            print(lvar[var1])
                                        elif value.isdigit():
                                            print(value)
                                        elif value in lvar:
                                            print(lvar[value])
                                        elif value.startswith('"') and value.endswith('"'):
                                            value = value.replace("|s|", " ")
                                            print(value[1:-1])
                                        else:
                                            print("\033[91mError : Invalid Syntax\033[1;37m")
                            else:
                                print("\033[91mVariable not found\033[1;37m")                            
                elif line.startswith("var[] "):
                    varn, val = line[6:].split("=")
                    varn = varn.strip()
                    val = val.strip()
                    val0 = val.split(",")
                    val0 = [x.strip() for x in val0]
                    for i in range(0, len(val0)):
                        if val0[i].isdigit():
                            val0[i] = int(val0[i])
                        else:
                            if val0[i].startswith('"'):
                                if val0[i].endswith('"'):
                                    val0[i] = val0[i].replace('"', '')
                                else:
                                    pass
                            else:
                                pass
                    if val == "" or val == " ":
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                    else:
                        lvar[varn] = val0
                        ladr[varn] = id(lvar[varn])
                elif line.startswith("kill "):
                    varn = line[5:]
                    varn = varn.strip(" ")
                    try:
                        del ladr[varn]
                        del lvar[varn]
                    except:
                        print("\033[91mVariable not found\033[1;37m")
                elif line.startswith("act ") or line.startswith("mask "):
                    if line.startswith("act "):
                        varn, val = line[4:].split("=")
                        varn = varn.strip(" ")
                        val = val.strip(" ")
                        if varn in lvar:
                            lact[varn] = val
                        else:
                            print("\033[91mVariable not found to act or mask\033[1;37m")
                    else:
                        varn, val = line[5:].split("=")
                        varn = varn.strip(" ")
                        val = val.strip(" ")
                        if varn in lvar:
                            lact[varn] = val
                        else:
                            print("\033[91mVariable not found to act or mask\033[1;37m")
                elif line == "clr" or line == "cls" or line == "clr()" or line == "cls()" or line == "clrscr()":
                    if sys.platform == "win32":
                        os.system('cls')
                    else:
                        os.system('clear')
                elif line.startswith("sht "):
                    print(f"Hello {line[4:]}, greetings from ProcyoLang..!")
                elif line.startswith("plot "):
                    try:
                        _, x, y = line.split()
                        x, y = int(x), int(y)
                        plt.plot([x], [y], marker='o')
                        plt.title("ProcyoLang Plot")
                        plt.xlabel("X-Axis")
                        plt.ylabel("Y-Axis")
                        plt.grid(True)
                        plt.show()
                    except ValueError:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                    except exception as e:
                        print("\033[91mError : ", e, "\033[1;37m")
                elif line.startswith("plotline "):
                    try:
                        _, x1, y1, x2, y2 = line.split()
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        plt.plot([x1, x2], [y1, y2], marker='o')
                        plt.title('ProcyoLang Line Plot')
                        plt.xlabel('X')
                        plt.ylabel('Y')
                        plt.grid(True)
                        plt.show()
                    except ValueError:
                        print("\033[91mError : Invalid Syntax. Please use 'plotline x1 y1 x2 y2' format.\033[1;37m")
                    except exception as e:
                        print(f"\033[91mAn error occurred: {e}\033[1;37m")
                elif line.startswith("system "):
                    os.system(line[7:])
                elif line == "system":
                    print("\033[91mNo value supplied\033[1;37m")
                elif line == "echo":
                    print("\033[91mError : Statement expected after echo\033[1;37m")
                elif line.startswith("input "):
                    try:
                        var, inst = line[6:].split(" ")
                        inst = inst.replace("|s|", " ")
                        lvar[var] = input(inst)
                    except:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                elif line == "duck" or line == "DUCK" or line == "Duck":
                    print(0)
                elif line == "duckduck" or line == "DUCKDUCK" or line == "DuckDuck":
                    print("0^2")
                elif line == "input":
                    print("\033[91mError : Statement expected after input\033[1;37m")
                elif line.startswith("type("):
                    if line.endswith(")"):
                        if line[5:-1] in lvar:
                            dtype = str(type(lvar[line[5:-1]]))
                            if "int" in dtype:
                                print("Integer")
                            elif "float" in dtype:
                                print("Float")
                            elif "str" in dtype:
                                print("String")
                            elif "bool" in dtype:
                                print("Boolean")
                            elif "complex" in dtype:
                                print("Complex")
                            elif "list" in dtype:
                                print("Array")
                            else:
                                print("Other")
                        else:
                            print("\033[91mNo such variable found\033[1;37m")
                    else:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                elif line.startswith("int("):
                    if line.endswith(")"):
                        if line[4:-1].isdigit():
                            print(int(line[4:-1]))
                        else:
                            if line[4:-1] in lvar:
                                if lvar[line[4:-1]].isdigit():
                                    lvar[line[4:-1]] = int(lvar[line[4:-1]])
                                    print(lvar[line[4:-1]])
                    else:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                elif line.startswith("str("):
                    if line.endswith(")"):
                        if line[4:-1].startswith('"'):
                            if line[4:-1].endswith('"'):
                                print(str(line[5:-2]))
                            else:
                                print("\033[91mError : Invalid Syntax\033[1;37m")
                        else:
                            if line[4:-1] in lvar:
                                lvar[line[4:-1]] = str(lvar[line[4:-1]])
                                print(lvar[line[4:-1]])
                            else:
                                print("\033[91mNo such variable found to typecast\033[1;37m")
                    else:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                elif line.startswith("act "):
                    varn, val = line[4:].split("=")
                    varn = varn.strip(" ")
                    val = val.strip(" ")
                    if varn in lvar:
                        lact[varn] = val
                    else:
                        print("\033[91mVariable not found to act or mask\033[1;37m")
                elif line.startswith("isDigit("):
                    if line.endswith(")"):
                        if line[8:-1].isdigit():
                            print(True)
                        else:
                            if line[8:-1] in lvar:
                                if lvar[line[8:-1]].isdigit():
                                    print(True)
                                else:
                                    print(False)
                    else:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                elif line.startswith("isChar("):
                    if line.endswith(")"):
                        if len(line[7:-1]) == 1:
                            if line[7:-1] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', "'", '"', '\\', '|', ',', '.', '/', '?', '<', '>']:
                                print(True)
                            else:
                                if line[7:-1] in lvar:
                                    if lvar[line[7:-1]] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', "'", '"', '\\', '|', ',', '.', '/', '?', '<', '>']:
                                        print(True)
                                    else:
                                        print(False)
                        else:
                            if line[7:-1] in ['\\0', '\\n', '\\t']:
                                print(True)
                            else:
                                if lvar[line[7:-1]] in ['\\0', '\\n', '\\t']:
                                    print(True)
                                else:
                                    print(False)
                    else:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                elif line.startswith("isBool("):
                    if line.endswith(")"):
                        if line[7:-1] in ['True', 'False', '1', '0']:
                            print(True)
                        else:
                            if lvar[line[7:-1]] in ['True', 'False', '1', '0']:
                                print(True)
                            else:
                                print(False)
                    else:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                elif line.startswith("isFloat("):
                    try:
                        if line.endswith(")"):
                            if line[8:-1].replace(".", "").isdigit():
                                print(True)
                            else:
                                if lvar[line[8:-1]].replace(".", "").isdigit():
                                    print(True)
                                else:
                                    print(False)
                        else:
                            print("\033[91mError : Invalid Syntax\033[1;37m")
                    except:
                        print(False)
                elif line.startswith("adr "):
                    try:
                        print(id(lvar[line[4:]]))
                    except:
                        print("\033[91mVariable not found\033[1;37m")
                elif line.startswith("for "):
                    try:
                        iterating_var, in_command, command, action = line[4:].split(" ")
                        if in_command == "from":
                            start, end = command.split("~")
                            start = int(start)
                            end = int(end)
                            for i in range(start, end + 1):
                                for_run(action)
                        elif in_command == "till":
                            command = int(command)
                            for i in range(0, command + 1):
                                for_run(action)
                        elif in_command == "noDuckTill":
                            command = int(command)
                            for i in range(1, command + 1):
                                for_run(action)                                                 
                        else:
                            print("\033[91mError : Invalid Syntax\033[1;37m")
                    except:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                elif line.startswith("adrcall "):
                    val = line[8:]
                    for k, v in ladr.items():
                        if str(v) == val:
                            print(f"Variable: {k}, Value: {var[k]}")
                elif line.startswith("isAlpha("):
                    if line.endswith(")"):
                        if line[8:-1].isalpha():
                            print(True)
                        else:
                            if lvar[line[8:-1]].isalpha():
                                print(True)
                            else:
                                print(False)
                    else:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                elif line.startswith("killact ") or line.startswith("unmask "):
                    if line.startswith("killact "):
                        varn = line[8:]
                        varn = varn.strip(" ")
                        if varn in lact:
                            del lact[varn]
                        else:
                            print("\033[91mVariable not found to killact or unmask\033[1;37m")
                    else:
                        varn = line[7:]
                        varn = varn.strip(" ")
                        if varn in lact:
                            del lact[varn]
                        else:
                            print("\033[91mVariable not found to killact or unmask\033[1;37m")
                elif line.startswith("varops "):
                    op = line[7:].split(" ")[0]
                    varn = line[7:].split(" ")[1:]
                    for i in range(0, len(varn)):
                        if varn[i] in lvar:
                            if i == 0:
                                if op == "+":
                                    res = lvar[varn[i]]
                                elif op == "-":
                                    res = lvar[varn[i]]
                                elif op == "*":
                                    res = lvar[varn[i]]
                                elif op == "/":
                                    res = lvar[varn[i]]
                                else:
                                    print("\033[91mError : Invalid operator\033[1;37m")
                            else:
                                if op == "+":
                                    res += lvar[varn[i]]
                                elif op == "-":
                                    res -= lvar[varn[i]]
                                elif op == "*":
                                    res *= lvar[varn[i]]
                                elif op == "/":
                                    res /= lvar[varn[i]]
                                else:
                                    print("\033[91mError : Invalid operator\033[1;37m")
                        else:
                            print("\033[91mVariable not found\033[1;37m")
                    print(res)
                elif line.startswith("isAlnum("):
                    if line.endswith(")"):
                        if line[9:-1].isalnum():
                            print(True)
                        else:
                            if lvar[line[9:-1]].isalnum():
                                print(True)
                            else:
                                print(False)
                    else:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                else:
                    if line.endswith("()"):
                        print("\033[91mUndefined Function or Method Passed.!\033[1;37m")
                        print(line)
                    elif line in lact:
                        print(lact[line])
                        pass
                    elif line in lvar:
                        print(lvar[line])
                        pass
                    elif line.endswith("]"):
                        varn, arr = line.split(" ")
                        arr = int(arr[1:-1])
                        if arr > len(lvar[varn]) or arr < len(lvar[varn]):
                            if varn in lvar:
                                try:
                                    print(lvar[varn][arr])
                                except:
                                        print("\033[91mArray index out of bound\033[1;37m")
                                else:
                                    print("\033[91mVariable not found\033[1;37m")
                            else:
                                print("\033[91mIndex out of range\033[1;37m")
                        else:
                            print(line)
                            print("\033[91mInvalid Keyword or Variable Passed.!\033[1;37m")
    except:
        print("\033[91mError : File not found\033[1;37m")

if __name__ == "__main__":
    if len(sys.argv) != 2:
<<<<<<< Updated upstream
        print("ProcyoLang 1.0.2 Beta 1")
        print("Error : No input file specified")
        print("Usage : pl <filename>")
=======
        print("ProcyoLang 2.0.1 Beta 2")
        print("\033[91m[!] Error: No input file specified!\033[0m")
        print("Usage: pl <filename>")
>>>>>>> Stashed changes
        sys.exit(1)

    filename = sys.argv[1]
    if filename == "-v" or filename == "-ver" or filename == "--v" or filename == "--ver":
        print("ProcyoLang 1.0.2 Beta 1")
        print("Gautham Nair")
        sys.exit(0)
    try:
        run_file(filename)
    except:
        print("ProcyoLang 1.0.2 Beta 1")
        print("Error : File not found")
        sys.exit(1)