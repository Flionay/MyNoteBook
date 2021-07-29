# 单向链表

## Node理解

# 链表

`Node` 对象内部有`value` 和 `next`

![img](https://cdn.jsdelivr.net/gh/Flionay/pic_bed@master/Upic/202107/QScub5.png)

与arraylist很多接口相同，add remove clear等；

但是不能用继承，它们两个没有什么可以抽取到父类的公共代码。

但是可以用接口，只声明公共接口，不实现。

Node为单独类，里面保存值和下一个node的引用。

```java
public class Test {
    public static void main(String[] args) {
        // 创建了三个Node
        ListNode list1 = new ListNode(1);
        ListNode list2 = new ListNode(2);
        ListNode list3 = new ListNode(3);

        // 将他们串起来
        list1.next = list2; // 就相当于在类里面的 ListNode next = new  ListNode(2);
        list2.next = list3;

        // 输出一下
        System.out.println(list1.next.next.val); //3

    }
}

class ListNode{
    int val;
    ListNode next; // 声明next变量为ListNode 用的时候再给它赋值 这是一个引用 类似指针
    public ListNode(int val){
        this.val = val;
    }
}
```

![img](https://cdn.jsdelivr.net/gh/flionay/pic_bed//PicGo/20210715135226.png)

## 实现链表主要接口

```java
package com.ay.linkedlist;

public interface List<E> {
    void clear();
    int size();
    boolean isEmpty();
    void add(int index,E element);
    boolean contains(E element);
    void add(E element);
    E get(int index);
    E remove(int index);
    E set(int index,E element);
    int indexOf(E element);
}

```



```java
package com.ay.linkedlist;

public class LinkedList<E> implements List<E>{
    private int size;

    //只用在Linkedlist 定义为内部类
    private Node<E> first;

    private int ELEMENT_NOT_FOUND=-1;

    @Override
    public void clear() {
        first=null;
        size = 0;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size==0;
    }

    //
    @Override
    public void add(int index, E element) {
        Node<E> nodes = new Node<>(element);
        if(index == 0){
            first = new Node<>(element,first);
        }else{
            nodes.next = node(index-1).next;
            node(index-1).next = nodes;
//             Node<E> prev = node(index-1);
//             prev.next = new Node<>(element,prev.next);

        }
        size ++;
    }


    @Override
    public boolean contains(E element) {

        return indexOf(element)!=ELEMENT_NOT_FOUND;
    }


    @Override
    public void add(E element) {
        add(size,element);
    }

    @Override
    public E get(int index) {
        Node<E> nodes = first;
        for (int i = 0; i < index; i++) {
            nodes = nodes.next;
        }
        return nodes.element;
    }

    @Override
    public E remove(int index) {
        if(index==0){
            first = node(index+1);
        }else{
            node(index-1).next = node(index+1);
        }
        size--;
        return null;
    }


    // 相当于改动嘛
    @Override
    public E set(int index, E element) {
        E old = node(index).element;
        node(index).element = element;

        return old;
    }

    // 获取指定元素的index
    @Override
    public int indexOf(E element) {
        Node<E> nodes = first;
        for (int i = 0; i < size; i++) {
            nodes = nodes.next;
            if(nodes.element==element){
                return i;
            }
        }
        return ELEMENT_NOT_FOUND;
    }

    public String toString(){
        Node<E> nodes = first;
        StringBuilder string = new StringBuilder();
        string.append("Size: ").append(size).append(" [");
        while(nodes!=null){
            string.append(nodes.element).append(",");
            nodes = nodes.next;
        }
        string.append("]");
        return string.toString();

    }

    // 定义一个函数返回对应index的node对象
    private Node<E> node(int index){
        Node<E> nodes = first;
        for (int i = 0; i < index; i++) {
            nodes = nodes.next;
        }
        return nodes;
    }

    // 注意返回对象 跟返回对象元素
    private static class Node<E>{
        // 内部类可以省略public 或 private
        E element;
        Node<E> next;

        //构造方法
        public Node(E element){
            this.element = element;
        }

        public Node(E element,Node<E> next){
            this.element = element;
            this.next = next;
        }
    }
}

```

测试类

```java
package com.ay.linkedlist;
public class Main {
    public static void main(String[] args) {
        List<Integer> list1 = new LinkedList<Integer>();
        list1.add(10);
        list1.add(20);
        list1.add(30);
        list1.add(40);
        list1.remove(2);

        System.out.println(list1);

        list1.add(3,50);
        list1.set(2,70);
        System.out.println(list1);
        System.out.println(list1.get(3));

    }
}
```

## 练习

[237. 删除链表中的节点 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/)

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
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
```

> 用下一个节点的值覆盖此节点的值，然后就出现了两个相同值的节点，把此节点指向下下个节点就可以了。

[141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)

> 快慢指针，快指针走两步，慢指针走一步，如果有环肯定是相遇的。

```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head.next==null) return false;
        ListNode fast = head.next;
        ListNode low = head;
        while(fast != null && fast.next!=null){
            fast = fast.next.next;
            low = low.next;
            if(low == fast){
                return true;
            }
        }
        return false;
    }
}
```

# 双向链表

