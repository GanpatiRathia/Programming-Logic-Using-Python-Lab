


statement = input("Enter a statement : ")

statement_length = len(statement)

print("Length of the statement is : ", statement_length, end = "\n\n")

for i in range(statement_length):
	
	match i+1 % 10 :
		case 1 :
			print("{}st Character of {} is {}".format( i+1, statement, statement[i]) )
	
		case 2 :
			print("{}nd Character of {} is {}".format( i+1, statement, statement[i]) )

		case 3 :
			print("{}rd Character of {} is {}".format( i+1, statement, statement[i]) )

		case _ :
			print("{}th Character of {} is {}".format( i+1, statement, statement[i]) )

b = statement[2:4]

print("\"" + statement + "\"" + "[2:3] is :" + b)

print("\nSubstring of Hello:\n")
print("\"Hello\"[0]","Hello"[0], end = "\n\n")
print("\"Hello\"[:]","Hello"[:], end = "\n\n")
print("\"Hello\"[:5]","Hello"[:5], end = "\n\n")
print("\"Hello\"[2:]","Hello"[2:], end = "\n\n")
print("\"Hello\"[:3]","Hello"[:3], end = "\n\n")
print("\"Hello\"[1:2]","Hello"[1:2], end = "\n\n")


