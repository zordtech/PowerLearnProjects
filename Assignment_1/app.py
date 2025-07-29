#first PLP python assignment
num1 = float(input("enter a number: "))
operator = input("enter an operator: + , - , /, * ")
num2 = float(input("enter another number: "))
if operator == "+": 
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif operator != "+" "-" "*" "/":
    print("Enter a valid operator")
else : 
    print("invalid input")

