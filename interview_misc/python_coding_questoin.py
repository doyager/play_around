


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
# 1.  Given a two dimensional list, for example [ [2,3],[3,4],[5]] 
# person 2 is friends with 3 etc, find how many friends each person has. Note, one person has no friends


#frnds_dict = {}
# import defaultdict module
from collections import defaultdict
  
# create an empty set of dictionary
frnds_dict = defaultdict(set)
for row in b:
    if row[0] not in frnds_dict.keys():
        frnds_dict[row[0]] = set()
    for ele in row[1:] :
        frnds_dict[row[0]].add(ele)
        
        
print(frnds_dict)
        #if row[0] in frnds_dict.keys():
        #frnds_dict[row[0]].append(ele)
        #else:
     
print("Friends count : ")

for key, value in frnds_dict.items():
    cnt = len(value)
    print(f"{key} -  {cnt}")
    
o/p:
defaultdict(<class 'set'>, {2: {3}, 3: {4}, 5: set()})
Friends count : 
2 -  1
3 -  1
5 -  0

#################
