def area(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return 0
    assert a + b > c and a + c > b and b + c > a
    assert all(s >= 0 for s in (a, b, c))
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Стороны не могут образовать треугольник")
    return a + b + c
