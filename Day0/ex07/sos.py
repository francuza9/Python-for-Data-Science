import sys


def main() -> None:
    """ Main function to convert text to Morse code. """
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }
    try:
        argv = sys.argv
        if len(argv) != 2:
            raise AssertionError("the arguments are bad")
        for char in argv[1]:
            if not char.isdigit() and not char.isalpha() and char != ' ':
                raise AssertionError("the arguments are bad")
        text = argv[1].upper()
        for i, char in enumerate(text):
            end = "" if i == len(text) - 1 else " "
            print(NESTED_MORSE[char], end=end)
        print()
    except Exception as e:
        print("AssertionError:", e)
        return (1)
    return (0)


if __name__ == "__main__":
    main()
