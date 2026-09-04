"""
[그래프 - 다익스트라 최단경로 (Dijkstra's Shortest Path)]

▣ 문제 배경
- 가중치가 음이 아닌(0 이상) 방향 그래프에서, 한 출발점 'start' 에서 다른 모든 정점까지의
  최단 거리를 구하는 표준 알고리즘입니다.
- 1959년 Edsger W. Dijkstra 가 발표하였으며, 우선순위 큐(min-heap) 와 결합한 구현은
  공지된 표준 기법입니다. 본 지문과 테스트 케이스는 본 학습 자료를 위해
  자체적으로 작성되었습니다.
- 본 학습에서는 `week2/2. advanced/03_priority_queue` 에서 다룬 힙 자료구조를 활용합니다.

▣ 작은 예시
    정점: 0, 1, 2, 3, 4
    방향 간선(u, v, w):
        0 -> 1 (4)
        0 -> 2 (1)
        2 -> 1 (2)
        2 -> 3 (5)
        1 -> 3 (1)
        3 -> 4 (3)

    그림:
              4
        0 --------> 1
        |\         ^|
        | \1     2/ |
        |  \    /   |1
        |   v  /    v
        |    2 ---> 3 ---> 4
        |       5      3

    start = 0 일 때 최단 거리:
        0 -> 0 : 0
        0 -> 1 : 3   (0->2->1: 1+2)
        0 -> 2 : 1
        0 -> 3 : 4   (0->2->1->3: 1+2+1)
        0 -> 4 : 7   (0->2->1->3->4: 1+2+1+3)

▣ 구현할 함수
dijkstra(n: int, edges: list[tuple[int, int, int]], start: int) -> list
  - 정점은 0, 1, ..., n-1 의 정수로 식별됩니다.
  - edges 는 (u, v, w) 형식의 방향 간선들의 리스트 (w >= 0).
  - 반환값은 길이 n 의 리스트 dist 로,
        dist[i] = start 에서 정점 i 까지의 최단 거리,
        도달 불가능하면 float('inf').
  - dist[start] 는 항상 0 이어야 합니다.

▣ 제약
- 0 <= n <= 1000, 간선 수 <= 5000 정도면 충분.
- 0 <= w <= 10000

▣ 힌트 (heapq 사용, O((V+E) log V))
  import heapq
  - dist 를 INF 로 초기화하고 dist[start] = 0
  - 우선순위 큐에 (0, start) 를 push
  - 큐가 빌 때까지:
      (d, u) = heappop
      if d > dist[u]: continue     # 이미 더 짧은 경로로 처리됨
      for v, w in graph[u]:
          if dist[u] + w < dist[v]:
              dist[v] = dist[u] + w
              heappush(pq, (dist[v], v))
"""

import heapq


INF = float('inf')


def dijkstra(n: int, edges: list, start: int) -> list:
    """
    n: 정점 수 (정점 번호 0 ~ n-1)
    edges: (u, v, w) 형식 방향 간선 리스트
    start: 출발 정점
    반환: 길이 n 의 거리 리스트 (도달 불가 = float('inf'))
    """
    # TODO: 인접 리스트 graph 구성 (graph[u] = [(v, w), ...])
    # TODO: dist 를 INF 로 초기화하고 dist[start] = 0
    # TODO: 우선순위 큐(heapq)로 BFS-like 최단경로 탐색
    # TODO: dist 반환
    pass

    # 초기화 : 시작점v의 거리 = 0, v와 직접 연결된 정점들은 edge비용으로, 연결안되면 INF로
    # 선택 : 아직 거리가 확정되지 않은 정점들 중 가장 거리가 짧은 u를 표시
    # 갱신 : 새로 확정된 u를 거져서 가는 것(start -> u + u -> w) < 기존 (start -> w) 인 경우 갱신

    # kruskal prim은? 최소신장트리에 대해서...
    # 지하철 노선도

    # u = 현재 꺼낸 정점
    # v = u와 인접한 다음 정점
    # w = 간선의 가중치

    dist = [INF] * n
    dist[start] = 0
    priority_queue = []    # pq를 쓴 이유?

    # grph 초기화
    graph = {}
    for i in range(n):
        graph.setdefault(i, [])

    for e in edges:
        e1 = (e[1], e[2])
        graph[e[0]].append(e1) 

    heapq.heappush(priority_queue, (0, start))
    while priority_queue:
        d, u = heapq.heappop(priority_queue)    # d : u부터 v까지 가는 비용 / u : 출발 정점
        if d > dist[u]:                         # u -> v 비용이 시작지점부터 u까지 가는 비용보다 크면 스킵
            continue

        for v, w in graph[u]:                   # v : 도착 정점 w : 간선 비용
            if dist[u] + w < dist[v]:           # 기존에 시작지점부터 u까지 가는 비용 + u -> v가는 비용 < 기존 시작지점부터 v까지 가는 비용
                dist[v] = dist[u] + w           # 갱신
                heapq.heappush(priority_queue, (dist[v], v))    # 시작 -> v , 도착점 v

    return dist

    


    


def _format(dist):
    """출력 표기를 위한 헬퍼: float('inf') 는 'INF' 로 보여줌"""
    return [('INF' if x == INF else x) for x in dist]


if __name__ == "__main__":
    print("[테스트 1] 예시 그래프 (5개 정점)")
    n = 5
    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (2, 3, 5),
        (1, 3, 1),
        (3, 4, 3),
    ]
    print(f"  n={n}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 2] 정점 1개")
    print(f"  n=1, edges=[], start=0")
    print(f"  최단 거리: {_format(dijkstra(1, [], 0))}")
    print()

    print("[테스트 3] 도달 불가능한 정점 포함")
    n = 4
    edges = [(0, 1, 5)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 4] 동일한 거리의 두 경로 (둘 다 7)")
    n = 4
    edges = [(0, 1, 3), (1, 3, 4), (0, 2, 5), (2, 3, 2)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 5] 0 가중치 간선 포함")
    n = 3
    edges = [(0, 1, 0), (1, 2, 0), (0, 2, 5)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
