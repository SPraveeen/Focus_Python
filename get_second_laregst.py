arr=[10,30,20,40,60,80,50,70]
a=sorted(arr)
# print(a[-2])
#  but the above time complexity is high

def get_second_largest(arr):
    first_big=1
    second_big=0
    for i in arr:
        if i>first_big:
            second_big=first_big
            first_big=i
        elif i>second_big and i != first_big:
            second_big=i
    return first_big,second_big

print(get_second_largest(arr))