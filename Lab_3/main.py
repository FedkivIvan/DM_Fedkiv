from sys import maxsize
from itertools import permutations

path = "file/3.txt"
matrix_size = None

def mass_to_matrix(mass):
    global matrix_size
    matrix_size = int(mass.pop(0))
    matrix = []
    for i in mass:
        matrix.append([int(x) for x in i.split(" ") if x.isdigit()])
    return matrix
def txt_reader(path):
    file = open(path, "r")
    text = file.read()
    mass = text.split("\n")
    return mass_to_matrix(mass)

def travellingSalesmanProblem(matrix, s):
    mtrx = []
    for i in range(matrix_size):
        if i != s:
            mtrx.append(i)
    min_path = maxsize
    next_permutation = permutations(mtrx)

    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += matrix[k][j]
            k = j
        current_pathweight += matrix[k][s]
        min_path = min(min_path, current_pathweight)
    return min_path


if __name__ == '__main__':
    matrix = txt_reader(path)
    s = 0
    res = travellingSalesmanProblem(matrix, s)
    print(f"Min path = {res}")