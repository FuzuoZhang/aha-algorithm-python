import numpy as np


# ?3 * 6528 = 3? * 8256
def fun1():
    for i in range(1,10):
        if (i*10+3)*6528 ==(30+i)*8256:
            print("空格处的数字为：",i)


#???+???=???
#要求将数字1-9填入以上各?处，使等式成立，且每个数字只能使用一次
#9^10，要跑很久才能出结果
def fun2():
    total = 0
    a = np.zeros((10,),dtype=int)
    for a[1] in range(1,10):
        for a[2] in range(1,10):
            for a[3] in range(1,10):
                for a[4] in range(1,10):
                    for a[5] in range(1,10):
                        for a[6] in range(1,10):
                            for a[7] in range(1,10):
                                for a[8] in range(1,10):
                                    for a[9] in range(1,10):
                                        book = np.zeros((10,), dtype=int)
                                        sum_book = 0
                                        for i in range(1,10):
                                            book[a[i]]=1
                                        sum_book = np.sum(book)
                                        if sum_book==9 and a[1]*100+a[2]*10+a[3]+a[4]*100+a[5]*10+a[6]==a[7]*100+a[8]*10+a[9]:
                                            print("%d%d%d+%d%d%d=%d%d%d" %(a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]))
                                            total +=1
    print("总的可能结果数为：",(total+1)//2)         


#???+???=???
#要求将数字1-9填入以上各?处，使等式成立，且每个数字只能使用一次
#采用回溯搜索的策略来做，避免进行无用功的消耗
def fun3():
    book = np.zeros((10,), dtype=int)
    a = np.zeros((10,),dtype=int)
    total = 0
    for a[1] in range(1,10):
        book[a[1]]+=1
        for a[2] in range(1,10):
            if book[a[2]]>0:
                continue
            book[a[2]]+=1
            for a[3] in range(1,10):
                if book[a[3]]>0:
                    continue
                book[a[3]]+=1
                for a[4] in range(1,10):
                    if book[a[4]]>0:
                        continue
                    book[a[4]]+=1
                    for a[5] in range(1,10):
                        if book[a[5]]>0:
                            continue
                        book[a[5]]+=1
                        for a[6] in range(1,10):
                            if book[a[6]]>0:
                                continue
                            book[a[6]]+=1
                            for a[7] in range(1,10):
                                if book[a[7]]>0:
                                    continue
                                book[a[7]]+=1
                                for a[8] in range(1,10):
                                    if book[a[8]]>0:
                                        continue
                                    book[a[8]]+=1
                                    for a[9] in range(1,10):
                                        if book[a[9]]>0:
                                            continue
                                        book[a[9]]+=1
                                        if a[1]*100+a[2]*10+a[3]+a[4]*100+a[5]*10+a[6]==a[7]*100+a[8]*10+a[9]:
                                            print("%d%d%d+%d%d%d=%d%d%d" %(a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]))
                                            total +=1
                                        book[a[9]]-=1
                                    book[a[8]]-=1
                                book[a[7]]-=1
                            book[a[6]]-=1
                        book[a[5]]-=1
                    book[a[4]]-=1
                book[a[3]]-=1
            book[a[2]]-=1
        book[a[1]]-=1

    print("总的可能结果数为：",(total+1)//2) 



if __name__=="__main__":
    print("第一题：")
    fun1()
    print("第二题：")
    #fun2()
    fun3()