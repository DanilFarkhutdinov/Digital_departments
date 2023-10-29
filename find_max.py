import math


def find_max(array):
    max = -math.inf
    for number in array:
        if number > max:
            max = number
    return max


s = input()
try:
    array = list(map(int, s.split()))
    print(find_max(array))
except:
    print("Введены неверные данные")