import numpy as np

class Stack(object):
    def __init__(self, n):
        self.maxmize = n
        self.data = ['' for i in range(n)]
        self.top = -1 
        self.len = 0

    def get_len(self):
        return self.len

    def put_data(self, s):
        if self.len<self.maxmize:
            self.top+=1
            self.data[self.top]=s
            self.len+=1
        else:
            print("栈已满，无法入栈。")
    
    def read_top(self):
        if self.len<1:
            print("栈空。")
        else:
            tmp = self.data[self.top]
            return tmp

    def out_data(self):
        if self.len<1:
            print("栈空，无法出栈。")
        else:
            tmp = self.data[self.top]
            self.top-=1
            self.len-=1
            return tmp

    def show(self):
        i = self.top
        while i>=0:
            print(self.data[i])
            i-=1


def check_huiwen(strs):
    #解密回文：判断一个字符串是否为回文
    n = len(strs)
    mid = n//2-1
    
    if n%2==0:
        t = mid+1
    else:
        t = mid+2

    i = mid
    while t < n:
        if strs[t]!=strs[i]:
            return "False"
        i-=1
        t+=1
    
    return "True"


def is_matched(s1, s2):
    if s1=="(" and s2==")":
        return True
    if s1=="{" and s2=="}":
        return True
    if s1=="[" and s2=="]":
        return True
    return False


def check_match(strs):
    n = len(strs)
    if n<1:
        return True
    stack = Stack(n)
    stack.put_data(strs[0])
    for i in range(1,n):
        
        tmp = strs[i]
        if is_matched(stack.read_top(), tmp):
            stack.out_data()
        else:
            stack.put_data(tmp)

    if stack.get_len()==0:
        return True
    else:
        return False



if __name__ == "__main__":
    #回文
    strs = "ahaha"
    print(check_huiwen(strs))
    strs = "xyxayx"
    print(check_huiwen(strs))

    #括号的匹配
    strs = "([)]}{"
    print(check_match(strs))
    strs = "{[()]}"
    print(check_match(strs))



