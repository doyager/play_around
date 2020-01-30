
"""
Contents:
1. Lambda function
2. Map
3. Filter
4. Reduce
5. List comprehension

"""

#########################################################################


##### Lambda function
- a simple 1-line function , borrowed from functional programming
- These are implicit , dont use def or return keywords

Eg:

ex 1:
"""  Double the value"""
#traditional
def doubleValue(x):
  return x*2

#lamda , with one variable
lamda x: 2*x 

ex 2:
""" add two numbers"""
def add(x,y)
  return x+y
  
lamda x,y:x+y

ex 3:

""" find max of two numbers"""

def maxOfTwo(x,y):
  if x>y:
    return x
  else :
    return y
 
 print(maxOfTwo(4,5))
 
 
 mx = lamda x,y : x if x > y else y .  # we are asssigng the fucntion to variable mx , if x >y we return x , else if y
 print (mx(8,5)) // calling lamda fucntion


#########################################################################


##### Map

- apply same function to each element of a sequence
- return the modified list

List[m,n,p]          ----> .  MAP --------> .   returns new list , [f(m),f(n),f(p)]
Function, f()


eg:

""" Square of numbers in list """

## using map and lamda
# map function is going to apply the lamda function to all elements in list n , returns a list and prints it
n = [ 2,3,4,5]
print(List(map(lamda x : x*x, n  ))) .  

or


## using standard
lst = [2,3,4,5]

def square(lst1):
lst2 = []
  for num in lst1:
     lst2.append(num **2)
  return lst2
  
print(square([2,3,4]))



#########################################################################


##### Filter

- filter items out of a sequence
- return filtered list

List, [a,b,c],
Condition               ----------> FILTER .  ---------> New list , [a,c]
                                (if m==condition)
                                
 
 
 lst = [1,2,3,4]
 #lamda and filter

 print(list(filter(lambda x : x > 2, lst)))
 # here lst is the list with values , we are using lamda function, receives variable x and  to do filter greater than x>2
 # filter will apply this lambda function to each item in lst varialbe , and we have to explicity cast it to LIST
 
 
 # traditional python implementation
 def ovr_two(lst1):
  lst2 = [ x for x in lst1 if x>2]
  return lst2
  
  print(ovr_two(lst))
  
  





#########################################################################


##### Reduce

- applies same operation to items of a sequence
- uses result of operation as first param to next operation
- return an item , not a list

List ,[a,b,c]           ------>  REDUCE ------> f(f(a,b),c)
Function , f()


n = [ 1,2,3,4]
print (reduce(lamda x,y: x*y, n ))
# this will apply reduce on the list n, for which lamda fucntio is applied to every two elements of list n,
# and then to the result of 1st two elements & thrid element

i.e.

1*2 = 2
2 * 3 = 6
6 * 4 = 24

# traditional python function
# above reduce implementation using for loop
def mult(list1):
  product = list[0]
  for i in range(1,len(list1)):
     product *= list1[1]
  return product
  
print(mult([1,2,3,4))
# o/p : 24





#########################################################################


##### List comprehension
            
            
 #List is collection of data , surrounded by squre brackets and separated by comma           
List : [ 1,2,"a",3.14]


 #Basic Form 
            #[ expr  for val in collection]
            
            #[ expr for val in collection if <test>] . // only one condition
            
            #[ expr for val in collection if <test>] .   //mulitple conditions
            
            #[ expr for val1 in collection1  and val2 in collection2]





#########################################################################


##### 





#########################################################################


##### 







#########################################################################


##### 







#########################################################################


##### 




#########################################################################


##### 










#########################################################################


##### 






#########################################################################


##### 
 
 
 
 
 
 
 


