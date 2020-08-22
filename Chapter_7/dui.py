import numpy as np

def siftup(nums,i):
    while i>0:
        if nums[(i-1)//2]<nums[i]:
            nums[(i-1)//2],nums[i]=nums[i],nums[(i-1)//2]
            i=(i-1)//2
        else:
            break
    return 


def siftdown(nums,i,n):
    #大顶堆下滤
    while i<=n//2-1:
        if nums[i*2+1]>nums[i]:
            t=i*2+1
        else:
            t=i
        if i*2+2<n:
            if nums[2*i+2]>nums[t]:
                t=i*2+2
        if t==i:
            break
        else:
            nums[t],nums[i]=nums[i],nums[t]
            i=t
    return 

def siftdown_small(nums,i,n):
    #小顶堆下滤
    while i<=n//2-1:
        if nums[i*2+1]<nums[i]:
            t=i*2+1
        else:
            t=i
        if i*2+2<n:
            if nums[2*i+2]<nums[t]:
                t=i*2+2
        if t==i:
            break
        else:
            nums[t],nums[i]=nums[i],nums[t]
            i=t
    return 


def create_pile(nums, method=1):
    #method=1:整体下滤
    #method=2:每次新插入一个点，上滤
    n=len(nums)
    if method==1:
        start=n//2-1
        for i in range(start,-1,-1):
            siftdown(nums,i,n)
    if method==2:
        for i in range(1,n):
            siftup(nums,i)
    

def pile_sort(nums):
    create_pile(nums,method=2)
    print(nums)
    n=len(nums)
    for i in range(n-1,0,-1):
        nums[0],nums[i]=nums[i],nums[0]
        siftdown(nums,0,i)

def first_K_largest(nums,K):
    ls = nums.copy()
    n=len(ls)
    #用前K个数建立小顶堆
    start=K//2-1
    for i in range(start,-1,-1):
        siftdown_small(ls,i,K)
    for i in range(K,n):
        if ls[i]<ls[0]:
            continue
        else:
            ls[0]=ls[i]
            siftdown_small(ls,0,K)
    return ls


if __name__=="__main__":
    #堆排序
    nums=[99,5,36,7,22,17,46,12,2,19,25,28,1,92]
    pile_sort(nums)
    print("堆排序结果：", nums)

    #求第K大的数
    nums=[99,5,36,7,22,17,46,12,2,19,25,28,1,92]
    K=5
    ls = first_K_largest(nums,K)
    print("nums中第%d大的数为: %d" %(K,ls[0]))
    print("nums最大的前%d个数为: " %K, end="")
    for i in range(K):
        print("%d " %ls[i], end="")