def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Cannot divide by zero")
    else:
        return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print("This is Ola's Calculator!\nFor this version, please press ENTER between every number and operation.\nThank you for cooperation")


def calculator():
    num1 = int(input())
    continue_with_answer = True
    
    while continue_with_answer:

        operator = input()
        if operator not in operations:
            print("Invalid operator")

        num2 = int(input())
            
        answer = operations[operator](num1, num2)
        print(f"= {answer}")
    
        if input("press 'y' to continue on 'n' to restart\n") == "y":
            num1 = answer
            print(f"{answer}")
        else: 
            continue_with_answer = False
            calculator()

calculator()



