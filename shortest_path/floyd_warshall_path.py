import sys
INF = sys.maxsize


def floyd_warshall(graph, n):
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


def _mock_data():
    inp = """\
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2"""
    for line in inp.split(sep='\n'):
        yield line


if __name__ == "__main__":
    g = _mock_data()

    def _mock_input():
        return next(g)

    input = _mock_input

    n = int(input())
    m = int(input())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로 가는 비용은 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 테스트 데이터 입력
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    floyd_warshall(graph, n)

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                print("-", end=" ")
            else:
                print(graph[a][b], end=" ")
        print()
