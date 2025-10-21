def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(n):  # ❌ Should start from gap
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

print(shell_sort([12, 34, 54, 2, 3]))  # Expected [2, 3, 12, 34, 54]
