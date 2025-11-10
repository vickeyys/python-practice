import sys

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def dev(a, b):
    if b == 0:
        return "cannot devide by zero!"
    return a/b

print("simple calculation")
print("avaialble operations (+,-,*,/)")

num1 = float(sys.argv[1])
op   = sys.argv[2]
num2 = float(sys.argv[3])

if op == "+":
    print(add(num1, num2))
elif op == "-":
    print(sub(num1, num2))
elif op == "*":
   print(mul(num1, num2))
elif op == "/":
    print(dev(num1, num2))
else:
    print("wront input")
    
