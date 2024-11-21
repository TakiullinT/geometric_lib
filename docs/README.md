
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# General desription 
This is a simple calculator that calculates the area and perimeter of various figures such as square and circle.

The user enters the figure's name (circle or square), chooses what should be calculated (area or perimeter) and enters figure sizes, exactly radius for circle or one side for square.

The programm uses mathematical formulas for calculations and outputs result on the command line. 

# Functions, descriptions and examples 

## `calculate.py`
### `def calc(fig, func, size):`
- Calculates the value of the chosen function for the entered shape based on its dimensions 
- Example of a call:
```python
>> calc('square', 'perimeter', [5])
20
```
## `triangle.py` 
### `def area(a):`
- Calculates the half-meter of a triangle by entered lengths of the sides. 
- Example of a call: 
```python
>> area(3)
3.0
```
### `def perimeter(a):`
- Calculates the perimeter of a triangle by entered lengths of the sides.
- Example of a call:
```python
>> perimeter(2, 4, 5)
11
``` 
## `square.py`
### `def area(a):`
- Calculates the area of a square by entered length of the side.
- Example of a call:
```python 
>> area(8)
64
``` 
### `def perimeter(a):`
- Calculates the perimeter of a square by entered length of the side.
- Example of a call:
```python
>> perimeter(10)
40
``` 
## `circle.py`
### `def area(a):` 
- Calculates the area of a circle by entered radius 
- Example of a call
```python 
>> area(7)
153.93804002589985
```
### `def perimeter(a):`
- Calculates the perimeter (to be honest, length of a circle) of a circle by entered radius 
- Example of a call
```python 
>> perimeter(10)
62.83185307179586
```
# The history of changes of the project with the hashes of the commits 
1. **d76db2a** - L-04: Add calculate.py. 
   The `calculate.py` file for making calculations was added.
2. **51c40eb** - L-04: Doc updated for triangle. 
   The documentation for working with triangles was updated.
3. **d080c78** - L-04: Triangle added. 
   The `triangle.py` file for making calculations with triangles was added.
4. **d078c8d** - L-03: Docs added.
   The documentations for previous functions was added. 
5. **8ba9aeb** - L-03: Circle and square added. 
   The `circle.py` and `square.py` files for making calculations with circles and squares was added. 
