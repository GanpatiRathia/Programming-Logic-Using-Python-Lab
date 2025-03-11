n=list(map(int,input('enter a number = ').split()))
even=[]
odd=[]
for val in n:
    if val%2==0:
        even=even+[val]
    else:
            odd=odd+[val]
print(even)
print(odd)
