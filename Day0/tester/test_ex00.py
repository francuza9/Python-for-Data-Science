from defines import PATH_TO_EXERCISES, PASS_EMOJI, FAIL_EMOJI
from tester import DETAILED
import subprocess
from pathlib import Path
import sys
import io

path = Path(__file__).parent / PATH_TO_EXERCISES / "ex00/Hello.py"
expected_outputs = [
	"['Hello', 'World!']$\n('Hello', 'France!')$\n{'Hello', 'Angouleme!'}$\n{'Hello': '42Angouleme!'}$\n",
	"['Hello', 'World!']$\n('Hello', 'France!')$\n{'Angouleme!', 'Hello'}$\n{'Hello': '42Angouleme!'}$\n",
	"['Hello', 'World']$\n('Hello', 'France')$\n{'Hello', 'Angouleme'}$\n{'Hello': '42Angouleme'}$\n",
	"['Hello', 'World']$\n('Hello', 'France')$\n{'Angouleme', 'Hello'}$\n{'Hello': '42Angouleme'}$\n",
]

print(path)
result = subprocess.run(
	f"python3 {str(path)} | cat -e",
	shell=True,
	capture_output=True,
	text=True,
)
printed = result.stdout

print("ex00:")
if result.stderr:
	if DETAILED:
		print("---")
		print("Error: ", repr(subprocess.stderr))
	print(FAIL_EMOJI)
	exit(1)
if printed not in expected_outputs:
	if DETAILED:
		print("---")
		print("Printed: ", repr(printed))
		print("Expected one of: ", [repr(e) for e in expected_outputs])
	print(FAIL_EMOJI)
else:
	if DETAILED:
		print("---")
		print("Printed: ", repr(printed))
		print("Expected one of: ", [repr(e) for e in expected_outputs])
	print(PASS_EMOJI)
