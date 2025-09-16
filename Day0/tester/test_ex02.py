
from defines import PATH_TO_EXERCISES, PASS_EMOJI, FAIL_EMOJI
from pathlib import Path
from tester import DETAILED
import subprocess
import io
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
ex02_path = os.path.abspath(os.path.join(current_dir, f"{PATH_TO_EXERCISES}ex02"))
if ex02_path not in sys.path:
    sys.path.insert(0, ex02_path)

# if f"{PATH_TO_EXERCISES}ex02" not in sys.path:
# 	print(f"Adding {PATH_TO_EXERCISES}ex02 to sys.path")
# 	sys.path.insert(0, PATH_TO_EXERCISES)

from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
ft_str_brian = "Brian"
ft_str_toto = "Toto"
ft_int = 10
ft_bool = True
ft_none = None

ft_list_expected = "List : <class 'list'>\n"
ft_tuple_expected = "Tuple : <class 'tuple'>\n"
ft_set_expected = "Set : <class 'set'>\n"
ft_dict_expected = "Dict : <class 'dict'>\n"
ft_str_brian_expected = "Brian is in the kitchen : <class 'str'>\n"
ft_str_toto_expected = "Toto is in the kitchen : <class 'str'>\n"
ft_int_return_expected = "42\n"
ft_int_expected = "Type not found\n"
ft_bool_expected = "Type not found\n"
ft_none_expected = "Type not found\n"

tests = [
	(ft_list, ft_list_expected),
	(ft_tuple, ft_tuple_expected),
	(ft_set, ft_set_expected),
	(ft_dict, ft_dict_expected),
	(ft_str_brian, ft_str_brian_expected),
	(ft_str_toto, ft_str_toto_expected),
	(ft_int, ft_int_expected),
	(ft_bool, ft_bool_expected),
	(ft_none, ft_none_expected)
]

print("ex02:")

for (thing, expected) in tests:
	original_stdout = sys.stdout
	captured_output = io.StringIO()
	sys.stdout = captured_output
	result = all_thing_is_obj(thing)
	printed = captured_output.getvalue()
	sys.stdout = original_stdout
	if printed != expected:
		if DETAILED:
			print("---")
			print("Printed: ", repr(printed))
			print("Expected: ", repr(expected))
		print(FAIL_EMOJI, end=" ")
	else:
		if DETAILED:
			print("---")
			print("Printed: ", repr(printed))
			print("Expected: ", repr(expected))
		print(PASS_EMOJI, end=" ")
	
original_stdout = sys.stdout
captured_output = io.StringIO()
sys.stdout = captured_output
result = all_thing_is_obj(42)
sys.stdout = original_stdout
if result != 42:
	if DETAILED:
		print("---")
		print("Returned: ", result)
		print("Expected: 42")
	print(FAIL_EMOJI)
else:
	if DETAILED:
		print("---")
		print("Returned: ", result)
		print("Expected: 42")
	print(PASS_EMOJI)



