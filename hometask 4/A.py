# 'python' -> ['pppp', 'yyyy', 'tttt', 'hhhh', 'oooo', 'nnnn']
def solution1(arg):
    res = [arg[i]*4 for i in range(len(arg))]
    return res

# 'python' -> ['p', 'yy', 'ttt', 'hhhh', 'ooooo', 'nnnnnn']
def solution2(arg):
    res = [arg[i]*(i + 1) for i in range(len(arg))]
    return res

# range(16) -> [0, 3, 5, 6, 9, 10, 12, 15]
def solution3(arg):
    res = [i for i in arg if i % 3 == 0 or i % 5 == 0]
    return res

# [[1, 2, 3], [4, 5, 6, 7], [8, 9], [0]] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def solution4(arg):
    res = [j for i in arg for j in i]
    return res

# 15 -> [(3, 4, 5), (5, 12, 13), (6, 8, 10), (9, 12, 15)] (Пифагоровы тройки.)
def solution5(arg):
    res = [(a, b, int((a**2 + b**2)**0.5)) for a in range(1, arg) for b in range(a, arg)
           if a**2 + b**2 <= arg**2 and (a**2 + b**2)**0.5 - int((a**2 + b**2)**0.5) == 0.]
    return res

# ([0, 1, 2], [0, 1, 2, 3, 4]) -> [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
def solution6(arg):
    res = [[arg[0][i] + arg[1][j] for j in range(len(arg[1]))] for i in range(len(arg[0]))]
    return res

# [[1, 2], [3, 4], [5, 6]] -> [[1, 3, 5], [2, 4, 6]]
# [[1, 3, 5], [2, 4, 6]] -> [[1, 2], [3, 4], [5, 6]] (Транспонирование матрицы.)
def solution7(arg):
    res = [[arg[j][i] for j in range(len(arg))] for i in range(len(arg[0]))]
    return res

# ["0", "1 2 3", "4 5 6 7", "8 9"] -> [[0], [1, 2, 3], [4, 5, 6, 7], [8, 9]]
def solution8(arg):
    res = [[int(c) for c in arg[i].split()] for i in range(len(arg))]
    return res

# range(0, 7) -> {'a': 0, 'b': 1, 'c': 4, 'd': 9, 'e': 16, 'f': 25, 'g': 36}
def solution9(arg):
    res = {chr(ord('a') + i): i**2 for i in arg}
    return res

# ['Alice', 'vova', 'ANTON', 'Bob', 'kAMILA', 'CJ', 'ALICE', 'Nastya'] -> {'Alice', 'Anton', 'Kamila', 'Nastya', 'Vova'}
def solution10(arg):
    res = {chr(ord('A') - ord('a') + ord(i[0])) + i[1:] for i in set([j.lower() for j in arg if len(j) > 3])}
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
