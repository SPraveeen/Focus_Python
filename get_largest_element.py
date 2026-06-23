arr=[10,30,20,40,60,80,50,70]
a=sorted(arr)
# print(a[-1])
#  but the above time complexity is high

def find_largest_element(arr):
    largest_element=arr[0]
    for i in range(len(arr)):
        if arr[i]>largest_element:
            largest_element=arr[i]
    return largest_element

print(find_largest_element(arr))

def find_largest_element1(arr):
    largest_number=arr[0]
    for i in arr:
        if i > largest_number:
            largest_number=i
    return largest_number

print(find_largest_element1(arr))
