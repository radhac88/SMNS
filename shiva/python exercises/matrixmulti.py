X = [[1,1,1],[2,2,2],[3,3,3]]
Y = [[1,1,1],[2,2,2],[3,3,3]]
result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
	for j in range(len(Y[0])):
		for k in range(len(Y)):
			result[i][j] = X[i][k] + Y[k][j]
for r in result:
	print(r)
