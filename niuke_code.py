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
        while que!=[] and que[0]<i-k:
            que.pop(0)
        while que!=[] and arr[que[-1]]<arr[i]:
            que.pop()
        que.append(i)
        result.append(arr[que[0]])
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






if __name__ == '__main__':
    a=[1,2,3,4,5]
    b=[4,5,1,3,2]
    # print stack_input1(a,b)
    que=queue2stack()
    que._push(2)
    que._push(3)
    # print que._pop(),que._pop()
    # que._push(4)
    # que._push(3)
    # print que._pop(),que._pop()
    a1=[2,1,5,6,2,3,0]
    print 'hist  ' ,find_max_hist(a1)
    print 'slide windows is ', slide_wind_max(a1,3)