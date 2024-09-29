def print_square():

  x = int(input("Enter the size of the pattern: "))

  print(f"This is square of {x} as length")

  row = 1

  while row <= x:
    for i in range(x):
      print("*", end="")
    else:
      print()

    row += 1
  
  else:
    print()

print_square()
print_square()
print_square()


