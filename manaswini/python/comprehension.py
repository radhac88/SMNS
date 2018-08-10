#for
h=[]
for l in 'humanhejfj':
	h.append(l)
print(h)
#list
h=[a for a in 'human']
print(h)
#lambda
h=list(map(lambda x:x,'hellooo' ))
print(h)
#if with list
num=[x for x in range(10)if x%2==0]
print(num)
#nested if
num=[y for y in range(30)if y%2==0 if y%5==0]
print(num)
#if else
obj =['even' if i%2==0 else 'odd' for i in range(10)]
print(obj)
#transposed = []
#for i in range(2):
#   transposed_row = []
#   for row in matrix:
#       transposed_row.append(row[i])
#       transposed.append(transposed_row)
#
#print(transposed)
matrix=[[1,2],[3,4],[5,6],[7,8]]
transpose=[[row[i] for row in matrix]for i in range(2)]
print(transpose)
