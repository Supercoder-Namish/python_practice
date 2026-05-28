list_1 = [1, 2, 3]
list_2 = [4, 5, 6]


def length(list_1):
    return len(list_1)

def index(idx):
    return list_1[idx]

def concat(list_1, list_2):
    return list_1 + list_2

def append(list_1, list_2):
    list_1.append(list_2)

def reverse(list_1):
    list_1.reverse()

def sort(list_1):
    list_1.sort()

def pop(list_1):
    list_1.pop()

def row(matrix_1):
    return matrix_1[1]

def item(matrix_1):
    return matrix_1[1][2]


Length = length(list_1)
print(Length)

Index = index(2)
print(Index)

concat = concat(list_1, list_2)
print(concat)

append(list_1, list_2)
print(list_1)

reverse(list_1)
print(list_1)

list2 = [1,754,16.5,8951,1590,81.75]
list2.sort(reverse=True)
print(list2)

list_1.pop(2)
print(list_1)

matrix_1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]


row_1 = row(matrix_1)
print(row_1)

item = item(matrix_1)
print(item)


