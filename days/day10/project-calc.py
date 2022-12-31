
def add(n1, n2):
  """ Add two number and return the result. """
  return n1 + n2

def subtract(n1, n2):
  """ Subtract two number and return the result. """
  return n1 - n2

def multiply(n1, n2):
  """ Multiply two number and return the result. """
  return n1 * n2

def divide(n1, n2):
  """ Divide two number and return the result. """
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  number_1 = float(input("What's the first number?: "))
  symbol = [x for x in operations]

  while True:
    operation_symbol = input(f"Pick an operation: {' '.join(symbol)} ")
    
    if operation_symbol not in ["+", "-", "*", "/"]:
      print("invalid operation!")
      continue

    number_2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(number_1, number_2)
    print(f"{number_1} {operation_symbol} {number_2} = {answer}")
    
    if input(f"Type 'c' to continue with {answer}, or type 'q' to quit: ") == 'q':
      break
    
    number_1 = answer

if __name__ == "__main__":
  calculator()
