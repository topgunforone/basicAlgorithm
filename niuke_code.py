#-*- coding:utf-8 -*-
#栈的压入和弹出
def stack_input(in_,out_):
    if len(in_)!=len(out_):return false
    stack_=[]
    len_in=len(in_)
    for i in range(0,len(out_)):
        while (len(stack_) == 0) or (out_[i] != stack_[0]):
            if len_in == 0: return False
            stack_.insert(0, in_.pop(0))
            len_in -= 1
        stack_.pop(0)
    return True
#换一种思路好理解
def stack_input1(_in,_out):
    len_in=len(_in)
    len_out=len(_out)
    stack=[]
    for i in _out:
        stack.append(i)
        while len(stack) and _out[0]==stack[-1]:
            stack.pop()
            _out.pop(0)
    if len(stack):
        return  False
    else:
        return  True
#两个队列表示一个堆栈
class queue2stack:
    def __init__(self):
        self.__queue1=[]
        self.__queue2=[]
    def _push(self,node):
        if self.__queue1 !=[]:
            self.__queue1.append(node)
        else:
            self.__queue2.append(node)
    def _pop(self):
        if self.__queue1 ==[]:
            while len(self.__queue2)>1:
                self.__queue1.append(self.__queue2.pop(0))
            return self.__queue2.pop(0)
        else:
            while len(self.__queue1)>1:
                self.__queue2.append(self.__queue1.pop(0))
            return self.__queue1.pop(0)


#两个堆栈实现一个队列
class Solution:
    def __init__(self):
        self.__stack1=[]
        self.__stack2=[]
    def push(self, node):
        # write code here
        self.__stack1.insert(0,node)
    def pop(self):
        # return xx
        if self.__stack2 ==[]:
            while self.__stack1:
                self.__stack2.insert(0,self.__stack1.pop(0))
        return self.__stack2.pop(0)
#滑动窗口最大☞双端队列
def slide_wind_max(arr,k):
    '''
    :param arr:
    :param k:窗口大小
    :return:
    '''
    que=[]
    result=[]
    for i in range(len(arr)):
        while que!=[] and que[0]<i-k+1:
            que.pop(0)
        while que!=[] and arr[que[-1]]<arr[i]:
            que.pop()
        que.append(i)
        if i>=k-1:
            result.append(arr[que[0]])
    result+=[(result[-1])]*(k-1)
    return result


# 滑动窗口取最大：
def window_max(arr,k):
    result=[]
    window=[0]
    for i in range(len(arr)):
        while  window!=[]and window[0]<=i-k:
            window.pop(0)
        while window !=[] and arr[window[-1]]<arr[i]:
            window.pop()
        window.append(i)
        if i>k-2:
            result.append(arr[window[0]])
    return result




#leecode84题
def find_max_hist(arr):
    arr.append(0)
    stack=[]
    result=-1
    for i in range(len(arr)):
        while stack!=[] and arr[stack[0]]>arr[i]:
            a=stack.pop(0)
            if stack==[]:
                result=max(result,i*arr[a])
            else:
                result=max(result,arr[a]*(i-stack[0]-1))
        stack.insert(0,i)
    return result


def numberOf1(n):
    num=0
    while(n):
        if n%10==1:
             num+=1
        n=n/10
    return num
def between1Andn(n):
    num=0
    for i in range(1,n+1):
        num+=numberOf1(i)
    return num
import numpy as np
def findMaxMat(arr,k):
    '''

    :param arr:ndarray
    :return:
    '''
    arr= np.array(arr)
    len_m=len(arr)
    result=np.zeros((len_m,len_m-k+1))
    result1=np.zeros((len_m-k+1,len_m-k+1))
    for i in range(len_m):
        result[i,:]=window_max(arr[i,:],k)
    for j in range(len_m-k+1):
        result1[:,j]=window_max(result[:,j],k)
    return  result1
# 给定一颗二叉搜索树，请找出其中的第k大的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4
#二叉搜索树的中序遍历就是从小到大的排序
ls=[]
def  KthNode(pRoot, k):
    _mid(pRoot)
    if len(ls)<k:
        return []
    else:return ls[-1]

def _mid(root):
    if not root:
        return
    if len(result) > k: return
    _mid(root.left)
    result.append(root.val)
    _mid(root.left)

#寻找数组中一个等于10的角标
def find10(arr,number):
    #arr得排序
    i=0
    j=len(arr)-1
    while i<j:
        if (arr[i]+arr[j])==number:
            return i,j
        while i<j and (arr[i]+arr[j])<number :
            i+=1
        while i<j and(arr[i]+arr[j])>number:
            j-=1



#最长公共子序列
def getdp(str1,str2):
    m=len(str1)
    n=len(str2)
    dp=[[0]*n for _ in range(m)]
    dp[0][0]= 1 if str1[0]==str2[0]else 0
    for i in range(1,m):
        dp[i][0]=max(dp[i-1][0],1 if str1[i]==str2[0] else 0)
    for j in range(1,n):
        dp[0][j] = max(dp[ 0][j-1], 1 if str1[0] == str2[j] else 0)
    for i in range(1,m):
        for j in range(1, n):
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            if str1[i]==str2[j]:
                dp[i][j] = max(dp[i - 1][j-1]+1, dp[i][j])
    return dp

