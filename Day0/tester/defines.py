import subprocess
from pathlib import Path
# from tester import DETAILED

PATH_TO_EXERCISES = "../"  # relative path to exercises
PASS_EMOJI = "✅"  # or "Y"
FAIL_EMOJI = "❌"  # or "X"


class Exercise:
	def __init__(self, name: str, path: str, expected_outputs: list, inputs: list = None):
		self.path = Path(__file__).parent / PATH_TO_EXERCISES / path
		self.expected_outputs = expected_outputs  # nested lists: variations per test
		self.inputs = inputs if inputs else [None] * len(expected_outputs)
		self.results = []  # True/False per test
		self.name = name

	def run(self):
		for idx, variations in enumerate(self.expected_outputs):
			input_data = self.inputs[idx]
			result = subprocess.run(
				f"python3 {str(self.path)} | cat -e",
				shell=True,
				capture_output=True,
				text=True,
			)

			output = result.stdout

			# Check if output matches any variation
			passed = any(output.strip() == variation.strip() for variation in variations)
			self.results.append(passed)

	def summary(self):
		emojis = [PASS_EMOJI if r else FAIL_EMOJI for r in self.results]
		print(f"{self.name}:")
		print("\t".join(emojis))