def get_matrix(n, m, value):
    matrix = []
    list1 = []

    for i in range(n):
        matrix.insert(i, list1)

    for j in range(m):
        list1.insert(j, value)
    return matrix


result1 = get_matrix(4, 8, 35)
result2 = get_matrix(3, 6, 5)
result3 = get_matrix(2, 2, 3)
print(result1)
print(result2)
print(result3)