age = 36

try : 
	txt = "My name is John, I am " + age
	print(txt)
except  :
	print("Can not concatenate string 'My name is John, I am' with integer", age)


age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)


