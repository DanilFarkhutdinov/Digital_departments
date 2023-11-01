class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def multiplication_by_number(self, k):
        self.x *= k
        self.y *= k


v1 = Vector(1, 5)
v2 = Vector(2, 3)
v3 = v1 + v2
v4 = v1 - v2
print(f"вектор v1: ({v1.x}, {v1.y})")
print(f"вектор v2: ({v2.x}, {v2.y})")
print(f"Сумма векторов v1 + v2: ({v3.x}, {v3.y})")
print(f"Разность векторов v1 - v2: ({v4.x}, {v4.y})")
k = 3
v1.multiplication_by_number(k)
print(f"Вектор v1 * {k}: ({v1.x}, {v1.y})")