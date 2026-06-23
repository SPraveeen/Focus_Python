# find sum of array
## according to the number of elements for loop is iterationg that much -> ***linear time complexity*** -> O(n)

a=[1,2,3,4,5,6]

def get_sum(arr):
    ans=0
    iteration=0
    for i in range(len(a)+1):
        ans+=i
        iteration+=1
        print('iteration',iteration)
    return ans

print(get_sum(a))

## ***constant time complexity O(1)***
# take the first elemet in the list
a=[1,2,3,4,5,6,7]
print(a[0])

a=[1,2,3,4,5,6,6,7,8,8,9]
#still
print(a[0])

## *** Linear search ***
# find target of the element in the array
a=[1,2,3,4,5,6,7,8,9,15,11,12]
target=11
def find_target(arr,t):
    iteration=0
    for i in range(len(arr)+1):
        iteration+=1
        print('iteration',iteration)
        if arr[i]==target:
            return i
        
print(find_target(a,target))

## ***quadratic time complexity*** O(n^2)
## iterations are multipying twice according to the input
# find duplicate transactions
def find_duplicate_transactions(transactions:list[int])->list[tuple[int,int]]:
    duplicates=[]
    iteration=0
    for i in range(len(transactions)):
        for j in range(i+1,len(transactions)):
            iteration+=1
            print('iteration=',iteration)
            if transactions[i]==transactions[j]:
                duplicates.append((i,j))
    return duplicates

transactions=[101,203,101,405,203]
print(find_duplicate_transactions(transactions))

##binarySearch O(logn) -> time complexity
a=[1,3,5,7,8,10,13]
#compare 10 first to mid and find whether it's greate rtahn or lesser, only for *** sorted *** array it will work
def binary_search(a,target):
    left=0
    right=len(a)-1
    iteration=0
    while left <= right:
        mid=(left+right)//2
        iteration+=1
        print('iteration',iteration)
        if a[mid]==target:
            return mid
        elif a[mid]<target:
            left=mid+1
        else:
            right=mid-1

print(binary_search(a,8))


#O(logn)
TRANSACTION=[108,104,103,101,110]
TRANSACTION.sort()
print(TRANSACTION)


#get the largest/maximum value
