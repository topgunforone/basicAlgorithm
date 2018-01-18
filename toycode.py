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
def hanno(n,x,y,z):# 有n个 x借助于y移动到z
    if n==1:move(x,z)
    else:
        hanno(n-1,x,z,y) #x 借助于z 移动到y
        move(x,z)
        hanno(n-1,y,x,z)

def move(x,y):
    global i
    print '第',i,'步骤',x,'->',y
    i+=1


#翻转数
def reverse(number):
    if number==0:return number
    flag=0
    if number<0:
        return 0-reverse_num(abs(number))
    else:
        return reverse_num(number)
def reverse_num(num):
    new_num=0
    #去除低位的零
    while not num%10:
        num=num//10
    while(num>0):
        new_num=new_num*10+num%10
        num=num//10
    return new_num

#三个数求和
def tree_sum(arr,target):
    res=[]
    arr.sort()
    len_arr=len(arr)
    for i in range(0,len_arr-1):
        if i!=0 and arr[i]==arr[i-1]:continue
        p=i+1;q=len_arr-1
        while p<q:
            sum = arr[i] + arr[p] + arr[q]
            if sum==target:
                res.append([arr[i],arr[p],arr[q]])
                p = +1
                while arr[p]==arr[p-1]:
                    p=p+1
                q = q - 1
                while arr[q]==arr[q+1]:
                    q=q-1
            else:
                if sum>target:
                    q=q-1
                else: p=p+1
    return res




if __name__=='__main__':
    # print happy(119,[])
    # print isPrime(100)
    # print [i for i in range(2,101) if 0 not in [i%d for d in range(2,int(sqrt(i))+1) ]]
    #-------------汉诺塔------------------
    # i=1
    # hanno(3,'A','B','C')
    # ----------------------------------
    # print reverse(-1230100)
    print tree_sum([1,2,3,2,1],5)
