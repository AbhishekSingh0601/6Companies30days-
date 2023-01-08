'''
    You are given an integer array nums of length n. Return maximum length of Rotation Function.
'''
nums=[4,3,2,6]
list_sum=sum(nums)
n=len(nums)
res=sum(i*n for i,n in enumerate(nums))
 
total=res
for i in range(n):
    total+=n*nums[i] - list_sum
            
          
    res=max(total,res)
print(res)