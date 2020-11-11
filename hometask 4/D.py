# декоратор @counter, который считает глубину рекурсии функции и количество рекурсивных вызовов функции
import functools


def counter(func):
    counter.rdepth = 0
    counter.mdepth = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if counter.rdepth == 0:
            counter.mdepth = 0
            wrapper.ncalls = 0
        wrapper.ncalls += 1
        counter.rdepth += 1
        if counter.rdepth > counter.mdepth:
            counter.mdepth = counter.rdepth
        wrapper.rdepth = counter.mdepth
        result = func(*args, **kwargs)
        counter.rdepth -= 1
        return result
    wrapper.ncalls = 0
    wrapper.rdepth = 0
    return wrapper
