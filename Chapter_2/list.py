import numpy as np

class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    
if __name__ == "__main__":
    nums = [1,3,6,9,10]
    n = len(nums)

    head = None
    for i in range(n):
        p = ListNode(nums[i])
        if head==None:
            head = p
        else:
            q.next = p
        q = p
    
    x = 8
    if x<head.value:
        tmp = ListNode(x)
        tmp.next = head
        head =tmp
    else:
        p = head
        while p.next!=None and p.next.value<x:
            p=p.next
        tmp = ListNode(x)
        tmp.next = p.next
        p.next = tmp
    
    p = head
    while p!=None:
        print(p.value)
        p = p.next
    
