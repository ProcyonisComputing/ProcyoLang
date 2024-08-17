def display(param):
    print(param)

def add(a):
    sum = 0
    for i in a:
        sum += i
    print(sum)

def sub(a):
    print(a[0] - a[1])

def mul(a):
    product = 1
    for i in a:
        product *= i
    print(product)

def div(a):
    print(a[0] / a[1])

def mod(a):
    print(a[0] % a[1])

def ver():
    print("1.0.2")

def help():
    print("display(param) - Display the parameter")
    print("take(var, param) - Take input and store it in a variable")
    print("add(a) - Add all the elements in the list")
    print("sub(a, b) - Subtract b from a")
    print("mul(a) - Multiply all the elements in the list")
    print("div(a, b) - Divide a by b")
    print("mod(a, b) - Return the remainder of a divided by b")
    print("ver() - Return the version of the library")
    print("help() - Display this help message")
    
def main():
    print("This is a library file. Do not run this file directly.")

