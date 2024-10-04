def safe_divide(numerator, denominator):

  try:
    numerator = float(numerator)
    denominator = float(denominator)

    result = numerator / denominator
  
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

  except ValueError:
    print("Error: Please enter numeric values only.")

  except Exception:
    print('Something went wrong')

  else:
    print(f"The result of division is {result}")