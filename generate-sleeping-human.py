from sys import argv as args

if not args:
  print("Please enter an argument of number as length")
try:
  print(f"[(:D|{'-'*int(args[0])}]")
except ValueError:
  print("Please enter a valid number as argument")
