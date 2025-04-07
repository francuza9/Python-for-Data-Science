import sys

if len(sys.argv) < 2:
	sys.exit(1) 
try:
	assert len(sys.argv) == 2, "more than one argument is provided"
except AssertionError as e:
	print(f"AssertionError: {e}")
	sys.exit(1)

try:
	assert sys.argv[1].lstrip("-+").isdigit(), "argument is not an integer"
except AssertionError as e:
	print(f"AssertionError: {e}")
	sys.exit(1)

try:
	n = int(sys.argv[1])
except:
	print(f"AssertionError: {AssertionError('argument is not an integer')}")
	sys.exit(1)

print("I'm Even." if n % 2 == 0 else "I'm Odd.")
