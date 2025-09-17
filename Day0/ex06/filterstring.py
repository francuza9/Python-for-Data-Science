from ft_filter import ft_filter
import sys


def noSpecialChars(s: str) -> bool:
    """
    Checks if the string contains only
    alphanumeric characters and spaces.
    """
    for char in s:
        if not char.isalnum() and char != ' ':
            return False
    return True


def main():
    """
    Main function to filter words longer \
    than N characters from the input string S.
    """
    try:
        argv = sys.argv
        if len(argv) != 3:
            raise AssertionError("the arguments are bad")
        S = argv[1]
        N = argv[2]
        if not N.lstrip('-').isdigit():
            raise AssertionError("the arguments are bad")
        if not noSpecialChars(S):
            raise AssertionError("the arguments are bad")
        try:
            N = int(N)
        except ValueError:
            print("AssertionError: the arguments are bad")
            return (1)
        words = ft_filter(lambda x: len(x) > N, S.split(' '))
        print(words)

    except Exception as e:
        print("AssertionError:", e)
        return (1)
    return (0)


if __name__ == "__main__":
    main()
