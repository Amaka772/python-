Print ("select an operation to perform )
Print("1.ADD")
Print("2.SUBTRACT")
Print("3.MULTIPLY")
Print("4.DIVIDE")

Operation = input()
if operation == "1":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    Print("The sum is" + str(int(num1)+int(num2)))
elif operation == "2":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    Print("The result is" + str(int(num1)-int(num2)))
elif operation == "3":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    Print("The result is" + str(int(num1)*int(num2)))
elif operation == "4":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    Print("The result is" + str(int(num1)/int(num2)))
