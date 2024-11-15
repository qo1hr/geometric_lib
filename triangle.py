def area(a, b, c):
    ''' 
    //Функция вычисляет площадь треугольника с заданными сторонами
        Пример вызова функции: 
        input: area(3, 3, 3)
        output: 3.89711
    '''
    s = semi_perimeter(a, b, c)
    return math.sqrt(s * (s - a) * (s - b) * (s - c))



def semi_perimeter(a, b, c):
    '''
     //Функция вычисляет полупериметер треугольника с заданными сторонами
        Пример вызова функции: 
        input: area(3, 3, 3)
        output: 4,5//
    '''
    return (a + b + c) / 2


def perimeter(a, b, c):
    '''
     //Функция вычисляет периметер треугольника с заданными сторонами
        Пример вызова функции: 
        input: perimeter(3, 3, 3)
        output: 9//
    '''
    return a + b + c
