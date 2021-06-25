
'''

Question:

A[0] = -3
A[1] = -2
A[2] = 1
A[3] = 0
A[4] = 8
A[5] = 7
A[6] = 1
A subset containing the points numbered 1, 2, 5 and 6, having coordinates -2, 1, 7 and 1, respectively, is an example of a 3-aligned subset,
since:
• the distance between points numbered 1 and 2 is abs(A[1] - A[2) = 3,
the distances from point number 5 to points numbered 1 and 2 are 9 and 6, respectively,
• the distances from point number 6 to points numbered 1, 2 and 5 are 3,0 and 6, respectively.
and these distances are all divisible by M = 3. The size of this subset is 4 and there is no larger 3-aligned subset.
Write a function:
det solution (A, M)

full question : in gog doc - all int prep


A=[-3,-2,1,0,8,7,1]
M=3
Ans = 4

A=[7,1,11,8,4,10]
M=8
Ans = 1


Solution : My solution is wrong, may be approach is correct
'''


A=[7,1,11,8,4,10]
M=8
#valid_points=set()
valid_points=[]

def findNoOfSubsets(A,M):
    # initialize count as zero.
    cnt = 0;
    n = len(A)
    # iterating to find all the divisible pairs
    for i in range(n - 1) :
        iter=0
        for j in range(i + 1, n) :
            if (abs(A[i] - A[j]) % M == 0) :
                cnt += 1;
                #valid_points.add(A[i])
                #valid_points.add(A[j])
                #adding the i loop element only once
                if iter == 0:
                    valid_points.append(A[i])
                    valid_points.append(A[j])
                    iter+=1
                if iter !=0:
                    valid_points.append(A[j])
                    iter+=1
     
    #print('count : ',cnt); 
    return_val = 1 
    if (len(valid_points)!=0):
        return_val = len(valid_points)
    return return_val
    

size_of_subset = findNoOfSubsets(A,M)
#print("valid points : ",valid_points)
#print("valid points Lenght: ",len(valid_points))
print("Size of largest M-aligned subset : ",size_of_subset)
