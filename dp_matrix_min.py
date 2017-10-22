#-*- coding:utf-8 -*-
#http://blog.csdn.net/yang20141109/article/details/51541332
def dp_1(mat):
    m=4
    n=4
    state=[[0 for _ in range(n)]for _ in range(m)]
    #初始化第一行和第一列
    state[0][0]=mat[0][0]
    for i in range(1,m):
        state[i][0]=mat[i][0]+state[i-1][0]
    for j in range(1, n):
        state[0][j] = mat[0][j] + state[0][j-1]
    for i in range(1,m):
        for j in range(1,n):
            # if state[i-1][j]<state[i][j-1]:
            #     path+=(i-1,j)
            # else: path.append(0)
            state[i][j]=min(state[i-1][j],state[i][j-1])+mat[i][j]
    return state
    #寻找路径
def find_path(state):
    m=3
    n=3
    path=[(3,3)]
    i=m
    j=n
    while (i!=0)|(j!=0):
        if i ==0:
            j-=1
            path.insert(0,(i,j))
        if j==0:
            i-=1
            path.insert(0, (i, j))
        if (i>0) & (j>0):
            if state[i-1][j]<state[i][j-1]:
                i-=1
                path.insert(0, (i, j))
            else:
                j-=1
                path.insert(0, (i, j))
    return  path
# #存储空间小的优化方法
# 存储空间小的优化方法时间复杂度为o(n*m)，空间复杂度为o(m)，此方法需要2*m额外空间。
# 当我们求s[i][j]时，s[i-2]行的元素我们就不再需要，
# 我们只需要s[i-1]行中的元素，我们把s[i-1]行中的元素保存在pre数组中，
# 数组的大小为m。我们把s[i]保存在cur数组中，当s[i]行的元素计算完毕以后，
# 我们交换pre和cur数组。因为需要pre数组和cur数组，且数组的大小都为m，
# 所以我们需要2*m大小的额外空间
def dp_2(mat):
    m=4
    n=4
    cur=[0]*4
    pre=[0]*4
    pre[0]=mat[0][0]
    for i in range(1,n):
        pre[i]=mat[i][0]+pre[i-1]
    for i in range(1,m):
        cur[0]=mat[i][0]+pre[0]
        for j in range(1,n):
            if cur[j-1]<pre[j]:
                cur[j]=mat[i][j]+cur[j-1]
            else:
                cur[j] = mat[i][j] + pre[j]
        pre=cur
    return cur[-1]
    #初始化第一行和第一列

if __name__=='__main__':
    mat=[[10,5,7,4],
         [9,11,12,6],
         [1,2,4,9],
         [15,1,1,2]]
    print find_path(dp_1(mat))
