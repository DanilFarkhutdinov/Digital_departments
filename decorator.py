def decorator(func):
    def wrapper(*args, **kwargs):
        print("Ввод: ", args, kwargs)
        arg, kwg = func(*args, **kwargs)
        print("Вывод: ", "args ", arg, "kwargs", kwg)
    return wrapper


@decorator
def example_func(*args, **kwargs):
    return args, kwargs

decorator(example_func(1, 2, 3, first="Привет", second="Как дела?"))


