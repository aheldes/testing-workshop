from .math_operations import MathOperations

def test_add_correct():
  """Tests that add function returns the sum of two numbers."""
  result = MathOperations().add(5, 3)
  assert result == 8

def test_add_floats():
  """Tests that add function works with floating-point numbers."""
  result = MathOperations().add(2.5, 1.7)
  assert result == 4.2

def test_add_strings_raises_error():
  """Tests that adding strings raises a TypeError."""
  with pytest.raises(TypeError):
    MathOperations().add("10", "20")

def test_divide_correct():
  """Tests that divide function returns the quotient."""
  result = MathOperations().divide(10, 2)
  assert result == 5

def test_divide_by_zero_raises_error():
  """Tests that divide function raises ZeroDivisionError for division by zero."""
  with pytest.raises(ZeroDivisionError):
    MathOperations().divide(10, 0)

def test_factorial_correct():
  """Tests that factorial function calculates the factorial correctly."""
  result = MathOperations().factorial(5)
  assert result == 120

def test_factorial_negative_raises_error():
  """Tests that factorial function raises ValueError for negative input."""
  with pytest.raises(ValueError):
    MathOperations().factorial(-3)
