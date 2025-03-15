# -*- coding: utf-8 -*-
# @Author: Sara Hajbane

"""
Calculator
This is a simple calculator that can perform addition, subtraction, multiplication, division and modulo operations.

"""

def multi(num):
      for i in range(num):
            ti = input("What do you want to calculate? ")
            calculate(ti)

def calculate(ti):
      if '~' in ti:
              result = int(ti[:ti.index('~')]) // int(ti[ti.index('~')+1:])
              remainder = int(ti[:ti.index('~')]) % int(ti[ti.index('~')+1:])
              print(f"The answer is {result}\n The remainder is {remainder}")
      elif '+' in ti:
              result = int(ti[:ti.index('+')]) + int(ti[ti.index('+')+1:])
              print(f"The answer is {result}")
              return result
      elif '-' in ti:
              result = int(ti[:ti.index('-')]) - int(ti[ti.index('-')+1:])
              print(f"The answer is {result}")
              return result
      elif '*' in ti:
              result = int(ti[:ti.index('*')]) * int(ti[ti.index('*')+1:])
              print(f"The answer is {result}")
              return result
      elif '/' in ti:
              result = int(ti[:ti.index('/')]) / int(ti[ti.index('/')+1:])
              print(f"The answer is {result}")
              return result
      else:
        print('input not recognised')


def main():
    """
    Main function
    """
    print("Welcome to the Python calculator!")
    num = int(input('How many calculations do you want to do?'))
    multi(num)

if __name__ == "__main__":
    main()
