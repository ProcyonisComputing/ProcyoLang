import os
import sys
import time
from platform import processor, system, version
import matplotlib.pyplot as plt
import psutil

def run_file(filename):
    try:
        with open(filename, "r") as f:
            lvar = {}
            ladr = {}
            lact = {}
            lfor = []
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
        print("Usage : pl <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    run_file(filename)