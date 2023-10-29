def read():
    x = int(input())
    y = int(input())
    operation = input()
    return x, y, operation


def eval(x, y, operation):
    switcher = {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y,
    }
    result = switcher.get(operation, "Ошибка")
    return result


def print_loop(expression, history):
    print()
    print(expression)
    print("+ ", history[0])
    print("- ", history[1])
    print("* ", history[2])
    print("/ ", history[3])
    print()


def REPL(history):
    x, y, operaion = read()
    result = eval(x, y, operaion)
    expression = str(x) + operaion + str(y) + "=" + str(result)
    if (operaion == "+"):
        history[0].append(expression)
    if (operaion == "-"):
        history[1].append(expression)
    if (operaion == "*"):
        history[2].append(expression)
    if (operaion == "/"):
        history[3].append(expression)
    print_loop(expression, history)


def main():
    history = [[],[],[],[]]
    while True:
        REPL(history)


if __name__ == "__main__":
    main()