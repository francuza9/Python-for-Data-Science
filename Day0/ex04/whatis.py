import sys


try:
	if len(sys.argv) == 1:
		exit(0)
	if len(sys.argv) > 2:
		raise AssertionError("more than one argument is provided")
	if not sys.argv[1].lstrip('-').isdigit():
		raise AssertionError("argument is not an integer")

	if int(sys.argv[1]) % 2:
		print("I'm Odd.")
	else:
		print("I'm Even.")
except Exception as e:
	print("AssertionError:", e)
	exit(1)