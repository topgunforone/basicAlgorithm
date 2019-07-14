# encoding:utf-8
# all sorted set is ascending
# bubble sort
# 一般无优化
# 这样的写法是 ，大数往后冒。list 后面优先排好
# 冒泡排序法
def bubble_sort(arr):
    m = len(arr)
    if m<2:return arr
    for i in range(m):
        for j in range(i,m-i-1):# j+i+1<m | +1是因为for 循环内有j+1
            if arr[j]>arr[j+1]:  #  大于是稳定算法。如果是大于等于 则是不稳定算法
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# 优化 如果一趟冒泡无排序，则说明已经排好序了
def bubble_sort(arr):
    m = len(arr)
    if m<2:return arr
    for i in range(m):
        flag =True
        for j in range(i,m-i-1):# j+i+1<m | +1是因为for 循环内有j+1
            if arr[j]>arr[j+1]:  #  大于是稳定算法。如果是大于等于 则是不稳定算法
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = False
        if flag == True:
            return arr
    return arr

# # 再优化，如果是 前5个无顺序后100个有顺序则只需要对前五个排序
# def bubble_sort_front(arr):
#     m = len(arr)
#     flag = m
#     if m<2:return arr
#     while flag:
#         m = flag
#         flag = 0 # 每次循环都是有可能排好序了
#         for j in range(m-1): # j+i+1<m | +1是因为for 循环内有j+1
#             if arr[j] > arr[j+1]:  # 大于是稳定算法。如果是大于等于 则是不稳定算法
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 flag = j+1  # 说明前j+1 个还没有排好序
#     return arr
# bubble_sort_front([3,1,4,1,5])



# 选择排序 每次从后面选出极值排列
def select_sort(arr):
    m = len(arr)
    if m < 2: return arr
    for i in range(0,m):
        # 从i往后选择最小的一个数, 同时记录对应的坐标
        min_ = arr[i]
        min_idx = i
        for j in range(i+1,m):
            if arr[j]<min_:
                min_ = arr[j]
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx], arr[i]
    return arr
select_sort([3,1,4,1,5,9])

# 插入排序
def insert_sort(arr):
    m = len(arr)
    if m<2:return arr
    for i in range(1,m): # 从1开始也没问题，为了方便
        j = i
        while j<m and arr[j]<arr[j-1] : # 因为下面 j-1>0 j< m
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j - 1
    return arr
insert_sort([3,1,4,1,5,9,10,9])

# nlogn 的写法 插入排序算法
def insert_arr_nlogn(arr):
    for i in range(1,len(arr)):
        select_insert(arr,arr[i],i)
    return arr
def select_insert(arr,target,i):
    a = arr[:i]
    if target>=a[-1]:
        arr[i] =target
    elif target<=a[0]:
        arr[1:i+1]=arr[:i]
        arr[0]=target
    else:
        left = 0
        right = len(a)-1
        while left+1<right:
            mid = (left+right)//2
            if a[mid]<target:
                left = mid
            else:
                right = mid
        arr[right+1:i+1] =  arr[right:i]
        arr[right] = target
# 快速排序,网上很多版本，我喜欢这个版本
def quick_sort(arr):
    m = len(arr)
    if m<2:return
    quick_sort_helper(arr,0,len(arr)-1)  # len(arr)-1 是坐标
    return arr
