#coding:utf-8
from numpy import *

def happy(num,wordBag):
    if num in wordBag:
        return False
    if num==1:
        return True
    wordBag.append(num)
    split_num=[]
    while(num):
        split_num.append(num%10)
        num=num//10
    return happy(sum(map(square,split_num)),wordBag)
def square(num):
    return num**2

def isPrime(num):
    ls=[]
    for i in range(2,101):
        flag=0
        for j in range(2,int(sqrt(i))+1):
            if i%j ==0:
                flag=1
                break
        if flag==0:
            ls.append(i)
    return ls

#汉诺塔
def hanno(n,x,y,z):
    if n==1:move(x,z)
    else:
        hanno(n-1,x,z,y)
        move(x,z)
        hanno(n-1,y,x,z)

def move(x,y):

    print '第',i,'步骤',x,'->',y
    i+=1

if __name__=='__main__':
    # print happy(119,[])
    # print isPrime(100)
    # print [i for i in range(2,101) if 0 not in [i%d for d in range(2,int(sqrt(i))+1) ]]
    #-------------汉诺塔------------------
    global i
    i=1
    hanno(3,'A','B','C')
    # ----------------------------------
