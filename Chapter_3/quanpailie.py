import numpy as np

def fun1():
#123的全排列
    book = np.zeros((4,), dtype=int)
    a = np.zeros((4,), dtype=int)
    total = 0
    for a[1] in range(1,4):
        book[a[1]]+=1
        for a[2] in range(1,4):
            if book[a[2]]>0:
                continue
            book[a[2]]+=1
            for a[3] in range(1,4):
                if book[a[3]]>0:
                    continue 
                print("%d%d%d" %(a[1],a[2],a[3]))
                total+=1

            book[a[2]]-=1
        book[a[1]]-=1
    print("总的全排列个数为：%d" %total)
    
def fun2():
#1234的全排列
    book = np.zeros((5,), dtype=int)
    a = np.zeros((5,), dtype=int)
    total = 0
    for a[1] in range(1,5):
        book[a[1]]+=1
        for a[2] in range(1,5):
            if book[a[2]]>0:
                continue
            book[a[2]]+=1
            for a[3] in range(1,5):
                if book[a[3]]>0:
                    continue 
                book[a[3]]+=1
                for a[4] in range(1,5):
                    if book[a[4]]>0:
                        continue
                    print("%d%d%d" %(a[1],a[2],a[3]))
                    total+=1
                book[a[3]]-=1
            book[a[2]]-=1
        book[a[1]]-=1
    print("总的全排列个数为：%d" %total)
    
if __name__=="__main__":
    print("123的全排列")
    fun1()
    print()
    print("1234的全排列")
    fun2()