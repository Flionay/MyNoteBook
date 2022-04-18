# ArrayList

```java
package com.ay.arraylist;

public class ArrayList<E> {
    public int size;
    private E[] elements; //所有的元素
    private static final int DEFAULT_CAPACITY = 10;
    private static final int ELEMENT_NOT_FOUND = -1;

    //构造方法
    public ArrayList(int capaticy){
        if (capaticy<DEFAULT_CAPACITY){
            capaticy = DEFAULT_CAPACITY;
        }else{
            capaticy = capaticy;
        }
        elements = (E[]) new Object[capaticy];
    }

    public void rangeCheck(int index){
        if (index<0 || index>= size){
            throw new IndexOutOfBoundsException("Index： "+index + "But Size :"+size);
        };
    }

    public void rangeCheckForAdd(int index){
        if (index<0 || index> size){
            throw new IndexOutOfBoundsException("Index： "+index + "But Size :"+size);
        };
    }


    public void add(E element){

        add(size,element);
    }

    public void add(int index,E element){

        rangeCheckForAdd(index);
        ensureCapacity(size+1);
        for (int i = size-1; i >= index ; i--) {
            elements[i+1] = elements[i];
        }
        elements[index] = element;
        size ++;
    }

    public ArrayList(){
        //elements = new int[DEFAULT_CAPACITY];
        this(DEFAULT_CAPACITY); //调用有参数的构造方法
    }

    public boolean isEmpty(){
        return size==0;
    }

    public E get(int index){
        rangeCheck(index);
        return elements[index];
    }

    public E set(int index,E element){
        rangeCheck(index);
        E old = elements[index];
        elements[index] = element;
        return old;
    }

    /**
    * 查看元素索引
    * @param element
    * @return index
     */
    public int indexOf(E element){
        for (int i = 0; i < size; i++) {
            if (elements[i]==element) return i;
        }
        return ELEMENT_NOT_FOUND;
    }

    /**
     * 是否包含某个元素
     * @param element
     * @return boolean
     */
    public boolean contains(E element){
        return indexOf(element) != ELEMENT_NOT_FOUND;
    }

    // 清楚所有元素

    /**
     * 控制size为0即可，无需清空
     */
    public void clear(){
        for (int i = 0; i < size; i++) {
            elements[i] = null;
        }
        size = 0;
    }

    // java中 打印对象会默认调用 对象.toString() 重写该方法
    public String toString(){
        // 拼接字符串
        StringBuilder string = new StringBuilder();
        string.append("size=").append(size).append(" [");
        for (int i = 0; i < size; i++) {
            string.append(elements[i]);
            if(i!=size-1){
                string.append(",");
            }
        }
        string.append("]");
        return string.toString();
    }

    public E remove(int index){
        rangeCheck(index);
//        for (int i = 0; i < size; i++) {
//            if (i>index){
//                elements[i-1] = elements[i];
//            }
//        }
        E old = elements[index];
        for (int i = index+1; i <size ; i++) {
            elements[i-1] = elements[i];
        }
        size --;
        elements[size]=null;
        return old;
    }
    /**
     * 保证要有capacity的容量
     * @param capacity
     */
    private void ensureCapacity(int capacity){
        int oldCapacity = elements.length;
        if (oldCapacity>=capacity){
            return;
        }
        // 新容量为旧容量的1.5倍
        int newCapacity = oldCapacity + (oldCapacity>>1);
        E[] newElements = (E[]) new Object[newCapacity];
        for (int i =0;i<size;i++){
            newElements[i] = elements[i];
        }
        elements = newElements;
        System.out.println("扩容");
    }



}

```

测试类

```java
package com.ay.arraylist;

public class Main {
    public static void main(String[] args) {
        Main.test2();
    }

    // 测试person对象 添加到数组
    public static void test2(){
        Person xiaoming = new Person("xiaoming",14);
        Person xiaohong = new Person("xiaohong",30);
//        Person xiaohong = new Person("xiaohong",30);

        ArrayList<Person> arrayList = new ArrayList<>();
        arrayList.add(xiaoming);
        arrayList.add(xiaohong);
        arrayList.add(xiaohong);
        arrayList.add(xiaohong);
        System.out.println(arrayList);
        arrayList.clear();
        System.out.println(arrayList);
        //提醒jvm去做垃圾回收
        System.gc();
    }

    public static void test1(){
        ArrayList<Integer> arrayList = new ArrayList<>();

        arrayList.add(100);
        arrayList.add(10);
        arrayList.add(200);
        arrayList.add(300);

        for (int i=0;i<30;i++){
            arrayList.add(i);
        }

        System.out.println(arrayList);


    }
}

```

