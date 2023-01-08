'''
                                    Problem No:2  --> Combinational Sum with Twist

            Given an array of distinct integers candidates and a target integer target, 
            return a list of all unique combinations of candidates where the chosen numbers sum to target. 
            You may return the combinations in any order.

            The same number may be chosen from candidates an unlimited number of times.
            Two combinations are unique if the frequency of at least one of the chosen numbers is different.
'''
candidates=[int(item) for item in input().split(",")]
#candidates=[2,3,6,7]
target=int(input())
#target = 7

'''
using Backtracking Dfs the above problem is solved.
'''

#res fo storing the list combination
res=[]
def dfs(index,total,container):
    
    #making the bounding Condition
    if(total==target):
        res.append(container.copy())
        return
    
    #if no value is found
    if(total>target or index>=len(candidates)):
        return

    container.append(candidates[index])

    dfs(index,total+candidates[index],container)
    #after reaching bounding condition of no value found removing the last element added
    container.pop()
    #incrementing the index value to get other combination
    dfs(index+1,total,container)

dfs(0,0,[])
print(res)

#output
'''
output = [[2, 2, 3], [7]]
'''