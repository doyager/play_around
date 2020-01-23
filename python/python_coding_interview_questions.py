
which are divisible by 7 but are not a multiple of 5
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(l)

#1.
factorial of 8
def fact(x):
    if x==0 :
        return 1
    return x*fact(x-1)
x=input()
print(fact(int(x)))


#2.
import math
c=50
h=30
value = []


input_str = input()

print(input_str)


print(l)


#3.
#print 5th fib num-- recursive
def fic(x):
    if x==1 :
        return 0
    if x==2:
        return 1
    return(fic(x-2)+fic(x-1))
x=10
print(fic(int(x)))

#4.
#area of circle
def ac(r):
    aca= 3.14*r*r
    return aca
r = 2
print(ac(r))  


#5.
#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print (list(evenNumbers))

# o/p: [4, 16, 36, 64, 100]


#6 . lambda and map , filter
#even numbers 1-20

li = range(1,21)
print(list(li))

en = map(lambda x: x ,filter(lambda x: x%2==0, li))

print(list(en))

#7.
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

#8.
# print no of letters and digits in the input
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

#9.
#for loop to print squares

abc = range(1,31)

for x in abc :
    print("for", x ,"square is", x**2)
    
    
    
# 11.    
 # Python program to find sum of 
# digits of a number until 
# sum becomes single digit. 
import math  
  
# method to find sum of digits  
# of a number until sum becomes  
# single digit 
def digSum( n): 
    sum = 0
      
    while(n > 0 or sum > 9): 
      
        if(n == 0): 
            n = sum
            sum = 0
          
        sum += n % 10
        n /= 10
      
    return sum
  
# Driver method 
n = 1234
print (digSum(n)) 
