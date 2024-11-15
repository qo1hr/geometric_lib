import circle
import square

# Доступные фигуры и операции
figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
    ''' 
    Функция вычисляет значение заданной фигуры
    Параметры:
        fig (str): Название фигуры ("circle" или "square")
        func (str): Название функции ("perimeter" или "area")
        size (list): Размер фигуры (для круга - радиус, для квадрата - сторона)
    
    Возвращает:
        float: Результат вычисления (периметр или площадь фигуры)
    
    Примеры:
        calc("square", "perimeter", [3])  # Возвращает 12
        calc("circle", "area", [3])       # Возвращает 28.27433
    '''
    # Проверка, что фигура и операция корректны
    assert fig in figs, f"Фигура '{fig}' не поддерживается. Доступные фигуры: {figs}"
    assert func in funcs, f"Функция '{func}' не поддерживается. Доступные функции: {funcs}"

    # Вычисление результата на основе фигуры и операции
    result = eval(f'{fig}.{func}(*{size})')
    return result

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()
    
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Enter size:\n").split(' ')))
    
    result = calc(fig, func, size)
    print(f"{func} of {fig} is {result}")