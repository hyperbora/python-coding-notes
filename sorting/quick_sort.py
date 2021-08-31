import unittest


def quicksort_pivot_first(arr, start, end):
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
    quicksort_pivot_first(arr, start, right - 1)
    quicksort_pivot_first(arr, right + 1, end)


def quicksort_pivot_last(arr, lo, hi):
    """
    피벗(Pivot)이라는 개념을 통해 피벗보다 작으면 왼쪽, 크면 오른쪽으로 파티셔닝하면서 쪼개 나간다.
    여기서 피벗은 맨 오른쪽 값을 기준으로 하며, 이를 기준으로 2개의 포인터가 이동해서 
    오른쪽 포인터의 값이 피벗보다 작다면 서로 스왑하는 형태로 진행된다.

    오른쪽 right 포인터가 이동하면서 피벗의 값이 오른쪽 포인터 값보다 더 클 때, 왼쪽과 오른쪽의 스왑이 진행된다.
    스왑 이후에는 왼쪽 left 포인터가 함께 이동한다. 오른쪽 포인터가 끝에 도달하면 피벗 미만인 값은 왼쪽으로
    피벗 이상인 값은 오른쪽에 위치하게 된다. 그리고 왼쪽 포인터의 위치로 피벗 아이템이 이동한다.
    결과적으로 피벗값을 기준으로 큰 값을 오른쪽으로 분할되고, 피벗이 그 중앙으로 이동하는 모습을 확인 할 수 있다.
    이렇게 계속 분할하면서 정복을 진행하여 코드 기준으로 lo < hi를 만족하지 않을 때까지,
    즉 서로 위치가 역전할 때까지 계속 재귀로 반복되면서 정렬이 완료된다.
    """

    def partition(lo, hi):
        pivot = arr[hi]
        left = lo
        for right in range(lo, hi):
            if arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
        arr[left], arr[hi] = arr[hi], arr[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort_pivot_last(arr, lo, pivot - 1)
        quicksort_pivot_last(arr, pivot + 1, hi)


class TestSolution(unittest.TestCase):
    def test_sort(self):
        arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
        new_arr = list(arr)
        quicksort_pivot_first(new_arr, 0, len(new_arr) - 1)
        self.assertListEqual(new_arr, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        new_arr = list(arr)
        quicksort_pivot_last(new_arr, 0, len(new_arr) - 1)
        self.assertListEqual(new_arr, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
