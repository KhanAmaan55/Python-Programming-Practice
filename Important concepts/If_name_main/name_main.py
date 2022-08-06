def calc(a, b):
    """
    special calculation
    """
    return (a//b)+(a/b)


def strprinting(s1):
    """
    printing a string
    """
    return f"Your string is : {s1}"


print(__name__)


if __name__ == "__main__":
    print(calc(10, 100))
    print(strprinting("This is a test"))
