def area(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return 0
    assert a + b > c and a + c > b and b + c > a
    assert all(s >= 0 for s in (a, b, c))
    expected_size = 3
    assert len([a, b, c]) == expected_size
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    return a + b + c
