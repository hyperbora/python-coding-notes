from collections import Counter


def sort(arr):
    """
    계수정렬
    모든 데이터의 개수를 세어서 별도의 리스트나 딕셔너리에 저장 후
    해당 리스트(혹은 딕셔너리)에서 저장된 개수만큼 출력(혹은 append)
    하면 정렬이 된다.
    주어진 리스트의 데이터 범위가 한정적인때만 속도를 낼 수 있다.
    """
    counter = Counter(arr)
    _max = max(arr)
    rst = []
    for i in range(len(arr)):
        _cnt = counter.get(i)
        if _cnt:
            for _ in range(_cnt):
                rst.append(i)
    return rst


if __name__ == "__main__":
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    print(sort(arr))
