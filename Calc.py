def subtract(x, y):
    return x - y

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def division(x, y):
    return x / y

def main():
    print("Operations available are 1. subtraction 2. addition 3. multi 4. division")
    nums = input("Pick one of the operations: 1, 2, 3, 4")
    if nums == "1":
        num1 = float(input("Pick your first number"))
        num2 = float(input("Pick your second number:"))
        print(num1, "-" ,num2, "=" ,subtract(num1,num2))
    elif nums == "2":
        num3 = float(input("Pick your first number:"))
        num4 = float(input("Pick your second number:"))
        print(num3, "+", num4, "=", add(num3,num4))
    elif nums == "3":
        num5 = float(input("Pick your first number:"))
        num6 = float(input("Pick your second number:"))
        print(num5, "*", num6, "=", multiply(num5,num6))
    elif nums == "4":
        num7 = float(input("Pick your first number:"))
        num8 = float(input("Pick your second number:"))
        print(num7, "/", num8, "=", division(num7,num8))
    else:
        print("Invalid input")

def another_calc():
    another = input("Do you want to make another calculation?")
    if another == "yes":
        main()
        another_calc()
    elif another == "no":
        print("Thanks for using us!")
    else:
        print("Invlaid input")

main()
another_calc()
