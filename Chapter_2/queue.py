import numpy as  np


class Queue(object):
    def __init__(self, n):
        self.maxsize = n
        self.data = np.zeros((n, ), dtype=int)
        self.head = 0
        self.tail = 0
        self.len = 0
    
    def get_len(self):
        return self.len
    
    def put_data(self, x):
        if self.len>=self.maxsize:
            print("队列已满，不可入队。")
        else:
            self.data[self.tail] = x
            self.tail = (self.tail+1)%self.maxsize
            self.len +=1
    
    def out_data(self):
        if self.len>0:
            tmp = self.data[self.head]
            self.head = (self.head+1)%self.maxsize
            self.len -=1
            return tmp
        else:
            print("队列为空，不可出队。")

    def show(self):
        i=self.head
        t = 0
        while t<self.len:
            print(self.data[i])
            i = (i+1)%self.maxsize
            t+=1

if __name__=="__main__":
    nums = [6,3,1,7,5,8,9,2,4]
    print("加密数组：", nums)
    queue = Queue(10)
    n = len(nums)
    for i in range(n):
        queue.put_data(nums[i])

    qq_num = []
    while queue.get_len()>1:
        qq_num.append(int(queue.out_data()))
        tmp = queue.out_data()
        queue.put_data(tmp)

    qq_num.append(int(queue.out_data()))
    print("解密的QQ号码：",qq_num)
    
