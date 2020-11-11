from collections import defaultdict


def decorator(func):
    def wrapper(n):
        return lambda: func(n)
    return wrapper


@decorator
def smartdict_nan(key):
    return 10 * key


N = 10

smartdict = {}
for key in range(N):
    val = defaultdict(smartdict_nan(key))
    smartdict[key] = val

# print(key)
# key = 5        #1
# print (smartdict[7]['key_unknown'])       #2

'''
    В изначальной реализации дефолтное значение зависит от конечного
    значения key, потому что формат дефолтной функции smartdict_nan(key).
    Например, если в старой реализации раскомментировать 1 и 2, то
    напечатается 50.
    То есть key ведёт себя как глобальная переменная и
    при изменении key меняется дефолтная функция для всех элементов
    smartdict. В конце цикла key = 9, мы и получаем, что для всех будет
    вызываться smartdict_nan(9) => 90.
    Исправление: добавить обертку, которая вычислит smartdict_nan(key) и
    вернет lambda: <вычисленное значение>
'''
