
# The dir() function is used to list all attributes and methods 
# of an object, module, class, or variable.


class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))

l1=[1,2]
l2=(1,2)
l3={1,2}
l4={"f1":"Ram","f2":"Rajya"}

print(dir(l1))
print(dir(l2))
print(dir(l3))
print(dir(l4))
