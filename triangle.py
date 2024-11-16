import math
def area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    ''' 
    //Функция вычисляет площадь треугольника с заданными сторонами
        Пример вызова функции: 
        input: area(3, 3, 3)
        output: 3.89711
    '''
    s = semi_perimeter(a, b, c)
    return math.sqrt(s * (s - a) * (s - b) * (s - c))



def semi_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    '''
     //Функция вычисляет полупериметер треугольника с заданными сторонами
        Пример вызова функции: 
        input: area(3, 3, 3)
        output: 4,5//
    '''
    return (a + b + c) / 2


def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    '''
     //Функция вычисляет периметер треугольника с заданными сторонами
        Пример вызова функции: 
        input: perimeter(3, 3, 3)
        output: 9//
    '''
    return a + b + c
