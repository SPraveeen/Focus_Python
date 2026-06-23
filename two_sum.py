# return its index two sum
nums=[1,2,11,15,10,7,20]
target=9

def get_two_sums(nums,target):
    seen={}
    for index,num in enumerate(nums):
        diff=target-num
        if diff in seen:
            return (index,seen[diff])
        else:
            seen[num]=index

print(get_two_sums(nums,target))