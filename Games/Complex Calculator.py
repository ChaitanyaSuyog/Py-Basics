
number_1 = float(input("Enter a number: "))

operation = input("What operation do you want to use?(+, -, *, /) ")

number_2 = float(input("Enter another number: "))

if operation == "+":
    result = number_1 + number_2
    print(result)
elif operation == "-":
    result = number_1 - number_2
    print(result)
elif operation == "*":
    result = number_1 * number_2
    print(result)
elif operation == "/":
    result = number_1 / number_2
    print(result)

else:
    print("Undefined. Enter a valid function: +, -, *, or /.")

