#excercise
from math import pi
r=float(input("enter the radius"))
print(pi*r*r)


x=[1,2,3,4]
print(x.sort())

matrix = [[1, 2],[3,4],[5,6],[7,8]]
transposed = []

for i in range(2):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)