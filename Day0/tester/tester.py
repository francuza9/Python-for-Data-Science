import sys

if len(sys.argv) != 2:
	print("Usage: python3 tester.py Detailed[y|n]")
	exit(1)

DETAILED = sys.argv[1].lower() == 'y'

import test_ex00
# import test_ex01
# import test_ex02




