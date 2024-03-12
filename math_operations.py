from typing import Union, TypeVar

T = TypeVar('T', int, float)  # Type variable for numeric types

class MathOperations:

  def add(self, num1: T, num2: T) -> T:
    """Adds two numbers and returns the sum."""
    return num1 + num2

  def divide(self, numerator: float, denominator: float) -> float:
    """Divides two numbers and returns the quotient."""
    if denominator == 0:
      raise ZeroDivisionError("Division by zero")
    return numerator / denominator

  def factorial(self, number: int) -> int:
    """Calculates the factorial of a non-negative integer."""
    if number < 0:
      raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, number + 1):
      result *= i
    return result
