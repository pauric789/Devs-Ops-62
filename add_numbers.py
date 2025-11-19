"""This module contains utility functions for adding numbers."""
def add_numbers(a, b):
    """
     Adds two numbers together.

     @author Pauric Mc Menamin
     @version 1.0
     @param a: The first number to add.
     @param b: The second number to add.
     @return: The sum of a and b.
     """
    return a + b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add_numbers(num1, num2)
print(f"Result: {result}")