def quick_sort_helper(arr,left,right):
    start = left
    end =  right
    if left>right:return
    pivot = arr[left+(right-left)//2]
    while left <= right:
        # 只是相遇
        while left <= right and arr[right]>pivot:
            right = right - 1
        while left <= right and arr[left]<pivot:
            left= left + 1
        if left <= right:
        # 相遇之后的错过
            arr[left], arr[right] = arr[right], arr[left]
            left =left + 1
            right = right - 1
    quick_sort_helper(arr,start,right)
    quick_sort_helper(arr, left, end)
    return arr


def quick_sort(arr,left,right):
    start = left
    end = right
    if start >end:return
    pivot= arr[(left+right)//2]
    while left<=right:
        # 只是碰头
        while left<=right and arr[left]<pivot:
            left =left+1
        while left<=right and arr[right]>pivot:
            right =right-1
        if left<=right:
        #碰头了后错过
            arr[left],arr[right] =arr[right],arr[left]
            left = left + 1
            right = right - 1
    quick_sort(arr,start,right)
    quick_sort(arr,left,end)
    return arr




# merge_sort() 分治 divide & conquer


def merge_sort(arr):
    m = len(arr)
    if m<2:return arr
      # 左边排好序的
      # 右边拍好序的
    left = merge_sort(arr[:m//2])
    right = merge_sort(arr[m//2:])
    return merge_sort_helper(left,right)



def merge_sort_helper(left,right):
    m, n = 0, 0
    total =[]
    while m<len(left) and n<len(right):
        if left[m] <right[n]:
            total.append(left[m])
            m = m + 1
        else:
            total.append(right[n])
            n = n + 1
    total += left[m:]
    total += right[n:]
    return total

merge_sort([3,1,4,1,5,9,2,6])




# merget no curse
def merge_no_curse(arr):
    flag = 2
    m = len(arr)
    while flag <2*m:
        for i in range(0,m,flag):
            arr[i:i+flag] = merge_sort_helper(arr[i:flag//2],arr[flag//2:i+flag])
        flag = flag*2
    return arr
# shell_sort
def shell_sort(arr):
    gap = len(arr)//2
    while gap:
        for i in range(gap):
            for  j in range(i,len(arr),gap):
            # 插入排序
                k = j - gap
                while k >-1  and arr[k+gap]<arr[k]:
                    arr[k], arr[k+gap] =arr[k+gap], arr[k]
                    k = k - gap
        gap =gap//2
    return arr
print(shell_sort([3,1,4,1,5,9,2,6]))



# heap_sort

def heap_sort(arr):
    # 从最后一个有叶子节点的孩子 从下到上，从左到右开始构建最大堆
    first = len(arr) // 2 - 1
    for start in range(first, -1, -1):   #收缩start-->0 [start,end],[start-1,end],start-2,end],...往下调整
        tuning_head(arr, start, len(arr) - 1) #

    # 将最大的放到堆的最后一个, 堆-1, 将heap 的元素往下调整 收缩end->0
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

def heap_sort(arr):
    m = len(arr)//2-1
    for i in range(m,-1,-1):
        tuning_head(arr,i,len(arr)-1)
    for j in range(len(arr)-1,0,-1):
        arr[j],arr[0]  =arr[0],arr[j]
        tuning_head(arr,0,j-1)



def heap_sort(arr):
    m =  len(arr)//2-1
    for i in range(m,-1,-1):
        tuning_head(arr,i,len(arr)-1)
    for  j in range(len(arr)-1,0,-1):
        arr[j],arr[0] = arr[0],arr[j]
        tuning_head(arr,0,j-1)
    return arr

def heap_sort_no_curse(arr):
    m =  len(arr)//2-1
    for i in range(m,-1,-1):
        tuning_head_no_curse(arr,i,len(arr)-1)
    for  j in range(len(arr)-1,0,-1):
        arr[j],arr[0] = arr[0],arr[j]
        tuning_head_no_curse(arr,0,j-1)
    return arr


def tuning_head_no_curse(arr,start,end):
    # 跳跃性质
    while True:
        child = 2 * start + 1  # left child
        if child>end:return  # 如果越界
        if child+1 <= end and arr[child+1] > arr[child]:
            child += 1
        if arr[child]>arr[start]: # 如果子代比父亲大
            arr[child], arr[start] = arr[start], arr[child]
            start = child
        else:
            break
heap_sort_no_curse([3,1,4,1,5,9,2,6])


