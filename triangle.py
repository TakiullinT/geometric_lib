def area(a, b, c):
    expected_size = 3
    assert a + b > c and a + c > b and b + c > a
    p = (a + b + c) / 2
    assert len([a, b, c]) == expected_size
    assert all(s >= 0 for s in (a, b, c))
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    assert a + b > c and a + c > b and b + c > a
    return a + b + c
