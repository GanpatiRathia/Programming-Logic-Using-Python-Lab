import sys

sum = 0
size_args = len(sys.argv)

len_argv = len(sys.argv)

for iterator in range(1,len_argv):
	sum += int(sys.argv[iterator])

print(sum)

