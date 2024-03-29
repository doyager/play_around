################################################################################################
# write a function to check brackets or parentheses
# OR brackets in string are correctly matched 

#Solution-2 : for only one type of parenthesis 
def check(myStr):
    stack = []
    for i in myStr:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if ((len(stack) > 0)):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
 
#If the question has more than one type of parenthesis
# Function to check parentheses
def check(myStr):
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
             # Here we are checking if we encountered the correct closing bracket, 
             # so we check the corresponding open bracket is the last one in the list by checking the current last element in the list
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):   
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

# Driver code
string = "{[]{()}}"
print(string,"-", check(string))
  
string = "[{}{})(]"
print(string,"-", check(string))
  
string = "((()"
print(string,"-",check(string))

o/p:
{[]{()}} - Balanced
[{}{})(] - Unbalanced
((() - Unbalanced
    
################################################################################################
# write a fucntion to return reverse of number , should be able to handle negative number
def rev_fun(x):
    sign=0
    reversed_num = 0
    if(x>0):
        sign=1
    else:
        sign=-1
        x=x*sign
        
    while x !=0:
        tmp = x % 10
        reversed_num = reversed_num * 10 + tmp
        x //= 10
    #print(reversed_num*sign)
    return reversed_num*sign

print(rev_fun(-456))
o/p:
 -654
 
######
Given a two dimensional list, for example [ [2,3],[3,4],[5]] person 2 is friends with 3 etc, find how many friends each person has. Note, one person has no friends
Can you do the following without using subquery?: {1,None,1,2,None} --> [1,1,1,2,2] Ensure you take care of case input[None] which means None object
Complete a function that returns a list containing all the mismatched words (case sensitive) between two given input strings # For example: # - string 1 : "Firstly this is the first string" # - string 2 : "Next is the second string" # # - output : ['Firstly', 'this', 'first', 'Next', 'second']
Complete a function that returns the number of times a given character occurs in the given string.
# For example:
# - input string = "mississippi"
# - char = "s"
#
# - output : 4

Given an array containing None values fill in the None values with most recent non None value in the array. For example:input array: [1,None,2,3,None,None,5,None] # - output array: [1,1,2,3,3,3,5,5]
Complete a function that returns a list containing all the mismatched words (case sensitive) between two given input strings # For example: string 1 : "Firstly this is the first string" # - string 2 : "Next is the second string" # # - output : ['Firstly', 'this', 'first', 'Next', 'second']
Given an array of integers, we would like to determine whether the array is monotonic (non-decreasing/non-increasing) or not. Examples:
 // 1 2 5 5 8 
// true 
// 9 4 4 2 2 
// true 
// 1 4 6 3 
// false  
//1 1 1 1 1 1
// true
Given two sentences, construct an array that has the words that appear in one sentence and not the other
Given an ip address as an input string, validate it and return True/False
Count the neighbors of each node in a graph. Input graph is a multi dimensional list
Given a dictionary, print the key for nth highest value present in the dict. If there are more than 1 record present for nth highest value then sort the key and print the first one
Flatten a nested dictionary
You have a 2-D array of friends like [[A,B],[A,C],[B,D],[B,C],[R,M], [S],[P], [A]]. Write a function that creates a dictionary of how many friends each person has. People can have 0 to many friends. However, there won't be repeat relationships like [A,B] and [B,A] and neither will there be more than 2 people in a relationship
What is a loop that goes on forever?
Recursively parse a string for a pattern that can be either 1 or 2 characters long
Write a simple spell-checking engine
Given two sentences, you have to print the words those are not present in either of the sentences.(If one word is present twice in 1st sentence but not present in 2nd sentence then you have to print that word too)



#########################
# 1.  Given a two dimensional list, for example [ [2,3],[3,4],[5],[2,3],[3,7],[3,6]]
# person 2 is friends with 3 etc, find how many friends each person has. Note, one person has no friends


## caculate the number of unique frineds for each and print the count for each name(number)
## assumption input will be LIST of LISTs, where inside list will be either 1 0r 2 number
## [5] : means 5 has no friend in this tuple 
## [3,4] : means 3 & 4 are friends
#frnds_dict = {}
# import defaultdict module

from collections import defaultdict
b =  [ [2,3],[3,4],[5],[2,3],[3,7],[3,6]]
# create an empty set of dictionary
frnds_dict = defaultdict(set)
for row in b:
    if len(row) ==2:
        if row[0] not in frnds_dict.keys():
            frnds_dict[row[0]] = set()
        if row[1] not in frnds_dict.keys():
            frnds_dict[row[1]] = set()
        
            frnds_dict[row[0]].add(row[1])
            frnds_dict[row[1]].add(row[0])
    elif len(row) ==1:
        if row[0] not in frnds_dict.keys():
            frnds_dict[row[0]] = set()
        
        
print(frnds_dict)
        #if row[0] in frnds_dict.keys():
        #frnds_dict[row[0]].append(ele)
        #else:
     
print("Friends count : ")

for key, value in frnds_dict.items():
    cnt = len(value)
    print(f"{key} -  {cnt}")
    
o/p:
defaultdict(<class 'set'>, {2: {3}, 3: {2, 4, 6, 7}, 4: {3}, 5: set(), 7: {3}, 6: {3}})
Friends count : 
2 -  1
3 -  4
4 -  1
5 -  0
7 -  1
6 -  1

#################
