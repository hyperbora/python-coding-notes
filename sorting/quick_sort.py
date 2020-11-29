def sort(arr, start, end):
    # 데이터가 한개면 종료
    if start >= end:
        return
    # 피벗은 첫번째 데이터 선택
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때 까지 왼쪽 포인터를 오른쪽으로 이동
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지 오른쪽 포인터를 윈쪽으로 이동
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        # 포인터가 엇갈리면 작은 데이터와 피벗을 교체
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않으면 작은 데이터와 큰 데이터 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]
    sort(arr, start, right - 1)
    sort(arr, right + 1, end)


if __name__ == "__main__":
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    sort(arr, 0, len(arr) - 1)
    print(arr)
