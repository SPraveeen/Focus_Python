nums=[1,2,3,2,4,5,1]


def find_duplicates(nums):
    seen1=set()
    dups=set()
    for i in nums:
        if i in seen1:
            dups.add(i)
        else:
            seen1.add(i)
    return(dups)

print(find_duplicates(nums))
