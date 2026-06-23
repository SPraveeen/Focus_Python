# find first non-repeating value

nums=[2,3,4,2,3,5]

# answer is 4 

def first_non_repeating(nums):
    emp_lis={}
    for i in nums:
        emp_lis[i]=emp_lis.get(i,0)+1
    
    for i in nums:
        if emp_lis[i]==1:
            return i

print(first_non_repeating(nums))