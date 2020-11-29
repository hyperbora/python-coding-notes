def sort(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


if __name__ == "__main__":
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(sort(arr))
