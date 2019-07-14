#-*- coding:utf-8 -*-
#排序都是升序
import numpy as np
#----------------------------------------------------
####  基本的bubble算法
def bubble(arr):
    len_arr=len(arr)
    for i in range(0,len_arr):
        for j in range(len_arr-1,i,-1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr
# print bubble([5,4,3,2,2,2,1])



#考虑到多种情况的冒泡排序 ,最优的方法
def bubuleSort(arr):
    flag=len(arr) #记录需要排到的角标
    while flag:
        n=flag
        flag=0#每次都有可能不需要排序
        for  j in range(1,n):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                flag=j
    return arr


#选择排序
def select_sort(arr):
    for i in range(0,len(arr)-1):
        _min=i
        for j in range(i+1,len(arr)):
            _min=j if arr[j]<arr[_min] else _min
        if _min !=i:
            arr[i],arr[_min]=arr[_min],arr[i]
    return arr

#插入排序;带有多次插入
def insert_sort(arr):
    len_arr=len(arr)
    for i in range(1,len_arr):
        k=i-1
        while k>-1 and (arr[k]>arr[k+1]):
            arr[k],arr[k+1]=arr[k+1],arr[k]
            k=k-1
    return  arr

# #插入排序，多次比较，一次插入
# def insert_sort1(arr):
#     for i in range(1,len(arr)):
#         tmp=arr[i]
#         ind=i-1
#         while ind>-1 and arr[ind]>tmp:
#             arr[ind+1]=arr[ind]
#             ind=ind-1
#         arr[ind+1]=tmp
#     return arr
arr = [3,1,4,1,5]
def insert_arr(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            while j>0:
                if  arr[j]>arr[j-1]:
                    arr[j],arr[j-1] = arr[j-1],arr[j]
                j= j -1
    return arr


def merge_sort(arr):
    if len(arr)<2:return arr
    left  =merge_sort(arr[:len(arr)//2])
    right  =merge_sort(arr[len(arr)//2:])
    return merge_sort_helper(left,right)

def merge_sort_helper(left,right):
    tot = []
    i =0
    j = 0
    while i <len(left) and j< len(right):
        if left[i]<right[j]:
            tot.append(left[i])
            i = i + 1
        else:
            tot.append(right[j])
            j = j + 1
    tot.extend(left[i:])
    tot.extend(right[j:])
    return tot

#一般快排序
def quick_sort(arr,L,R):
    i=L
    j=R
    if i>=j: return arr
    pivot = arr[i]
    while i<j:
        while i<j and arr[j]>=pivot:
            j-=1
        arr[i]=arr[j]
        while i<j and arr[i]<=pivot:
            i+=1
        arr[j]=arr[i]
    arr[i]=pivot
    quick_sort(arr,L,i-1)
    quick_sort(arr,i+1,R)
    return  arr


#最容易解释的快排
def quicksort(arr,L,R):
    i=L
    j=R
    if i>=j:return arr
    pivot=arr[i]
    while i<j:
        while i < j and pivot <=arr[j]:
            j -= 1
        while i<j and arr[i]<=pivot:
            i+=1
        arr[i],arr[j]=arr[j],arr[i]
    arr[i],arr[L]=arr[L],arr[i]
    quicksort(arr,L,i-1)
    quicksort(arr,i+1,R)
    return arr

#二分法
#按照原理来的原始形式
def shell_sort(arr):
    lenArr=len(arr)
    gap=len(arr)
    while(gap//2):
        gap=gap//2
        for j in range(gap):
            for i in range(j,lenArr,gap):
                k=i-gap
                while  (k>-1)and (arr[k]>arr[k+gap]):#在每一组内插排
                    arr[k+gap],arr[k]=arr[k],arr[k+gap]
                    k=k-gap
    return arr



#shell排序的简单形式
# def simplyShellSort(arr):
#     gap=len(arr)
#     len_arr=len(arr)
#     while gap>>1:
#         gap=gap>>1
#         for i in range(gap,len_arr):
#             k=i-gap
#             if arr[k+gap]<arr[k]:#开始组内的插入排序
#                 while(k>-1) and (arr[k]>arr[k+gap]):
#                     arr[k],arr[k+gap]=arr[k+gap],arr[k]
#                     k-=gap
#     return arr

def shell(arr):
    gap=len(arr)
    while gap:
        for i in range(gap,len(arr)):
            for j in range(i-gap,-1,-gap):
                if arr[j]>arr[j+gap]:
                    arr[j+gap],arr[j]=arr[j],arr[j+gap]
        gap=gap//2
    return arr

#归并排序的递归形式
def mergeSort(arr):
    if len(arr)<=1:return arr
    m=len(arr)//2
    left=mergeSort(arr[:m])
    right=mergeSort(arr[m:])
    return  merge(left,right)



def merge(left,right):
    i,j=0,0
    result=[]
    while (i<len(left)) and (j<len(right)):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return  result


#非递归形式的归并排序，用到上文的merge函数
def merge_Sort(arr):
    len_arr=len(arr)
    flag=2#标记变量
    while(flag<len_arr):#如果是刚好或者大于，则不需再进一步排序。
        #分组 排序
        for i in range(0,len_arr,flag):
            left=arr[i:i+flag//2]
            right=arr[i+flag//2:(i+flag)]
            arr[i:(i+flag)]=merge(left,right)
        flag = 2 * flag
    if flag//2<len_arr:#如果最终差了一截需要多做一次
        arr=merge(arr[:flag//2],arr[flag//2:])
    return arr

def heap_sort(arr):
    # 从最后一个有子节点的孩子开始调整最大堆
    first = len(arr) // 2 - 1
    for start in range(first, -1, -1):   #由后往前调整
        tuning_head(arr, start, len(arr) - 1)  #调整根的时候是大的往上冒，建立大跟堆得到升序

    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(arr) -1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        tuning_head(arr, 0, end - 1)
    return arr

def tuning_head(arr, start, end):
    child = start * 2 + 1  # 左孩子
    if child > end:  # 没有孩子
        return
    if child+1<=end and  arr[child+1]>arr[child]:
        child+=1
    if  arr[child]>arr[start]:
        arr[child],arr[start]=arr[start],arr[child]
        tuning_head(arr,child,end)

#非递归形式
def tuning_head1(arr,start,end):
    root=start
    while True:
        child=root*2+1#左孩子
        if child>end:#没有孩子
            break
        if child+1<=end and arr[child+1]>arr[child]:
            child=child+1
        if  arr[child]>arr[root]:#如果此处不满足，接下来也不会满足，所以可以break掉
            arr[root],arr[child]=arr[child],arr[root]
            root=child
        else:
            break#



#归并排序复习-------------------
# def mergeSort11(arr):
#     len_arr=len(arr)
#     flag=1
#     while flag<len_arr:
#         flag*=2
#         for i in range(0,len_arr,flag):
#             arr[i:i+flag]=merge1(arr[i:i+flag/2],arr[i+flag/2:i+flag])#python对 a[m,n]:的右边项有很好的处理
#     return arr
#
#
# def merge1(left,right):
#     a=[]
#     i,j=0,0
#     while i<len(left) and j<len(right):
#         if left[i]>right[j]:
#             a.append(right[j])
#             j+=1
#         else:
#             a.append(left[i])
#             i+=1
#     a.extend(left[i:])
#     a.extend(right[j:])
#     return a
#
#
# #-----------------------------------
#
# #堆排分割线-----------------------------------------------------
# #最大堆
# def sift_down(arr, start, end):
#     root = start
#     while True:
#         # 从root开始对最大堆调整
#         child = 2 * root + 1 #左孩子
#         if child > end:#如果没有孩子，不需要调整
#             break
#
#         # 找出两个child中交大的一个
#         if child + 1 <= end and arr[child] < arr[child + 1]:
#             child += 1
#         #不执行上步骤，就只有一个孩子。执行上步骤，有两个孩子
#         if arr[root] < arr[child]:
#             # 最大堆小于较大的child, 交换顺序.交换后以被交换的孩子作为root继续
#             arr[root], arr[child] = arr[child], arr[root]
#
#             # 正在调整的节点设置为root
#             root = child
#         else:
#             # 无需调整的时候, 退出
#             break
# def heap_sort(arr):
#     # 从最后一个有子节点的孩子开始调整最大堆
#     first = len(arr) // 2 - 1
#     for start in range(first, -1, -1):   #由后往前调整
#         tuning_head(arr, start, len(arr) - 1)  #调整根的时候是大的往上冒，建立大跟堆得到升序
#
#     # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
#     for end in range(len(arr) -1, 0, -1):
#         arr[0], arr[end] = arr[end], arr[0]
#         tuning_head(arr, 0, end - 1)
#     return arr
#
#
# #大的数往上冒
# def heapInsert(arr,index):
#     while arr[index]>arr[(index-1)//2]:
#         arr[index],arr[(index-1)//2]=arr[(index-1)//2], arr[index]
#         index=(index-1)//2
#
# #小的数往下沉
# def heapify(arr,index,size):
#     left=2*index+1
#     while left<size:
#         if left+1<size and arr[left+1]>arr[left]:
#             left=left+1
#         if arr[index]>arr[left]:
#             break
#         else:
#             arr[index],arr[left]=arr[left],arr[index]
#             left = 2 * index + 1
#
# def tuning_head(arr, start, end):
#     # type: (np.ndarray, int, int) -> array
#     child = start * 2 + 1  # 左孩子
#     if child > end:  # 没有孩子
#         return
#     if child+1<=end and  arr[child+1]>arr[child]:
#         child+=1
#     if  arr[child]>arr[start]:
#         arr[child],arr[start]=arr[start],arr[child]
#         tuning_head(arr,child,end)
#
# #非递归形式
# def tuning_head1(arr,start,end):
#     root=start
#     while True:
#         child=root*2+1#左孩子
#         if child>end:#没有孩子
#             break
#         if child+1<=end and arr[child+1]>arr[child]:
#             child=child+1
#         if  arr[child]>arr[root]:#如果此处不满足，接下来也不会满足，所以可以break掉
#             arr[root],arr[child]=arr[child],arr[root]
#             root=child
#         else:
#             break#
# def tuning(arr,start,end):
#     #小堆根
#     child = start * 2 + 1
#     while child<=end:
#         if child+1<=end and arr[child]<arr[child+1]:
#             child=child+1
#         if arr[child]>arr[start]:
#             arr[child],arr[start]=arr[start],arr[child]
#         start = child
#         child = start * 2 + 1

 #环形报数
#     class
#     Solution
#     {
#         public:
#             int LastRemaining_Solution(unsigned int n, unsigned
#     int
#     m)
#     {
#     if (n == 0)
#     return -1;
#     if (n == 1)
#         return 0;
#     else
#         return (LastRemaining_Solution(n - 1, m) + m) % n;
#
# }
# };
# #模拟环形
# class Solution:
#     def LastRemaining_Solution(self, n, m):
#         # write code here
#         if not m or not n:
#             return -1
#         res = range(n)
#         i = 0
#         while len(res)>1:
#             i = (m+i-1)%len(res)
#             res.pop(i)
#         return res[0]




#--------------------------------------------------------

# if __name__ == '__main__':
#     arr=np.array([2,1,4,9,1,4,3,2,8])
#     # print insert_sort(arr)
#     # print quick_sort(arr,0,len(arr)-1)
#     # print bubble(arr)
#     # print shel(arr)
#     # print quicksort([3,2,5,1],0,3)
#     print (shell(arr))