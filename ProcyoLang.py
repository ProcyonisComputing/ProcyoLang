import os
import sys
import time
import art
import tqdm
from time import sleep
from time import time as timer
from time import sleep as delay
from platform import processor, system, version
import matplotlib.pyplot as plt
import psutil

if sys.platform == "win32":
    os.system('cls')
else:
    os.system('clear')

sleep(5)

modules = ['matplotlib.pyplot', 'platform', 'psutil', 'os', 'sys', 'time', 'art', 'time']
for module in tqdm.tqdm(modules):
    try:
        globals()[module.split('.')[0]] = __import__(module)
    except ImportError as e:
        print(f"\033[91mError : {e}\033[1;37m")

sleep(2)

print(art.text2art("ProcyoLang", "random"))
print("Starting...")
sleep(5)
if sys.platform == "win32":
    os.system('cls')
else:
    os.system('clear')
if sys.platform == "win32":
    os.system('cls')
else:
    os.system('clear')

try:
    import matplotlib.pyplot as plt
except:
    print("\033[91mInitialization of plot engine failed\033[1;37m")
    sleep(1)

try:
    import platform
    import psutil
except:
    print("\033[91mInitialization of system modules failed\033[1;37m")

print(art.text2art("ProcyoLang", "random"))
print("ProcyoLang")
print("1.0.1 Alpha 10")
print("Gautham Nair")
print("----------------------------------------")
print("/!\ This mode (interactive mode) will be removed from Beta releases. Beta release starts after Alpha 10..!")
prompt = ""
var = {}
adr = {}
act = {}
while prompt not in  ["exit", "quit", "exit()", "quit()"]:
    prompt = input("ProcyoLang $ ")
    if prompt.startswith("print "):
        if prompt[6:].isdigit():
            print(prompt[6:])
        elif prompt[6:] in var:
            print(var[prompt[6:]])
        elif prompt[6:].startswith('"'):
            if prompt.endswith('"'):
                print(prompt[7:-1])
            else:
                print("\033[91mError : Invalid Syntax\033[1;37m")
        else:
            print("\033[91mNo such variable found to print\033[1;37m")
    elif prompt.startswith("timeout("):
        if prompt.endswith(")"):
            try:
                delay(int(prompt[8:-1]))
            except:
                print("\033[91mError : Invalid Syntax\033[1;37m")
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt == "print":
        print("\033[91mError : Statement expected after print\033[1;37m")
    elif prompt.startswith("echo "):
        print(prompt[5:])
    elif prompt.startswith("which "):
        if prompt[6:] == "cpu" or prompt[6:] == "CPU":
            print(platform.processor())
        elif prompt[6:] == "os" or prompt[6:] == "OS":
            print(platform.system() + " " + platform.version())
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("exec "):
        filename = prompt[5:]
        try:
            with open(filename, "r") as f:
                lvar = {}
                ladr = {}
                lact = {}
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
                        except Exception as e:
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
                        except Exception as e:
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
                    elif line.startswith("killact ") or prompt.startswith("unmask "):
                        if line.startswith("killact "):
                            varn = prompt[8:]
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
                    elif line.startswith("for "):
                        try:
                            iterating_var, in_command, command, action = line[4:].split(" ")
                            if in_command == "from":
                                start, end = command.split("~")
                                start = int(start)
                                end = int(end)
                                if action.startswith("print"):
                                    action, value = action.split("->")
                                    if value == iterating_var:
                                        for i in range(start, end + 1):
                                            print(i)
                                    elif value.isdigit():
                                        for i in range(start, end + 1):
                                            print(value)
                                    else:
                                        if value in lvar:
                                            for i in range(start, end + 1):
                                                print(lvar[value])
                                        elif value.startswith('"') and value.endswith('"'):
                                            value = value.replace("|s|", " ")
                                            for i in range(start, end + 1):
                                                print(value[1:-1])
                                        else:
                                            print("\033[91mError : Variable not found\033[1;37m")
                                else:
                                    print("\033[91mError : Invalid Syntax\033[1;37m")
                            elif in_command == "till":
                                if action.startswith("print"):
                                    action, value = action.split("->")
                                    command = int(command)
                                    if value == iterating_var:
                                        for i in range(0, command + 1):
                                            print(i)
                                    elif value.isdigit():
                                        for i in range(0, command + 1):
                                            print(value)
                                    else:
                                        if value in lvar:
                                            for i in range(0, command + 1):
                                                print(lvar[value])
                                        elif value.startswith('"') and value.endswith('"'):
                                            value = value.replace("|s|", " ")
                                            for i in range(0, command + 1):
                                                print(value[1:-1])
                                        else:
                                            print("\033[91mError : Variable not found\033[1;37m")
                                else:
                                    print("\033[91mError : Invalid Syntax\033[1;37m")
                            elif in_command == "noDuckTill":
                                if action.startswith("print"):
                                    action, value = action.split("->")
                                    command = int(command)
                                    if value == iterating_var:
                                        for i in range(1, command + 1):
                                            print(i)
                                    elif value.isdigit():
                                        for i in range(1, command + 1):
                                            print(value)
                                    else:
                                        if value in lvar:
                                            for i in range(1, command + 1):
                                                print(lvar[value])
                                        elif value.startswith('"') and value.endswith('"'):
                                            value = value.replace("|s|", " ")
                                            for i in range(1, command + 1):
                                                print(value[1:-1])
                                        else:
                                            print("\033[91mError : Variable not found\033[1;37m")
                                else:
                                    print("\033[91mError : Invalid Syntax\033[1;37m")                                                 
                            else:
                                print("\033[91mError : Invalid Syntax\033[1;37m")
                        except:
                            print("\033[91mError : Invalid Syntax\033[1;37m")
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
    elif prompt.startswith("sht "):
        print(f"Hello {prompt[4:]}, greetings from ProcyoLang..!")
    elif prompt.startswith("plot "):
        try:
            _, x, y = prompt.split()
            x, y = int(x), int(y)
            plt.plot([x], [y], marker='o')
            plt.title("ProcyoLang Plot")
            plt.xlabel("X-Axis")
            plt.ylabel("Y-Axis")
            plt.grid(True)
            plt.show()
        except ValueError:
            print("\033[91mError : Invalid Syntax\033[1;37m")
        except Exception as e:
            print("\033[91mError : ", e, "\033[1;37m")
    elif prompt.startswith("plotline "):
        try:
            _, x1, y1, x2, y2 = prompt.split()
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            plt.plot([x1, x2], [y1, y2], marker='o')
            plt.title('ProcyoLang Line Plot')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.grid(True)
            plt.show()
        except ValueError:
            print("\033[91mError : Invalid Syntax. Please use 'plotline x1 y1 x2 y2' format.\033[1;37m")
        except Exception as e:
            print(f"\033[91mAn error occurred: {e}\033[1;37m")
    elif prompt.startswith("system "):
        os.system(prompt[7:])
    elif prompt == "system":
        print("\033[91mNo value supplied\033[1;37m")
    elif prompt == "echo":
        print("\033[91mError : Statement expected after echo\033[1;37m")
    elif prompt.startswith("input "):
        input(prompt[6:])
    elif prompt == "input":
        print("\033[91mError : Statement expected after input\033[1;37m")
    elif prompt.startswith("type("):
        if prompt.endswith(")"):
            if prompt[5:-1] in var:
                dtype = str(type(var[prompt[5:-1]]))
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
    elif prompt.startswith("int("):
        if prompt.endswith(")"):
            if prompt[4:-1].isdigit():
                print(int(prompt[4:-1]))
            else:
                if prompt[4:-1] in var:
                    if var[prompt[4:-1]].isdigit():
                        var[prompt[4:-1]] = int(var[prompt[4:-1]])
                        print(var[prompt[4:-1]])
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("float("):
        if prompt.endswith(")"):
            if prompt[6:-1].replace(".", "").isdigit():
                print(float(prompt[6:-1]))
            else:
                if prompt[6:-1] in var:
                    if var[prompt[6:-1]].replace(".", "").isdigit():
                        var[prompt[6:-1]] = float(var[prompt[6:-1]])
                        print(var[prompt[6:-1]])
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("str("):
        if prompt.endswith(")"):
            if prompt[4:-1].startswith('"'):
                if prompt[4:-1].endswith('"'):
                    print(str(prompt[5:-2]))
                else:
                    print("\033[91mError : Invalid Syntax\033[1;37m")
            else:
                if prompt[4:-1] in var:
                    var[prompt[4:-1]] = str(var[prompt[4:-1]])
                    print(var[prompt[4:-1]])
                else:
                    print("\033[91mNo such variable found to typecast\033[1;37m")
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("bool("):
        if prompt.endswith(")"):
            if prompt[5:-1] in ['True', 'False', '1', '0']:
                print(bool(prompt[5:-1]))
            else:
                if prompt[5:-1] in var:
                    if var[prompt[5:-1]] in ['True', 'False', '1', '0']:
                        print(bool(var[prompt[5:-1]]))
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("isDigit("):
        if prompt.endswith(")"):
            if prompt[8:-1].isdigit():
                print(True)
            else:
                if prompt[8:-1] in var:
                    if var[prompt[8:-1]].isdigit():
                        print(True)
                    else:
                        print(False)
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("isChar("):
        if prompt.endswith(")"):
            if len(prompt[7:-1]) == 1:
                if prompt[7:-1] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', "'", '"', '\\', '|', ',', '.', '/', '?', '<', '>']:
                    print(True)
                else:
                    if prompt[7:-1] in var:
                        if var[prompt[7:-1]] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', "'", '"', '\\', '|', ',', '.', '/', '?', '<', '>']:
                            print(True)
                        else:
                            print(False)
            else:
                if prompt[7:-1] in ['\\0', '\\n', '\\t']:
                    print(True)
                else:
                    if var[prompt[7:-1]] in ['\\0', '\\n', '\\t']:
                        print(True)
                    else:
                        print(False)
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("isBool("):
        if prompt.endswith(")"):
            if prompt[7:-1] in ['True', 'False', '1', '0']:
                print(True)
            else:
                if var[prompt[7:-1]] in ['True', 'False', '1', '0']:
                    print(True)
                else:
                    print(False)
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("isFloat("):
        try:
            if prompt.endswith(")"):
                if prompt[8:-1].replace(".", "").isdigit():
                    print(True)
                else:
                    if var[prompt[8:-1]].replace(".", "").isdigit():
                        print(True)
                    else:
                        print(False)
            else:
                print("\033[91mError : Invalid Syntax\033[1;37m")
        except:
            print(False)
    elif prompt.startswith("isAlpha("):
        if prompt.endswith(")"):
            if prompt[8:-1].isalpha():
                print(True)
            else:
                if var[prompt[8:-1]].isalpha():
                    print(True)
                else:
                    print(False)
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("isAlnum("):
        if prompt.endswith(")"):
            if prompt[9:-1].isalnum():
                print(True)
            else:
                if var[prompt[9:-1]].isalnum():
                    print(True)
                else:
                    print(False)
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("isLower("):
        if prompt.endswith(")"):
            if prompt[9:-1].islower():
                print(True)
            else:
                if var[prompt[9:-1]].islower():
                    print(True)
                else:
                    print(False)
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("isUpper("):
        if prompt.endswith(")"):
            if prompt[9:-1].isupper():
                print(True)
            else:
                if var[prompt[9:-1]].isupper():
                    print(True)
                else:
                    print(False)
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("isSpace("):
        if prompt.endswith(")"):
            if prompt[9:-1].isspace():
                print(True)
            else:
                if var[prompt[9:-1]].isspace():
                    print(True)
                else:
                    print(False)
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("isTitle("):
        if prompt.endswith(")"):
            if prompt[9:-1].istitle():
                print(True)
            else:
                if var[prompt[9:-1]].istitle():
                    print(True)
                else:
                    print(False)
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt == "input":
        print("\033[91mError : Statement expected after input\033[1;37m")
    elif prompt == "help":
        print("ProcyoLang Help")
        print("print <statement> : Prints the statement")
        print("echo <statement> : Prints the statement")
        print("input <statement> : Takes input from the user")
        print("clr() : Clears the screen")
        print("ver() : Shows the version of ProcyoLang")
        print("exit : Exits the ProcyoLang")
        print("quit : Exits the ProcyoLang")
        print("exit() : Exits the ProcyoLang")
        print("quit() : Exits the ProcyoLang")
        print("var <variable_name> = <value> : Creates a variable")
        print("varops <operation> <variable_name> <variable_name> ... : Performs operations on variables")
        print("eval <expression> : Evaluates the expression")
        print("varupd <variable_name> = <value> : Updates the value of existing variable")
        print("act <variable_name> = <value> : Make variable masked with another value, doesn't replace original value")
        print("kill <variable_name> : Kills a variable")
        print("killact <variable_name> : Kills mask for a variable")
        print("system <command> : Execute system or shell commands")
    elif prompt.startswith("range "):
        range1, range2 = prompt[6:].split(" ")
        for i in range(int(range1), int(range2) + 1):
            print(i)
    elif prompt.startswith("adr "):
        try:
            print(id(var[prompt[4:]]))
        except:
            print("\033[91mVariable not found\033[1;37m")
    elif prompt == "clr()":
        if sys.platform == "win32":
            os.system('cls')
        else:
            os.system('clear')
    elif prompt == "":
        print()
    elif prompt == " ":
        print()
    elif prompt.startswith("adrcall "):
        val = prompt[8:]
        for k, v in adr.items():
            if str(v) == val:
                print(f"Variable: {k}, Value: {var[k]}")
    elif prompt.startswith("var "):
        if prompt[4] == " ":
            print("\033[91mError : Invalid Syntax")
        elif prompt[4] in ["-", "+", "/", "*", "!", "@", "#", "$", "%", "^", "&", "`", "~", ".", ",", "\\", "{", "}", "[", "]", ";", ":", "'", '"', "|", "<", ">", "?", "(", ")"]:
            print("\033[91mError : Invalid start of variable name\033[1;37m")
        else:
            varn, val = prompt[4:].split("=")
            varn = varn.strip(" ")
            val = val.strip(" ")
            if varn in var:
                print("\033[93mVariable already exists, use varupd to update variable content\033[1;37m")
            else:
                if val == " ":
                    print("\033[91mError : Invalid Syntax\033[1;37m")
                elif val.startswith('"'):
                    if val.endswith('"'):
                        var[varn] = val[1:-1]
                        adr[varn] = id(var[varn])
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
                            var[varn] = float(val)
                            adr[varn] = id(var[varn])
                        else:
                            print("\033[91mError : Invalid Syntax\033[1;37m")
                    else:
                        var[varn] = int(val)
                        adr[varn] = id(var[varn])
                elif val.startswith("'"):
                    if val.endswith("'"):
                        var[varn] = val[1:-1]
                        adr[varn] = id(var[varn])
                    else:
                        print("\033[91mError : Invalid Syntax\033[1;37m")
                else:
                    print("\033[93mUnknown datatype\033[93m")
    elif prompt.startswith("varupd "):
        varn, val = prompt[7:].split("=")
        varn = varn.strip(" ")
        val = val.strip(" ")
        del var[varn]
        del adr[varn]
        if val == " ":
            print("\033[91mError : Invalid Syntax\033[1;37m")
        elif val.startswith('"'):
            if val.endswith('"'):
                var[varn] = val[1:-1]
                adr[varn] = id(var[varn])
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
                    var[varn] = float(val)
                    adr[varn] = id(var[varn])
                else:
                    print("\033[91mError : Invalid Syntax\033[1;37m")
            else:
                var[varn] = int(val)
                adr[varn] = id(var[varn])
        elif val.startswith("'"):
            if val.endswith("'"):
                var[varn] = val[1:-1]
                adr[varn] = id(var[varn])
            else:
                print("\033[91mError : Invalid Syntax\033[1;37m")
        else:
            print("\033[93mUnknown datatype\033[93m")
    elif prompt.startswith("var[] "):
        varn, val = prompt[6:].split("=")
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
            var[varn] = val0
            adr[varn] = id(var[varn])
    elif prompt.startswith("kill "):
        varn = prompt[5:]
        del adr[varn]
        del var[varn]
    elif prompt.startswith("act ") or prompt.startswith("mask "):
        if prompt.startswith("act "):
            varn, val = prompt[4:].split("=")
            varn = varn.strip(" ")
            val = val.strip(" ")
            if varn in var:
                act[varn] = val
            else:
                print("\033[91mVariable not found to act or mask\033[1;37m")
        else:
            varn, val = prompt[5:].split("=")
            varn = varn.strip(" ")
            val = val.strip(" ")
            if varn in var:
                act[varn] = val
            else:
                print("\033[91mVariable not found to act or mask\033[1;37m")
    elif prompt.startswith("killact ") or prompt.startswith("unmask "):
        if prompt.startswith("killact "):
            varn = prompt[8:]
            varn = varn.strip(" ")
            if varn in act:
                del act[varn]
            else:
                print("\033[91mVariable not found to killact or unmask\033[1;37m")
        else:
            varn = prompt[7:]
            varn = varn.strip(" ")
            if varn in act:
                del act[varn]
            else:
                print("\033[91mVariable not found to killact or unmask\033[1;37m")
    elif prompt.startswith("bin("):
        if prompt.endswith(")"):
            print(bin(int(prompt[4:-1])))
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("oct("):
        if prompt.endswith(")"):
            print(oct(int(prompt[4:-1])))
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("hex("):
        if prompt.endswith(")"):
            print(hex(int(prompt[4:-1])))
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt.startswith("varops "):
        if prompt[7] == "+":
            varnl = []
            varnl = prompt[9:].split(" ")
            sum = 0
            for i in range(0, len(varnl)):
                try:
                    sum = float(sum) + float(var[varnl[i]])
                except:
                    print("\033[91mVariable likely contains value, not supported by varops\033[1;37m")
            print(sum)
        elif prompt[7] == "-":
            varnl = []
            varnl = prompt[9:].split(" ")
            dif = 0
            flag = 0
            for i in range(0, len(varnl)):
                if dif == 0 and flag == 0:
                    dif = float(var[varnl[i]])
                    flag = 1
                else:
                    try:
                        dif = float(dif) - float(var[varnl[i]])
                    except:
                        print("\033[91mVariable likely contains value, not supported by varops\033[1;37m")
            print(dif)
        elif prompt[7] == "*":
            varnl = []
            varnl = prompt[9:].split(" ")
            mul = 1
            for i in range(0, len(varnl)):
                try:
                    mul = float(mul) * float(var[varnl[i]])
                except:
                    print("\033[91mVariable likely contains value, not supported by varops\033[1;37m")
            print(mul)
        elif prompt[7] == "/":
            varnl = []
            varnl = prompt[9:].split(" ")
            div = None
            for i in range(0, len(varnl)):
                if div == None:
                    div = float(var[varnl[i]])
                else:
                    try:
                     div = div / float(var[varnl[i]])
                    except:
                        print("\033[91mVariable likely contains value, not supported by varops\033[1;37m")
            print(div)
        elif prompt[7] == "%":
            varnl = []
            varnl = prompt[9:].split(" ")
            mod = None
            for i in range(0, len(varnl)):
                if mod == None:
                    mod = float(var[varnl[i]])
                else:
                    try:
                        mod = mod % float(var[varnl[i]])
                    except:
                        print("\033[91mVariable likely contains value, not supported by varops\033[1;37m")
            print(mod)
        elif prompt[7:].startswith("bin "):
            try:
                print(bin(var[prompt[11:]]))
            except:
                print("\033[91mVariable likely contains value, not supported by varops\033[1;37m")
        elif prompt[7:].startswith("hex "):
            try:
                print(hex(var[prompt[11:]]))
            except:
                print("\033[91mVariable likely contains value, not supported by varops\033[1;37m")
        elif prompt[7:].startswith("oct "):
            try:
                print(oct(var[prompt[11:]]))
            except:
                print("\033[91mVariable likely contains value, not supported by varops\033[1;37m")
        else:
            print("\033[91mError : Invalid Syntax\033[1;37m")
    elif prompt == "ver()":
        print("ProcyoLang")
        print("1.0.1 Alpha 10")
        print("Gautham Nair")
    elif prompt.startswith("eval "):
        print(eval(prompt[5:]))
    elif prompt == "exit" or prompt == "quit" or prompt == "exit()" or prompt == "quit()":
        break
    else:
        if prompt.endswith("()"):
            print("\033[91mUndefined Function or Method Passed.!\033[1;37m")
            print(prompt)
        elif prompt in act:
            print(act[prompt])
            pass
        elif prompt in var:
            print(var[prompt])
            pass
        elif prompt.endswith("]"):
            varn, arr = prompt.split(" ")
            arr = int(arr[1:-1])
            if arr > len(var[varn]) or arr < len(var[varn]):
                if varn in var:
                    try:
                        print(var[varn][arr])
                    except:
                        print("\033[91mArray index out of bound\033[1;37m")
                else:
                    print("\033[91mVariable not found\033[1;37m")
            else:
                print("\033[91mIndex out of range\033[1;37m")
        else:
            print("\033[91mInvalid Keyword or Variable Passed.!\033[1;37m")