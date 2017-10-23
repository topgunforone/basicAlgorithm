#-*- coding:utf-8 -*-
#排序都是升序
#----------------------------------------------------
def bubble(arr):
    '''
    大数往后放.冒泡排序
    :param arr:
    :return:
    '''
    len_arr=len(arr)
    flag=0
    for i in range(0,len_arr-2):
        for j in range(1,len_arr-i):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                flag=1
        if flag==0:
            return arr
    return arr


#考虑到多种情况的冒泡排序 ,最优的方法
def bubuleSort(arr):
    flag=len(arr)
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
        maxValue =1e+10
        maxInd = -1
        j=i
        while j<len(arr):
            if arr[j]<maxValue:
              maxValue=arr[j]
              maxInd=j
            j=j+1
        arr[i],arr[maxInd]=arr[maxInd],arr[i]

    return arr


#插入排序;带有多次插入,此方法不好，更复杂了
def insert_sort(arr):
    len_arr=len(arr)
    for i in range(1,len_arr):
        k=i-1
        while k>-1 and (arr[k]>arr[k+1]):
            arr[k],arr[k+1]=arr[k+1],arr[k]
            k=k-1
    return  arr
#插入排序，多次比较，一次插入
def insert_sort1(arr):
    for i in range(1,len(arr)):
        tmp=arr[i]
        ind=i-1
        while ind>-1 and arr[ind]>tmp:
            arr[ind+1]=arr[ind]
            ind=ind-1
        arr[ind+1]=tmp
    return arr


#快排序
def quick_sort(arr,L,R):
    i=L
    j=R
    if i>=j: return arr
    key = arr[i]
    while i<j:
        while i<j and arr[j]>=key:
            j-=1
        arr[i]=arr[j]
        while i<j and arr[i]<=key:
            i+=1
        arr[j]=arr[i]
    arr[i]=key
    quick_sort(arr,L,i-1)
    quick_sort(arr,i+1,R)
    return  arr


#二分法
#shell_sort() 原始形式
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
def simplyShellSort(arr):
    gap=len(arr)
    len_arr=len(arr)
    while gap>>1:
        gap=gap>>1
        for i in range(gap,len_arr):
            k=i-gap
            if arr[k+gap]<arr[k]:#开始组内的插入排序
                while(k>-1) and (arr[k]>arr[k+gap]):
                    arr[k],arr[k+gap]=arr[k+gap],arr[k]
                    k-=gap
    return arr


#归并排序 的递归形式
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
def mergeSort(arr):
    len_arr=len(arr)
    flag=2
    while(flag<=len_arr):
        #分组 排序
        for i in range(0,len_arr,flag):
            left=arr[i:i+flag//2]
            right=arr[i+flag//2:(i+flag)]
            arr[i:(i+flag)]=merge(left,right)
        flag = 2 * flag
    if flag//2<len_arr:
        arr=merge(arr[:flag//2],arr[flag//2:])
    return arr


#堆排分割线-----------------------------------------------------
#最大堆
def sift_down(arr, start, end):
    root = start
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1
        if child > end:#如果没有孩子，不需要调整
            break

        # 找出两个child中交大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        #不执行上步骤，就只有一个孩子。执行上步骤，有两个孩子
        if arr[root] < arr[child]:
            # 最大堆小于较大的child, 交换顺序.交换后以被交换的孩子作为root继续
            arr[root], arr[child] = arr[child], arr[root]

            # 正在调整的节点设置为root
            root = child
        else:
            # 无需调整的时候, 退出
            break


def heap_sort(arr):
    # 从最后一个有子节点的孩子开始调整最大堆
    first = len(arr) // 2 - 1
    for start in range(first, -1, -1):
        tuning_head(arr, start, len(arr) - 1)

    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(arr) -1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        tuning_head(arr, 0, end - 1)
    return arr


#递归形式
def tuning_head(arr, start, end):
    child = start * 2 + 1  # 左孩子
    if child > end:  # 没有孩子
        return
    if child+1<=end and  arr[child+1]<arr[child]:
        child+=1
    if  arr[child]<arr[start]:
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
        if  arr[child]>arr[root]:
            arr[root],arr[child]=arr[child],arr[root]
            root=child
        else:
            break


def sort_head(arr):
    first=len(arr)//2-1
    for start in range(first,-1,-1):
        tuning_head(arr, start, len(arr)-1)

    for end in range(len(arr)-1,0,-1):
        arr[0],arr[end]=arr[end],arr[0]
        tuning_head(arr,0, end-1)
    return arr
#--------------------------------------------------------






if __name__ == '__main__':
    arr=[2,1,4,1,5,9,2,1,6]
    # print insert_sort(arr)
    # print quick_sort(arr,0,len(arr)-1)
    # print bubble(arr)
    print insert_sort1(arr)
