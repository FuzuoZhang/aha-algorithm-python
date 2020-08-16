import numpy as np

def quick_sort(nums, left, right):
    #升序
    if right<=left:
        return

    temp = nums[left]
    i=left
    j=right
    while i<j:
        while i<j and nums[j]>=temp:
            j-=1
        while i<j and nums[i]<=temp:
            i+=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[left]=nums[i]
    nums[i]=temp
    quick_sort(nums,left,i-1)
    quick_sort(nums,i+1,right)
    return

if __name__=="__main__":
    nums = [6,1,2,7,9,3,4,5,10,8]
    print("原列表：", nums)
    quick_sort(nums,0,len(nums)-1)
    print("升序排序后的列表：", nums)