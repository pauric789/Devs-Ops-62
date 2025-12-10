"""This module contains utility functions for adding numbers."""

import logging


def add_numbers(a, b):
    """
     Adds two numbers together.

     @author Pauric Mc Menamin
     @version 1.0
     @param a: The first number to add.
     @param b: The second number to add.
     @return: The sum of a and b.
     """
    logging.info("Received request to add %s and %s", a, b)
    sum_result = a + b
    logging.info("The calculated sum is %s", sum_result)
    return sum_result


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print(f"Result: {result}")
    
