l1=[1,2,3,4,5,(6,7,8,9)]
print(l1)
l1[5]=99
print(l1)

l2=(1,2,3,4,5,[6,7,8,9])
print(l2)
#l2[5]=99
#print(l2)
l3=tuple((1,2,3,[4,5,6]))
print(l3)
l4=list((1,2,3,(4,5,6)))
print(l4)
print(len(l4))
l4.remove(3)
print(l4)
l4[1]=100
print(l4)