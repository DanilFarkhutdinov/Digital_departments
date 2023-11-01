import random

dct = {"a": 1}

# try:
#     print(dct['b'])
# except KeyError as e:
#     print("Ошибка", e)


class AppException(Exception):
    pass


class MyException(AppException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def my_func():
    if random.random() > 0.5:
        raise MyException("test")


for i in range(10):
    try:
        my_func()
    except MyException:
        ...  # 1 specific app exception
    except AppException:
        ...  # 2 other app exceptions
    except BaseException:
        ...  # 3 python exceptions
