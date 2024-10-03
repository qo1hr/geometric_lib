
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

# General description of the solution
## `calculate.py`
### 'def calc(fig, func, size):'
 - This file calculates the value of a function based on the choice of shape (square or circle), the operation to be calculated (perimeter or area) and its size
 - Let me give you an example of a function call:
`python`
input: calc("square", "perimeter", 3)
output: 12
input: calc("circle", "area", 3)
output: 28,27433
## `square.py`
### def area(a):
- This function calculates the area of a square based on a user-specified side
- Let me give you an example of a function call:
`python`
input: area(3)
output: 9
### def perimeter(a):
- This function calculates the perimeter of a square based on a user-specified side
- Let me give you an example of a function call:
`python`
input: perimeter(3)
output: 12
## `triangle.py`
### def area(a, b, c):
- This function calculates the semi-perimeter of a triangle based on user-specified sides
- Let me give you an example of a function call:
`python`
input: area(3, 3, 3)
output: 4.5
### def perimeter(a, b, c):
- This function calculates the perimeter of a triangle based on user-specified sides
- Let me give you an example of a function call:
`python`
input: perimeter(3, 3, 3)
output: 9
## `circle.py`
### def area(a):
- This function calculates the area of a circle with a user-specified radius 
- Let me give you an example of a function call:
`python`
input: area(3)
output: 28,27433
### def perimeter(r):
- This function calculates the perimeter (length) of a circle with a user-specified radius
- Let me give you an example of a function call:
`python`
input: perimeter(3)
output: 18,84956


# Project change history with commit hashes

1. ***d76db2a*** L-04: Add calculate.py
Adding a 'calculate.py' file to perform calculations

2. ***51c40eb*** L-04: Doc updated for triangle
Updated the documentation to work with the triangle

3. ***d080c78*** L-04: Triangle added
Added functionality for working with triangles

4. ***d078c8d*** (origin/main, origin/HEAD, main) L-03: Docs added
Added functionality to work with previous functions

5. ***8ba9aeb*** L-03: Circle and square added
Added functionality for working with circles and squares