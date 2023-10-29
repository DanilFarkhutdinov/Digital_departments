def find_max(*args):
    if len(args) == 0:
        return None
    else:
        max = args[0]
    for number in args:
        if number > max:
            max = number
    return max


print(find_max(5, 3, 8, 10, 3))