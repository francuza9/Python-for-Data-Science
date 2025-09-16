from defines import Exercise	
import subprocess
from pathlib import Path
from defines import PATH_TO_EXERCISES, PASS_EMOJI, FAIL_EMOJI
import time

def fuzzy_time_compare_str(actual: str, expected: str, expected_len: int) -> bool:
	if len(actual) != expected_len:
		return False

	if actual[0] != '1' and actual[1] != ',' and actual[5] != ',' and actual[9] != ',' and actual[13] != '.':
		return False
	# check if inbetween 1-5 5-9 and 9-13 are digits
	if not (actual[2:5].isdigit() and actual[6:9].isdigit() and actual[10:13].isdigit()):
		return False

	return True

path = Path(__file__).parent / PATH_TO_EXERCISES / "ex01/format_ft_time.py"
scirpt_output = subprocess.run(
	f"python3 {str(path)} | cat -e",
	shell=True,
	capture_output=True,
	text=True,
)
actual_output = scirpt_output.stdout
err_output = scirpt_output.stderr
print("ex01:")
if err_output:
	print(FAIL_EMOJI)
	exit(1)
if actual_output[0:33] != "Seconds since January 1, 1970: 1,":
	print(FAIL_EMOJI)
	exit(1)

first_time_str_actual = actual_output[31:49]
first_time_str_expected = f"{time.time():,.4f}"
if not fuzzy_time_compare_str(first_time_str_actual, first_time_str_expected, len(first_time_str_expected)):
	print(FAIL_EMOJI)
	exit(1)

last_part_str_actual = actual_output[49:85]
last_part_str_expected = " or 1.76e+09 in scientific notation$"
if last_part_str_actual != last_part_str_expected:
	print(FAIL_EMOJI)
	exit(1)


last_date_actual = actual_output[86:]
last_date_expected = time.strftime("%B %d %Y", time.localtime()) + "$\n"
if last_date_actual != last_date_expected:
	print(FAIL_EMOJI)
	exit(1)

print(PASS_EMOJI)


# ex01.run()
# ex01.summary()