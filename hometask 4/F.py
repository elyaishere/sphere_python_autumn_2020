# правильные скобочные последовательности
def gen(n, left, right, res):
    if left + right == 2 * n:
        yield res
    if left < n:
        yield from gen(n, left + 1, right, res + '(')
    if left > right:
        yield from gen(n, left, right + 1, res + ')')


def brackets(n):
    yield from gen(n, 0, 0, '')


if __name__ == "__main__":
    n = int(input())
    print(*list(brackets(n)), sep='\n')
