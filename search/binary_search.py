def search(array, target, start, end):
    if start > end:
        return None
    mid = start + (end - start) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return search(array, target, start, mid - 1)
    else:
        return search(array, target, mid + 1, end)


def search_repeat(array, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(search(arr, 5, 0, len(arr) - 1))
    print(search_repeat(arr, 5, 0, len(arr) - 1))
