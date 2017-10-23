## basicAlgorithm
自己练习算法
### 排序算法
**稳定性**    
          如果Ai = Aj，排序前Ai在Aj之前，排序后Ai还在Aj之前，则称这种排序算法是稳定的。通俗地讲就是保证排序前后两个相等的数的相对顺序不变。
需要注意的是，排序算法是否为稳定的是由具体算法决定的，不稳定的算法在某种条件下可以变为稳定的算法，而稳定的算法在某种条件下也可以变为不稳定的算法。
例如，对于冒泡排序，原本是稳定的排序算法，如果将记录交换的条件改成A[i] >= A[i + 1]，则两个相等的记录就会交换位置，从而变成不稳定的排序算法。
_好处_:
    排序算法如果是稳定的，那么从一个键上排序，然后再从另一个键上排序，第一个键排序的结果可以为第二个键排序所用。基数排序就是这样，先按低位排序，逐次按高位排序，低位排序后元素的顺序在高位也相同时是不会改变的。
 
#### 冒泡排序法
    算法的名字由来是因为越小(或越大)的元素会经由交换慢慢“浮”到数列的顶端。
  
**步骤** :（默认升序排列）  
    1. 比较相邻的元素，如果后一个比前一个严格大，换序。  
    2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。此轮结束后，最后一个位置存放的是当前最大。  
    3. 针对所有的元素重复以上的步骤。  
    4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。  

！[][C:\Users\toby\Evernote\Databases\Attachments\739525-20160328160227004-680964122.gif]
