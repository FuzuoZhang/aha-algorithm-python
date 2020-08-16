import numpy as np


def bucket_sort(m, nums, sort="ascend"):  
    #sort="ascend"，升序；sort="descend"，降序
    #桶的范围为0~m-1
    assert(sort=="ascend" or sort=="descend")
    book = np.zeros((m,), dtype=int)
    n = len(nums)
    for i in range(n):
        book[nums[i]]+=1
    
    sorted_nums = np.zeros((n,), dtype=int)
    t = 0
    if sort=="descend":
        for i in range(m-1,-1,-1):
            if book[i]>0:
                sorted_nums[t:t+book[i]] = i
                t = t+book[i]
    else:
        for i in range(m):
            if book[i]>0:
                sorted_nums[t:t+book[i]]=i
                t+=book[i]

    return sorted_nums


if __name__ == "__main__":
    nums = [5,3,5,2,8]
    print("原列表：", nums)
    sorted_nums = bucket_sort(11, nums)
    print("升序排序后的列表：", sorted_nums)

    print()
    nums = [8, 100, 50,22,15,6,1,1000, 999, 0]
    print("原列表：", nums)
    sorted_nums = bucket_sort(1001, nums,"descend")
    print("降序排序后的列表：", sorted_nums)