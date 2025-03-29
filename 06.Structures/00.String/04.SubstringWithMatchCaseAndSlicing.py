


statement = input("Enter a statement : ")

statement_length = len(statement)

print("Length of the statement is : ", statement_length, end = "\n\n")

# stamement = "This is a string"
# len(statement) #16
for i in range(statement_length): # 0 ....15
	 #1 -> 1st
	 #2 -> 2nd
	 #3 -> 3rd
	 #else -> 4th, 5th ....
	match i+1 % 10 : #for 0th character i+1 % 10 = 1
		case 1 :
			print("{}st Character of {} is {}".format( i+1, statement, statement[i]) )

		case 2 : # i=1
			print("{}nd Character of {} is {}".format( i+1, statement, statement[i]) )

		case 3 : # i=2
			print("{}rd Character of {} is {}".format( i+1, statement, statement[i]) )

		case _ : # else
			print("{}th Character of {} is {}".format( i+1, statement, statement[i]) )

#statement = This is a string
b = statement[2:4] #is

print("\"" + statement + "\"" + "[2:4] is :" + b)

print("\nSubstring of Hello:\n")
print("\"Hello\"[0]","Hello"[0], end = "\n\n")
print("\"Hello\"[:]","Hello"[:], end = "\n\n")
print("\"Hello\"[:5]","Hello"[:5], end = "\n\n")
print("\"Hello\"[2:]","Hello"[2:], end = "\n\n")
print("\"Hello\"[:3]","Hello"[:3], end = "\n\n")
print("\"Hello\"[1:2]","Hello"[1:2], end = "\n\n")


