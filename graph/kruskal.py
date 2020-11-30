"""
신장 트리(Spanning Tree) : 하나의 그래프가 있을 때 모든 노드를 포함하면서
사이클이 존재하지 않는 부분 그래프를 의미
모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는 다는 조건이 필요

1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    (1) 사이클이 발생하지 않는 경우 최소 신장 트리엥 포함
    (2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
3. 모든 간성에 대해 2번 과정을 반복
"""


def _mock_data():
    inp = """\
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25"""
    for line in inp.split(sep='\n'):
        yield line


def find_parent(parent, x):
    """
    특정 원소가 속한 집합 찾기
    """
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    """
    두 원소가 속한 집합 합치기
    """
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def krustal(edges, parent):
    # 간선을 비용순서대로 정렬
    edges.sort()

    result = 0
    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않으면 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    print(result)


if __name__ == "__main__":
    g = _mock_data()

    def _mock_input():
        return next(g)

    input = _mock_input

    v, e = map(int, input().split())
    parent = [0] * (v + 1)

    edges = []
    result = 0

    # 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i

    # 간선 정보 입력
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    krustal(edges, parent)
