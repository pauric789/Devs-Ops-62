"""This module contains utility functions for adding numbers."""

import logging
from fastapi import FastAPI
# Configure logging to show in Docker logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()

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


@app.get("/")
def health_check():
    """
    Health check endpoint
    """

    return {"status": "online", "owner": "Pauric Mc Menamin"}

@app.get("/add")
def api_add(a: int, b: int):

    """
    API endpoint to add two numbers
    """
    result = add_numbers(a, b)
    return {"sum": result}
