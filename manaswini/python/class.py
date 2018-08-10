class person:
  def __init__(self,name,age,group):
    self.name=name
    self.age=age
    self.group=group
#p1=person("harleen",21,"a")
#print(p1.name)
  def fun(abc):   #or   #def fun(self):
  	print(abc.age)      #print(self.age)

p2=person("riya",20,"b")
p2.fun()
p2.age=30
print(p2.age)