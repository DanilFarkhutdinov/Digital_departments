def list_comprehensions(lst):
    try:
        lst = [int(n) for n in lst]
        print("Четные: ", [n for n in lst if n % 2 == 0])
        print("Нечетные: ", [n for n in lst if n % 2 == 1])
        print("Меньше 0: ", [n for n in lst if n < 0])
    except:
        print(-1)


def list_map_filter(lst):
    try:
        lst = list(map(int, lst))
        print("Четные: ", list(filter(lambda n: n % 2 == 0, lst)))
        print("Нечетные: ", list(filter(lambda n: n % 2 == 1, lst)))
        print("Меньше 0: ", list(filter(lambda n: n < 0, lst)))
    except:
        print(-1)


numbers = input("Введите числа через пробел: ").split()
print("list comprehensions")
list_comprehensions(numbers)
print()
print("map and filter")
list_map_filter(numbers)