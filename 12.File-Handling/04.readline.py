f = open("name.txt", "r")

for iter in range(1,10,1):
	
	print(f"line no. {iter}")
	print(f.readline())

f.close()
