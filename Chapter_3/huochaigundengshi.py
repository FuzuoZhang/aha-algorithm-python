import numpy as np


def compute(x):
    stand = [6,2,5,5,4,5,6,3,7,6]
    total = 0
    while x>=10:
        y = x%10
        total += stand[y]
        x = x//10
    total += stand[x]
    return total

if __name__ == "__main__":
    total = 0
    for a in range(0,1112):
        for b in range(0,1112):
            c = a+b
            if compute(a)+compute(b)+compute(c)==14:
                print("%d+%d=%d" %(a,b,c))
                total +=1
    print("总的可能方案数为：%d" %total)
            