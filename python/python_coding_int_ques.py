which are divisible by 7 but are not a multiple of 5
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(l)


factorial of 8
def fact(x):
    if x==0 :
        return 1
    return x*fact(x-1)
x=input()
print(fact(int(x)))


import math
c=50
h=30
value = []


input_str = input()

print(input_str)


print(l)

#print 5th fib num-- recursive
def fic(x):
    if x==1 :
        return 0
    if x==2:
        return 1
    return(fic(x-2)+fic(x-1))
x=10
print(fic(int(x)))

#area of circle
def ac(r):
    aca= 3.14*r*r
    return aca
r = 2
print(ac(r))  


#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print (list(evenNumbers))

# o/p: [4, 16, 36, 64, 100]

#even numbers 1-20

li = range(1,21)
print(list(li))

en = map(lambda x: x ,filter(lambda x: x%2==0, li))

print(list(en))


#define a dic with 1st 5 numbers n its sqrs-- dict is key value pairs

abc= {1:1,2:4}

#print keys -1,2

for key in abc:
    print(key)
   
#print values
   
for value in abc.values():
    print(value)
   
for k,value in abc.items():
    print("key ",k,"value ",value,"sum ", k+value)
   
x= input()

s = raw_input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]

#for loop to print squares

abc = range(1,31)

for x in abc :
    print("for", x ,"square is", x**2)
