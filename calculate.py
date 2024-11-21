import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
    '''
    
    Вычисляет значение заданной функции для данной фигуры на основе её размеров. 
    
    Параметры: 
    fig (str): название фигуры (должно быть 'circle' или 'square')
    func (str): название функции (должно быть 'perimeter' или 'area')
    size (list): список размеров фигуры. Для ввода ожидается одно значение (Для круга - радиус, для квадрата - длина стороны). 
    
    Возвращаемое значение: 
    (float): Результат вычисления функции для данной фигуры. 
    
    Пример вызова: 
    >> calc('circle', 'area', [11])
    area of circle is 380.132711084365
    
    >> calc('square', 'perimeter', [5])
    perimeter of square is 20
    
    '''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



