






12. two sum













############################
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


# 12 . two sum

# Python program to find if there are 
# two elements wtih given sum 
  
# function to check for the given sum 
# in the array 
def printPairs(arr, arr_size, sum): 
      
    # Create an empty hash set 
    s = set() 
      
    for i in range(0, arr_size): 
        temp = sum-arr[i] 
        if (temp in s): 
            print "Pair with given sum "+ str(sum) + " is (" + str(arr[i]) + ", " + str(temp) + ")"
        s.add(arr[i]) 
  
# driver program to check the above function 
A = [1, 4, 45, 6, 10, 8] 
n = 16
printPairs(A, len(A), n) 
  
    Output:


Pair with given sum 16 is (10, 6)

method 2:
    
    Two-pass Hash Table
To improve our run time complexity, we need a more efficient way to check if the complement exists in the array. 
If the complement exists, we need to look up its index. What is the best way to maintain a mapping of each element
in the array to its index? A hash table.
We reduce the look up time from O(n) to O(1) by trading space for speed. A hash table is built exactly for this purpose,
it supports fast look up in near constant time. I say “near” because if a collision occurred, a look up could degenerate 
to O(n) time. But look up in hash table should be amortized O(1) time as long as the hash function was chosen carefully.
A simple implementation uses two iterations. In the first iteration, we add each element’s value and its index to the table.
Then, in the second iteration we check if each element’s complement (target−nums[i]) exists in the table.
Beware that the complement must not be nums[i]itself!
hash_table={}
for i in range(len(nums)):    # 先做一個hash table
    hash_table[nums[i]]=i
for i in range(len(nums)):
    if target-nums[i] in hash_table:
        if hash_table[target-nums[i]] != i:
            return [i, hash_table[target-nums[i]]]
return []




