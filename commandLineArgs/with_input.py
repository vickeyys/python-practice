def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # handle divide-by-zero safely
    if b == 0:
        return "❌ Cannot divide by zero!"
    return a / b

# --- Interactive input ---
print("🔹 Simple Calculator 🔹")
print("Available operations: +, -, *, /")

num1 = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", add(num1, num2))
elif op == "-":
    print("Result:", sub(num1, num2))
elif op == "*":
    print("Result:", mul(num1, num2))
elif op == "/":
    print("Result:", div(num1, num2))
else:
    print("❌ Invalid operator! Use +, -, *, /")
