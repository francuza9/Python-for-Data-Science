

def main():
	"""
	This program displays the sums of its upper-case characters, lower-case
	characters, punctuation characters, digits and spaces.
	
	Parameters:
	arg1 (str): input_string to be parsed.

	returns:
	No return value.

	Example:
	>>> py building.py "Hello World!"
	2 upper letters
	8 lower letters
	1 punctuation marks
	1 spaces
	0 digits
	"""
	import sys
	import string
	
	try:
		assert len(sys.argv) < 3, "more than one argument is provided"
	except AssertionError as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
	
	input_string = None

	if len(sys.argv) < 2 or sys.argv[1] == "":
		print("What is the text to count?")
		lines = []
		try:
			while True:
				line = input()
				lines.append(line)
		except EOFError:
			pass
		input_string = "\n".join(lines)


	
	if input_string is None:
		input_string = sys.argv[1]
	
	try:
		assert type(input_string) is str
	except AssertionError as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
	
	try:
		assert input_string.isprintable(), "argument is not printable"
	except AssertionError as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
	
	upper = 0
	lower = 0
	punctuation = 0
	digits = 0
	spaces = 0

	for char in input_string:
		if char.isupper():
			upper += 1
		elif char.islower():
			lower += 1
		elif char in string.punctuation:
			punctuation += 1
		elif char.isdigit():
			digits += 1
		elif char.isspace():
			spaces += 1
	
	print(f"The text contains {len(input_string)} characters:")
	print(f"{upper} upper letters")
	print(f"{lower} lower letters")
	print(f"{punctuation} punctuation marks")
	print(f"{spaces} spaces")
	print(f"{digits} digits")




if __name__ == "__main__":
	main()