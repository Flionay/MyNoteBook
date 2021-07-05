## [剑指 Offer 03. 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

### 题目【难度简单】

找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

**示例 1：**

```
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
```

**限制：**

```
2 <= n <= 100000
```

 ### 思路

方法一：利用hashset，这个比较简单，直接看代码即可。

**原地交换：**

主要思想上是首先循环，然后判断该下标位置上的数字是否与下标相等，不想等的话，把这个数字放到它该在的位置去（35 就放到a[35]）,然后让a[35]的数字交换过来，如果这个数字交换过来于下标想等，就存放下来，不相等继续交换，如果发现这个地方已经有等于下标的数了，那么就找到了重复数字。

### 代码

```java
class Solution {
    public int findRepeatNumber(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for(int i: nums){
            if (set.contains(i)){
                return i;
            }
            set.add(i);
        }
        return -1;    
    }
}
```

```java
class Solution {
    public int findRepeatNumber(int[] n) {
        int t= 0;
        for(int i=0;i<n.length;i++){
            if(n[i]!=i){
                t = n[n[i]];
                n[n[i]] = n[i];
                if (n[i]==t){
                    return t;
                }else{
                    n[i] = t;
                }
            }else{
                continue;
            }
        }
        return -1;
    }   
}
```

## [剑指 Offer 04. 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)

难度中等371收藏分享切换为英文接收动态反馈

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

**示例:**

现有矩阵 matrix 如下：

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

给定 target = `5`，返回 `true`。

给定 target = `20`，返回 `false`。

 

**限制：**

```
0 <= n <= 1000
0 <= m <= 1000
```

### 思路

### 解题

```java
class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if  (matrix.length ==0){
            return false;
        }else if (matrix[0].length==0){
            return false;
        }

        int row = matrix.length;
        int col = matrix[0].length;
        int j=0,i=row-1;
        while (i>=0 && j<col){
            if (target<matrix[i][j]){       //  目标太小 往上边寻找
                i--;
            }else if(target>matrix[i][j]){  //  目标太大 往右边寻找
                j++;
            }else{
                return true;
            }

        }
        return false;
    }
}
```

## [剑指 Offer 06. 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)

难度简单164收藏分享切换为英文接收动态反馈

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

**示例 1：**

```
输入：head = [1,3,2]
输出：[2,3,1]
```

### 解题

==方法一==利用栈

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] reversePrint(ListNode head) {
        Stack<Integer> st = new Stack<Integer>();
        // 遍历 入栈
        // 链表不知道长度，用while循环
        while(head != null){
            int temp = head.val;
            st.push(temp);
            head = head.next;
        }
        int len = st.size();
        int[] arr = new int[len];
        for(int i=0;i<len;i++){
            arr[i] = st.pop();
        }
    return arr;
    }
}
```





## [剑指 Offer 66. 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)

### 题目【难度中等】

给定一个数组 `A[0,1,…,n-1]`，请构建一个数组 `B[0,1,…,n-1]`，其中 `B[i]` 的值是数组 `A` 中除了下标 `i` 以外的元素的积, 即 `B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]`。不能使用除法。

**示例:**

```
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
```

**提示：**

- 所有元素乘积之和不会溢出 32 位整数
- `a.length <= 100000`

### 思路

定义一个新数组，第一次遍历存放每个数左边的累乘积（只需将最新的左边一个数*数组上一次的累乘积），然后从后面往前第二次遍历，存放每个数右边的累乘积*左边累乘积对应相乘。

### 代码

```java
class Solution{
    public int[] constructArr(int[] a){
        //测试用例 有个[] 要注意
        if(a.length==0){
            return a;
        }
        
        int[] b = new int[a.length];
        b[0] = 1;
        int tmp = 1;
        for (int i = 1; i < b.length; i++) {
            b[i]  = a[i-1] * b[i-1];
        }

        for (int k=b.length-2; k>=0; k--){
            tmp = tmp*a[k+1];
            b[k] = b[k]*tmp;
        }
        return b;
    }
}
```

> 空间复杂度 O(1) ) 时间复杂度(n)

##

