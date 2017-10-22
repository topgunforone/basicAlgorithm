#-*- coding:utf-8 -*-
#递归实现
def dp_1(mat,m,n,path):
    if m==0:
        if n>0:
            return dp_1(mat,0,n-1,path)+mat[0][n]
        else:
            return mat[0][0]
    if n==0:
        if m>0:
            return dp_1(mat,m-1,0,path)+mat[m][0]
        else:
            return mat[0][0]
    return max(dp_1(mat,m,n-1,path),dp_1(mat,m-1,n,path))+mat[m][n]
#堆栈实现
# def dp_2(mat,m,n):


if __name__=='__main__':
    mat=[[10,5,7,4],
         [9,11,12,6],
         [1,2,4,9],
         [15,1,1,2]]
    mat1=[[2,5,6],[3,9,4],[7,9,1]]
    path=[]
    print dp_1(mat1,2,2,path),path
