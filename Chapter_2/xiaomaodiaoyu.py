import numpy as np
from queue import Queue
from stack import Stack

if __name__=="__main__":
    nums1 = [2,4,1,2,5,6]
    nums2 = [3,1,3,5,6,4]
    n1, n2 = len(nums1), len(nums2)
    n = n1+n2
    q1 = Queue(n)
    q2 = Queue(n)
    
    for i in range(n1):
        q1.put_data(nums1[i])
    for i in range(n2):
        q2.put_data(nums2[i])
    
    s = Stack(n)
    book = np.zeros((10,), dtype=int)
    while q1.get_len()>0 and q2.get_len()>0:
        #先q1出牌
        tmp = q1.out_data()
        #底牌有同一张牌
        if book[tmp]>0:
            q1.put_data(tmp)
            top = s.out_data()
            while top!=tmp:
                q1.put_data(top)
                book[top]=0
                top = s.out_data()
            q1.put_data(top)
            book[top]=0
        else:
            s.put_data(tmp)
            book[tmp]=1
        if q1.get_len()==0:
            break
        #q2出牌
        tmp = int(q2.out_data())
        #底牌有同一张牌
        if book[tmp]>0:
            q2.put_data(tmp)
            top = s.out_data()
            while top!=tmp:
                q2.put_data(top)
                book[top]=0
                top = s.out_data()
            book[top]=0
            q2.put_data(top)
        else:
            s.put_data(tmp)
            book[tmp]=1
    
    if q1.get_len()==0:
        print("P2赢。")
        print("P2手中的牌：")
        q2.show()
        print("地上的牌：")
        s.show()
    else:
        print("P1赢。")
        print("P1手中的牌：")
        q1.show()
        print("地上的牌：")
        s.show()
        