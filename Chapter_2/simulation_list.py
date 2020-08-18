import numpy as np

#模拟链表
if __name__=="__main__":
    data = np.zeros((10,), dtype=int)
    right = np.zeros((10,), dtype=int)
    ind_head = 0
    nums = [2,3,5,8,9,10,18,26,32]
    n = len(nums)
    for i in range(n):
        data[i]=nums[i]
        right[i]=i+1
    right[n-1] = -1

    x = 6
    data[n]=x
    if x<data[0]:
        right[n]=0
        ind_head = n
    else:
        ind = 0
        while right[ind]!=-1:
            if data[right[ind]]>x:
                break
            else:
                ind = right[ind]
        right[n]=right[ind]
        right[ind]=n
    
    i = ind_head
    while i!=-1:
        print(data[i])
        i = right[i]

