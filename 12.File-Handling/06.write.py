f = open("append_name.txt","w")

print("Enter a name : ", end ="")

name = input()

f.write(name)

f.close()

f = open("append_name.txt")

print(f.read())

f.close()


