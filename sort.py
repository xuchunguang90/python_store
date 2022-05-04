# 冒泡排序
def bubble_sort(array):
    n = len(array)
    # 一共需要n-1次循环，每一个数都要找到没排好序的最大值
    for i in range(n-1):
        # 将没有排好序的数组找到最大值，并一直将最大值换到最顶端
        for j in range(n-i-1):
            # 依次比较，将两者较大的往后放
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == '__main__':
    testList = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort(testList))
