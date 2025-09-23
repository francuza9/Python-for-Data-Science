def square(x: int | float) -> int | float:
	if not isinstance(x, (int, float)):
		raise TypeError("Input should be a number.")
	return x * x

def pow(x: int | float) -> int | float:
	if not isinstance(x, (int, float)):
		raise TypeError("Input should be a number.")
	return x ** x

def outer(x: int | float, function) -> object:
	if not isinstance(x, (int, float)):
		raise TypeError("Input should be a number.")
	if not callable(function):
		raise TypeError("Input should be a function.")
	count = 0
	def inner() -> float:
		nonlocal count, x
		x = function(x)
		count += 1
		return x
	return inner
