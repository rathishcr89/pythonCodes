
# Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b) -> int:
    return (a + b)
def mul(a, b) -> int:
    return (a * b)
def minus(a, b) -> int:
    return (a - b)
def divide(a, b) -> int:
    return (a / b)
def divide2(a, b) -> int:
    return (a // b)
def modulo(a, b) -> int:
    return (a % b)
def readInpu(arg):
    """
    Read an integer input from the user.
    
    :param arg: Argument to indicate which number to read.
    :return: The integer input from the user.
    """
    try:
        inputno = int(input(f'Enter number {arg}: '))
    except ValueError as e:
        print(f"An unexpected error occurred due to invalid Input: {e}, number {arg} value will be replace with 0")
        return 0
    else:
        return inputno

# Main program to read two numbers and perform operations
if __name__ == "__main__":
    print("This program will read two numbers and perform sum and multiplication on them.")
#a=readInpu(1)
#b=readInpu(2)
a=5
b=4
print(f"Sum of {a} and {b} is {sum(a, b)}")
print(f"Minus of {a} and {b} is {minus(a, b)}")
print(f"Multiplication of {a} and {b} is {mul(a, b)}")
print(f"Division of {a} and {b} is {divide(a, b)}")
print(f"Division 2 of {a} and {b} is {divide2(a, b)}")
print(f"Mod of {a} and {b} is {modulo(a, b)}")

