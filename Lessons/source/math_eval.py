from stack import Stack


def split_by(string: str, symbols: list, include_symbols=True) -> list:
    out = []
    curr = ""
    for c in string:
        if c in symbols:
            out.append(curr)
            out.append(c)
            curr = ""
        else:
            curr += c
    out.append(curr)
    return out


def simplify(expression: str, operations=[["*", "/"], ["+", "-"]]) -> str:
    curr_ops, rest_ops = operations[-1], operations[:-1]  # copy array

    symbols = Stack(split_by(expression, curr_ops)[::-1])

    while len(symbols) > 1:
        num1, operation, num2 = symbols.pop(), symbols.pop(), symbols.pop()
        if len(rest_ops) > 0:  # Possibly more to simplify
            num1 = simplify(num1, rest_ops)
            num2 = simplify(num2, rest_ops)

        result = calculate(float(num1), operation, float(num2))
        symbols.push(str(result))

    return symbols.pop()


def calculate(num1: float, operation: str, num2: float) -> float:
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        return num1 / num2


print(simplify("4-5+6*32/2+3*2-45"))
print(4-5+6*32/2+3*2-45)
