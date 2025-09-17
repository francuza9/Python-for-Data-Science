import sys

if len(sys.argv) == 1:
	exit(0)

try:
	assert len(sys.argv) <= 2, "more than one argument is provided"
	assert sys.argv[1].lstrip('-').isdigit(), "argument is not an integer"

	if int(sys.argv[1]) % 2:
		print("I'm Odd.")
	else:
		print("I'm Even.")
except AssertionError as e:
	print("AssertionError:", e)
	exit(1)