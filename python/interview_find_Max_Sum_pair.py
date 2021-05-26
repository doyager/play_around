'''
Find the max sum pair , print both numbers and max sum
'''
x = [3,4,5,6,11,13,9,1,99,50,2,7,8]
n = len(x)
print("Lenght: ",n)
firMax=max(x[0],x[1])
secMax=min(x[0],x[1])
for i in x:
    if i > firMax:
        secMax = firMax
        firMax = i
    elif i > secMax and i != secMax:
        secMax = i

tot = firMax + secMax

print("Max Sum : ",tot)
print("First Max : ",firMax)
print("Second Max : ",secMax)



output:
  Lenght:  13
Max Sum :  149
First Max :  99
Second Max :  50
