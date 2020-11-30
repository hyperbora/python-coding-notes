"""
다익스트라 알고리즘
    - 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 찾는 알고리즘.
    - 음의 간선이 없을 때 정상 동작
        1. 출발 노드를 설정한다.
        2. 최단 거리 테이블을 초기화한다.
        3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
        4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
        5. 3번과 4번을 반복한다.
"""
import heapq
import sys
INF = sys.maxsize


def dijkstra(graph, start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


if __name__ == "__main__":
    graph = [
        [],
        [(2, 2), (3, 5), (4, 1)],
        [(3, 3), (4, 2)],
        [(2, 3), (6, 5)],
        [(3, 3), (5, 1)],
        [(3, 1), (6, 2)],
        []
    ]
    distance = [INF] * len(graph)
    start = 1
    dijkstra(graph, start, distance)
    print(distance[1:])
