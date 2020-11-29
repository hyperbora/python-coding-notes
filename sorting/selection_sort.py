def sort(arr):
    length = len(arr)
    for i in range(length):
        min_i = i
        for j in range(i + 1, length):
            if arr[min_i] > arr[j]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


if __name__ == "__main__":
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(sort(arr))
