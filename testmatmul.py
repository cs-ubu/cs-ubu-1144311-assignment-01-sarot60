import matmul

A = matmul.readm('A.csv')
b = matmul.readn('b.csv')


for i in matmul.matmul(A,b):
    print(i)