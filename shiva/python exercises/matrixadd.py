X = [[1,1,1],[2,2,2],[3,3,3]]
Y = [[1,1,1],[2,2,2],[3,3,3]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(X)):
	for j in range(len(X[0])):
		result[i][j] = X[i][j] + Y[i][j]

for k in result:
	print(k)