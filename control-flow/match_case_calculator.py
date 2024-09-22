num1= input("Enter the first number:")
num2= input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")
match operation:
  case "For addition (+)":
    result = num1 + num2
    print(f"The result is {result}")
  case " subtract (-)":
    result = num1 - num2
    print(f"The result is {result}")
  case " multiply (*)":
    result= num1*num2
    print(f"The result is {result}")
  case "divide (/)":
    if num2 == 0:
      print("Cannot divide by zero.")
    else:
      result= num1%num2
      print("The result is {result}")
  case _:
    print("Invalid opperation. Please choose +, -, * or % .")
  

