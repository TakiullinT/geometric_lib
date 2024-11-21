import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    'circle_perimeter': 1,
    'circle_area': 1,
    'square_perimeter': 1,
    'square_area': 1,
    'triangle_perimeter': 3,
    'triangle_area': 3
}


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    key = f'{fig}_{func}'
    expected_size = sizes.get(key)

    assert expected_size is not None
    assert len(size) == expected_size
    assert all(s >= 0 for s in size)

    if fig == 'triangle':
        a, b, c = size
        assert a + b > c and a + c > b and b + c > a

    result = eval(
        f'{fig}.{func}(*{size})'
    )
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{fig}_{func}", 1):
        size = list(map(int, input(
            "Input figure sizes separated by space, 1 for circle and square\n"
        ).split(' ')))

    calc(fig, func, size)
