import functools
lst = list(map(lambda x: x * 2, [1, 2, 3]))
lst1 = list(filter(lambda x: x < 4, [1, 3, 8]))
print(sorted([1, 5, 3, 2, 4]))
print(lst)
print(lst1)
print(functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))


def my_generator():
    print("старт генератора")
    i = 1
    while True:
        print("итерция генератора", i)
        i += 1
        yield i ** 2


my_generator2 = (i ** 2 for i in range(100))

for i in my_generator():
    print("в цикле", i)
    if i > 10:
        break