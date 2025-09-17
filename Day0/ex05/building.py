import sys
import string


def assertError(comparison: bool, message: str) -> None:
    try:
        assert comparison, message
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)


def count_characters(text: str) -> dict:
    counts = {
        "upper": sum(c.isupper() for c in text),
        "lower": sum(c.islower() for c in text),
        "punctuation": sum(c in string.punctuation for c in text),
        "spaces": sum(c.isspace() for c in text),
        "digits": sum(c.isdigit() for c in text),
        "total": len(text)
    }
    return counts


def print_counts(counts: dict) -> None:
    print(f"The text contains {counts['total']} characters:")
    print(counts['upper'], "upper letters")
    print(counts['lower'], "lower letters")
    print(counts['punctuation'], "punctuation marks")
    print(counts['spaces'], "spaces")
    print(counts['digits'], "digits")


def main() -> int:
    argv = sys.argv
    text = ""
    assertError(len(argv) <= 2, "more than one argument is provided")
    if len(argv) == 1 or argv[1] == "":
        try:
            print("What is the text to count?")
            text = sys.stdin.readline()
        except KeyboardInterrupt:
            pass
    else:
        text = argv[1]
    counts = count_characters(text)
    print_counts(counts)
    return 0


if __name__ == "__main__":
    main()
