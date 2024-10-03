import math


def area(r):
    '''
     //Функция вычисляет площадь окружности с заданным радиусом
        Пример вызова функции: 
        input: area(3)
        output: 28,27433//
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    //Функция вычисляет периметр(длину) окружности с заданным радиусом
        Пример вызова функции:
        input: preimeter(3)
        output: 18,84956//
    '''
    return 2 * math.pi * r

