def merge(arr, low, mid, high):
    temp = []
    l, h = low, mid

    while l < mid and h < high:
        if arr[l] < arr[h]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[h])
            h += 1

    while l < mid:
        temp.append(arr[l])
        l += 1
    while h < high:
        temp.append(arr[h])
        h += 1

    for i in range(low, high):
        arr[i] = temp[i - low]


def merge_sort(arr, low, high):
    if high - low < 2:
        return
    mid = low + (high - low) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid, high)
    merge(arr, low, mid, high)


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    merge_sort(arr, 0, len(arr))
    print(arr)
    arr = [1, 5, 4, 3, 2]
    merge_sort(arr, 0, len(arr))
    print(arr)
