import re
from functools import reduce
from operator import setitem

# ['12', '25.6', '84,02', '  69-91'] -> [21, 652, 2048, 1996]
def solution1(arg):
    res = list(map(lambda x: int(re.sub(r"\D", "", x)[::-1]), arg))
    return res

# zip(range(2, 5), range(3, 9, 2)) -> [6, 15, 28]
def solution2(arg):
    res = list(map(lambda x: x[0] * x[1], arg))
    return res

# range(20) -> [0, 2, 5, 6, 8, 11, 12, 14, 17, 18]
def solution3(arg):
    res = list(filter(lambda x: x % 6 == 0 or x % 6 == 2 or x % 6 == 5, arg))
    return res

# ['', 25, None, 'python', 0.0, [], ('msu', '1755-01-25')] -> [25, 'python', ('msu', '1755-01-25')]
def solution4(arg):
    res = list(filter(bool, arg))
    return res

# rooms = [
#     {"name": "комната1", "width": 2, "length": 4},
#     {"name": "комната2", "width": 2.5, "length": 5.6},
#     {"name": "кухня", "width": 3.5, "length": 4},
#    {"name": "туалет", "width": 1.5, "length": 1.5},
# ] (Добавьте к каждому элементу списка rooms поле square, показывающее площадь комнаты. Элементы списка rooms ДОЛЖНЫ обновиться!)
def solution5(arg):
    list(map(lambda x: setitem(x, "square", x["width"] * x["length"]), arg))
    return arg

# Добавьте к каждому элементу списка rooms поле square, показывающее площадь комнаты.
# Элементы исходного списка rooms НЕ ДОЛЖНЫ обновиться! Порядок элементов в результирующем списке должен совпадать с порядком в исходном списке.
def solution6(arg):
    res = list(map(lambda x: dict(x, square=x["width"] * x["length"]), arg))
    return res

# [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}, {3, 4, 5, 6, 7}] -> {3, 4, 5} (Найдите пересечение всех множеств. Используйте функцию reduce.)
def solution7(arg):
    res = set(reduce(lambda x, y: x & y, arg))
    return res

# [1, 2, 1, 1, 3, 2, 3, 2, 4, 2, 4] -> {1: 3, 2: 4, 3: 2, 4: 2} (Посчитайте, сколько раз встречается каждый элемент в списке.)
def solution8(arg):
    res = reduce(lambda d, x: setitem(d, x, d.pop(x, 0) + 1) or d, arg, {})
    return res

# students = [
#     {'name': 'Alina', 'gpa': 4.57},
#     {'name': 'Sergey', 'gpa': 5.0},
#     {'name': 'Nastya', 'gpa': 4.21},
#     {'name': 'Valya', 'gpa': 4.72},
#     {'name': 'Anton', 'gpa': 4.32},
# ] 
# (Выведите имена студентов, чей GPA > 4.5.)
# students -> ['Alina', 'Sergey', 'Valya']
def solution9(arg):
    res = list(map(lambda x: x['name'], list(filter(lambda x: x['gpa'] > 4.5, arg))))
    return res

# ['165033', '477329', '631811', '478117', '475145', '238018', '917764', '394286'] -> ['165033', '475145', '238018']
# Билетик называется счастливым, если сумма цифр на четных местах равна сумме цифр на нечетных. Из исходного списка выведите только счастливые билетики.
def solution10(arg):
    res = list(filter(lambda z: reduce(lambda x, y: int(x) + int(y), z[::2]) ==
                      reduce(lambda x, y: int(x) + int(y), z[1::2]), arg))
    return res


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
