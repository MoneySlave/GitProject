def bubble_sort(arr):
    n = len(arr)
    for i in range(n)
        #每次循环将未排序部分最大值移动到末尾
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