def lcse(str1,str2):
    if not str1 or not str2:return None
    dp=getdp(str1,str2)
    m=len(str1)-1
    n=len(str2)-1
    _max=dp[-1][-1]
    res=[]
    while _max > 0:
        if m > 0 and dp[m][n] == dp[m - 1][n]:
            m -= 1
        elif n > 0 and dp[m][n] == dp[m][n - 1]:
            n -= 1
        else:
            res.append(str1[m])
            _max -= 1
            m -= 1
            n -= 1
    return res
#最长公共子串
def getdp1(str1,str2):
    m=len(str1)
    n=len(str2)
    dp=[[0]*n for _ in range(m)]
    dp[0][0]= 1 if str1[0]==str2[0]else 0
    for i in range(1,m):
        if str1[i]==str2[0]:
            dp[i][0]=1
    for j in range(1,n):
        if str2[j]==str1[0]:
            dp[0][j]=1
    for i in range(1,m):
        for j in range(1, n):
            if str1[i]==str2[j]:
                dp[i][j] = dp[i-1][j-1]+1
    return dp
def lcse1(str1,str2):
    if not str1 or not str2:return None
    dp=getdp1(str1,str2)
    m=len(str1)
    n=len(str2)
    _max=0
    end=0
   #dp[i][j]是将str1[i],str2[j]当成最后一个字符的情况下，公共子串最长能有多长
    for i in range(m):
        for j in range(n):
            if dp[i][j]>_max:
                end=i
                _max=dp[i][j]
    return str1[(end-_max+1):(end+1)],_max,end

#最长公共子串
def zcggzc(arr1,arr2):
    lena=len(arr1)
    lenb=len(arr2)
    res=[[0]*lenb for _ in range(lena)]
    res[0][0]=1 if arr1[0]==arr2[0] else 0
    for i in range(1,lena):
        res[i][0]=max(0,1 if arr1[i]==arr2[0] else 0)
    for j in range(1,lenb):
        res[0][j]=max(0,1 if arr2[j]==arr1[0] else 0)
    for i in range(1,lena):
        for j in range(1,lenb):
            if arr1[i]==arr2[j]:
                res[i][j]=res[i-1][j-1]+1
            else:
                res[i][j]=max(res[i][j-1],res[i-1][j])
    return res

def find_most_common(arr1,arr2):
    lena = len(arr1)
    lenb = len(arr2)
    dp=zcggzc(arr1,arr2)
    m=lena-1
    n=lenb-1
    res=[]
    step=dp[-1][-1]
    while step:
        if n>0 and dp[m][n]==dp[m][n-1]:
            n=n-1
        if m>0 and dp[m][n]==dp[m-1][n]:
            m=m-1
        else:
            res.append(arr1[m])
            m-=1
            n-=1
            step-=1

    return res

#寻找三元组;


# def find_two(arr,s):
#     i=len(arr)-1
#     j=0
#     res=[]
#     while i<j:
#         if arr[]


def find_middle(arr):
    res = []
    if len(arr) == 1:
        return arr
    for i in range(0, len(arr), 3):
        sorted(arr[i:i + 3])
        res.append(arr[i:i + 3][1])
    return find_middle(res)

a = [1, 2, 3, 4, 5]
print find_middle(a)


def Insert_Sort(arr,left,right):
    #插入排序的中间索引
    len_arr=len(arr)
    for i in range(left+1,right+1):
        tmp=arr[i]
        j=i-1
        while j>=left and arr[j]>tmp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=tmp
    return ((right-left)>>1)+left


def Get_pivot_index(arr,left,right):
    if right-left<5:
        return Insert_Sort(arr,left,right)
    sub_right=left-1
    for i in range(left,right-4+1,5):
        index=Insert_Sort(arr,i,i+4)
        sub_right+=1
        arr[sub_right],arr[index]=arr[index],arr[sub_right]

    return BFPRT(arr,left,sub_right,((sub_right-left+1)>>1)+1)
#利用中位数下标进行划分，返回分界线下标
def partion(arr,left,right, pivot_index):
    arr[pivot_index],arr[right]=arr[right],arr[pivot_index]
    divide_index=left
    for i in range(left,right):
        if arr[i]<arr[right]:
            arr[divide_index],arr[right]=arr[right],arr[divide_index]
            divide_index+=1
    arr[divide_index], arr[right] = arr[right], arr[divide_index]
    return divide_index
def BFPRT(arr,left,right,k):
    pivot_index=Get_pivot_index(arr,left,right)
    divide_index=partion(arr,left,right, pivot_index)
    num=divide_index-left+1
    if num==k:
        return divide_index
    elif num>k:
        return BFPRT(arr,left,divide_index-1,k)
    else :return BFPRT(arr,divide_index+1,right,k-num)

