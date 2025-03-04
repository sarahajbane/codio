# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-03-22 05:33:50
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-10-09 14:34:22

"""
[SE102] Calculator
"""

# define global constant
SUPPORTED_OPERATORS = ("+", "-", "*", "/", "~")


def get_operator(operation):
    """
    Returns operator from given operation
    """
    for operator in SUPPORTED_OPERATORS:
        if operator in operation:
            return operator
    return None


def calculate(operation):
    """
    Prints result of given operation
    """
    operator = get_operator(operation)

    # validate operator
    if not operator:
        print("Only support operators:", SUPPORTED_OPERATORS)
        return

    # split operation by operator to get operands
    operands = operation.split(operator)
    first_num = int(operands[0])
    second_num = int(operands[1])
    if operator == "+":
        print(f"The answer is {first_num + second_num}")
    if operator == "-":
        print(f"The answer is {first_num - second_num}")
    if operator == "*":
        print(f"The answer is {first_num * second_num}")
    if operator == "/":
        print(f"The answer is {first_num / second_num}")
    if operator == "~":
        print(f"The answer is {first_num // second_num}")
        print(f"The remainder is {first_num % second_num}")


def main():
    """
    Main function
    """
    print("Welcome to the Python calculator!")
    nb_calculations = int(input("How many calculations do you want to do? "))
    for _ in range(nb_calculations):
        operation = input("What do you want to calculate? ")
        calculate(operation)


if __name__ == "__main__":
    main()