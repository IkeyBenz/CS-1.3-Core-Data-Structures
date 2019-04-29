def calculate(string: str) -> float:

    def _simplify(string: str, operation: str) -> float:

        index_of_operation = indexOf(string, operation)

        if index_of_operation is not None:
            pre = get_previous_number(string, index_of_operation)
            post = get_next_number(string, index_of_operation)

            result = str(do_math(pre, post, operation))

            simplified = string.replace(f'{pre}{operation}{post}', result)

            return _simplify(simplified, operation)

        return string

    string = remove_spaces(string)

    for operation in ["*", "/", "+", "-"]:
        string = _simplify(string, operation)

    return float(string)


def do_math(num1: int, num2: int, operation: str) -> int:

    if operation == "*":
        return num1 * num2
    if operation == "/":
        return num1 / num2
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2


def get_next_number(string: str, index: int) -> float:

    assert 0 <= index < len(string)-1, IndexError(
        "Index must be between 0 and len(string)-1")

    number = ""
    index += 1

    while index < len(string) and (string[index].isdigit() or string[index] is "."):
        number += string[index]
        index += 1

    return float(number)


def get_previous_number(string: str, index: int) -> float:

    assert 0 < index < len(string), IndexError(
        "Index must be between 0 and len(string)")

    number = ""
    index -= 1  # Getting the number before here, so exclude this index

    while index >= 0 and (string[index].isdigit() or string[index] is "."):
        # Prepend new number (moving backwards)
        number = string[index] + number
        index -= 1

    return float(number)


def indexOf(string: str, substring: str) -> int:
    """ Returns the index of the first character of the substring in string.
    Returns None if substring cannot be found.
    Runtime: ? """

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return i

    return None


def remove_spaces(string: str) -> str:
    " Removes every space in the string. Returns new string. "

    new = ""

    for char in string:
        if char is not " ":
            new += char

    return new

# ------------- TESTS --------------


def test_get_previous_number():
    cases = [
        {  # Number is in middle of string
            "string": "123-345+345",
            "index": 7,
            "expected": 345.0
        },
        {
            "string": "4*2+74-85/12",
            "index": 9,
            "expected": 85.0
        },
        {  # Number is begining of string
            "string": "12/2",
            "index": 2,
            "expected": 12.0
        },
        {  # string[index] is a digit
            "string": "17+12-24",
            "index": 7,
            "expected": 2.0
        },
        {   # With decimal
            "string": "1.0/4",
            "index": 3,
            "expected": 1.0
        }
    ]

    for case in cases:
        actual = get_previous_number(case["string"], case["index"])
        assert actual == case["expected"], f'{actual} != {case["expected"]}'

    print("All tests passed for get_previous_number()")


def test_indexOf():
    cases = [
        {
            "string": "hello",
            "substring": "el",
            "expected": 1
        },
        {
            "string": "what's up",
            "substring": "'s",
            "expected": 4
        },
        {
            "string": "123456789",
            "substring": "9",
            "expected": 8
        },
        {
            "string": "peter",
            "substring": "j",
            "expected": None
        }
    ]

    for case in cases:
        assert indexOf(case["string"], case["substring"]
                       ) == case["expected"], case

    print("All tests passed for indexOf()")


def test_get_next_number():
    cases = [
        {   # Number is end of string
            "string": "1+2+3",
            "index": 3,
            "expected": 3.0
        },
        {   # Number is begining of string
            "string": "-1+2+3",
            "index": 0,
            "expected": 1.0
        },
        {   # Number is in middle of string
            "string": "-1+2+3+4",
            "index": 4,
            "expected": 3.0
        },
    ]

    for case in cases:
        actual = get_next_number(case["string"], case["index"])
        assert actual == case["expected"], f'{actual} != {case["expected"]}'

    print("All tests passed for get_next_number()")


def test_calculate():
    cases = [
        {
            "in": "1 * 2 - 3 + 4 / 2",
            "expected": "2-3+4/2"
        },
    ]

    for case in cases:
        actual = calculate(case["in"])
        assert actual == case["expected"], f'{actual} != {case["expected"]}'

    print("All tests passed for calculate()")


def run_all_tests():
    for test in [
        test_indexOf,
        test_get_previous_number,
        test_get_next_number,
        # test_calculate
    ]:
        test()


if __name__ == '__main__':
    run_all_tests()