#--简洁的BFPRT------------------------------------------------------------

# Insert_Sort()
# def  find_mid(a,l,r):
#     if l==r:return l,a[l]
#     for i in range(l,r+1,5):
#         Insert_Sort(a,i,i+4)
#         n=i%(4)
#         a[l+n],a[i+2]=a[i+2],a[l+n]
#     num=r-i+1
#     if num>0 and num<5:
#         Insert_Sort(a,i,i+num-1)
#         n=n+1
#         a[l + n ], a[i + num/2] = a[i + num/2], a[l + n]
#     if n==1:return l,a[l]
#     return find_mid(a,l,l+n-1)
def  find_mid(a,l,r):
    if l==r:return l
    # for i in range(l,r-5+1,5):
    #     Insert_Sort(a,i,i+4)
    #     n=i%4
    #     a[l+n],a[i+2]=a[i+2],a[l+n]
    # num=r-i+1
    # if num>0 and num<5:
    #     Insert_Sort(a,i,i+num-1)
    #     n=n+1
    #     a[l + n ], a[i + num/2] = a[i + num/2], a[l + n]
    # if n==1:return l
    # return find_mid(a,l,l+n)
    n=0
    i=0
    offset=(r-l+1)%5
    for i in range(l,r-3,5):
        Insert_Sort(a,i,i+4)
        n=i//5
        a[l+n],a[i+2]=a[i+2],a[l+n]
    if offset:
        start=n*5
        Insert_Sort(a,start,start+offset)
        n+=1
        a[l + n], a[i + offset / 2] = a[i + offset / 2], a[l + n]
    if n == 1: return l
    return find_mid(a,l,l+n)

def partion1(a,l,r,p):
    a[p],a[l]=a[l],a[p]
    i=l
    j=r
    pivot=a[l]
    while i<j:
        while i<j and a[j]>=pivot:
            j-=1
        a[i]=a[j]
        while i<j and a[i]<=pivot:
            i+=1
        a[j]=a[i]
    a[i]=pivot
    return i
def BFPRT1(a,l,r,k):
    p=find_mid(a,l,r)
    # p=find_id(a,l,r,num)
    i=partion1(a,l,r,p)
    m=i-l+1
    if m==k:return a[i]
    if m>k: return BFPRT1(a,l,i-1,k)
    return BFPRT1(a,i+1,r,k-m)


# def find_id(a,l,r,num):
#     for i in range(l,r+1):
#         if a[i]==num:
#             return i
#     return -1

#复习bfpr
def bfprt11(arr,left,right,k):
    id=find_mid11(arr,left,right)
    i=partion11(arr,left,right,id)
    rest=i-left+1
    if rest==k:
        return arr[i]
    elif rest<k:
        return bfprt11(arr,i+1,right,k-i)
    else:return bfprt11(arr,left,i-1,k)

def partion11(arr,left,right,id):
    if left==right:return left
    arr[left],arr[id]=arr[id],arr[left]
    i=left
    j=right
    pivot=arr[left]
    while i<j:
        while i<j and arr[j]>=pivot:
            j-=1
        arr[i]=arr[j]
        while i<j and arr[i]<=pivot:
            i+=1
        arr[j]=arr[i]
    arr[i]=pivot
    return i
def find_mid11(arr,left,right):
    if left==right:return left
    offset=(right-left+1)%5
    n=0
    i=0
    for i in range(left,right-3,5):
        Insert_Sort(arr,i,i+4)
        n=i//5
        arr[left+n],arr[i+2]=arr[i+2],arr[left+n]
    if offset:
        Insert_Sort(arr,n*5 , n*5+offset)
        n = n+1
        arr[left + n], arr[i + offset//2] = arr[i + offset//2], arr[left + n]
    if n==1:return left
    return find_mid11(arr,left,left+n)


if __name__ == '__main__':
    # a=[1,2,3,4,5]
    # b=[4,5,1,3,2]
    # # print stack_input1(a,b)
    # que=queue2stack()
    # que._push(2)
    # que._push(3)
    # # print que._pop(),que._pop()
    # # que._push(4)
    # # que._push(3)
    # # print que._pop(),que._pop()
    # a1=[2,1,5,6,2,3,0]
    # # print 'hist  ' ,find_max_hist(a1)
    # mmat=[[2,3,1],[4,6,7],[5,6,8]]
    # print 'slide windows is ', findMaxMat(mmat,2)
    # # print between1Andn(12)
    # print find10([1,3,4,5,6,7,8],10)
    # print find_most_common('1A5B3D4B56','B1D23CA45B6A')
    # # print lcse1('abcde','bebcd')
    # arr=[1,1,2,3,1,5,-1,7,8,-10]
    # k=5
    # print arr[BFPRT(arr,0,9,6)]
    # print arr
    arr = [1, 1, 2, 3, 1, 5, -1, 7, 8 ]
    print sorted(arr)
    print '->',bfprt11(arr, 0, len(arr)-1, 5)
    print arr