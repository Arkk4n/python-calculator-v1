def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

def mult(n1, n2):
    return n1 * n2

operators = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mult
}

def calc():
    first_number = float(input("Enter first number: "))
    continue_loop = True
    while continue_loop:
        operator = input("Enter operator: ")
        second_number = float(input("Enter second number: "))
        result = operators[operator](first_number, second_number)
        print(result)
        continue_loop = input("Continue? (y/n): ")
        if continue_loop == "y":
            first_number = result
        else:
            continue_loop = False
            print("\n" * 20)
            calc()

calc()

