import numpy as np
from bubble_sort import bubble_sort
from quick_sort import quick_sort


#去重+排序问题
#解法一：先去重，后排序（桶排序）
#解法二：先排序，后去重（常规排序算法）


def bucket_uniquesort(m, nums, sort="ascend"):
    assert(sort=="ascend" or sort=="descend")
    book = np.zeros((m,), dtype=int)
    n=len(nums)
    for i in range(n):
        book[nums[i]]=1
    
    sorted_nums = np.zeros((n,), dtype=int)
    t = 0
    if sort=="ascend":
        for i in range(m):
            if book[i]>0:
                sorted_nums[t]=i
                t+=1
    else:
        for i in range(m-1,-1,-1):
            if book[i]>0:
                sorted_nums[t]=i
                t+=1
    nums_unique_sort = np.zeros((t,), dtype=int)
    for j in range(t):
        nums_unique_sort[j]=sorted_nums[j]
    return nums_unique_sort


def sort_unique(nums, sort="ascend"):
    nums_copy = nums.copy()
    bubble_sort(nums_copy,sort)
    n = len(nums_copy)
    j = 1
    i = 0
    while j<n:
        if nums_copy[j]!=nums_copy[i]:
            nums_copy[i+1]=nums_copy[j]
            i+=1
        j+=1
    nums_unique_sort = np.zeros((i+1,), dtype=int)
    for j in range(i+1):
        nums_unique_sort[j]=nums_copy[j]
    return nums_unique_sort


if __name__=="__main__":
    nums = [20,40,32,67,40,20,89,300,400,15]
    print("原列表：", nums)
    sorted_nums = bucket_uniquesort(1001, nums)
    print("先去重后排序的列表：", sorted_nums)
    nums_unique_sort = sort_unique(nums)
    
    print("先排序后去重的列表：", nums_unique_sort)
