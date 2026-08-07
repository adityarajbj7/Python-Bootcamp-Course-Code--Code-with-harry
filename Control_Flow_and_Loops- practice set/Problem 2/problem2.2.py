num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

opreation = input("Choose opreation: ")

match opreation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
        #Problem solved