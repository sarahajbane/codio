# -*- coding: utf-8 -*-
# @Author: Sara Hajbane

"""
Prime numbers 
A Python program that checks if and prints all prime numbers within a given range.
Also includes a function to check if any number is divisible by any another number.
"""

def is_divisible_by(number, by):
    return number % by == 0


def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2,number):
        if is_divisible_by(number,i) == True:
            return False
        
    return True


def primes_in_range(start, end):
    primes = []

    for i in range(start, end):
        if is_prime(i):
            print(f"The number {i} is prime")
            primes.append(i)

    return primes


def main():
    start = int(input("Please enter the start of the range you want to check:"))
    end = int(input("Please enter the end of the range you want to check:"))
    primes_in_range(start, end)


if __name__ == "__main__":
    main()
