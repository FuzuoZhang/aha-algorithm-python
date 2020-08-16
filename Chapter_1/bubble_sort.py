import numpy as np


def bubble_sort(nums, sort="ascend"):
    #冒泡排序
    assert(sort=="ascend" or sort=="descend")
    n = len(nums)
    for i in range(n-1):
        mark = 0
        for j in range(n-1-i):
            if sort=="ascend":
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    mark=1
            else:
                if nums[j]<nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    mark=1
        if mark==0:
            break
    return 


class item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

def item_bubble_sort(items, sort="ascend"):
    assert(sort=="ascend" or sort=="descend")
    n = len(items)
    for i in range(n-1):
        mark = 0
        for j in range(n-1-i):
            if sort=="ascend":
                if items[j].value>items[j+1].value:
                    items[j],items[j+1] = items[j+1],items[j]
                    mark=1
            else:
                if items[j].value<items[j+1].value:
                    items[j],items[j+1] = items[j+1],items[j]
                    mark=1
        if mark==0:
            break
    return

if __name__ == "__main__":
    nums = [8, 100, 50,22,15,6,1,1000, 999, 0]
    print("原列表：", nums)
    bubble_sort(nums, sort="descend")
    print("降序排序后的列表：", nums)

    item1 = item("huhu",5)
    item2 = item("haha",3)
    item3 = item("xixi",5)
    item4 = item("hengheng",2)
    item5 = item("gaoshou",8)
    items = [item1,item2,item3,item4,item5]
    item_bubble_sort(items,"descend")
    n = len(items)
    print()
    for i in range(n):
        print(items[i].name,":",items[i].value)
