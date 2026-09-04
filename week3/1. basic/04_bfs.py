"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visited = []
    
    # TODO: 큐 생성 및 시작 정점 추가
    ## 방문한 정점 집합
    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들 확인
    ## 방문하지 않은 정점이면 큐에 추가

    queue = deque() # deque는 무엇을 사용하는가
    queue.append(start)
    is_visitied = set()
    # 원래 가까운지를 판단하는 비용이 있어야하는데 여기는 정점에 저장된 값이 비용이라고 하자.

    while queue:
        # 부모 노드를 방문
        current_vertice = queue.popleft()
        # 이미 방문한 정점이라면 스킵
        if current_vertice in is_visitied:
            continue
        is_visitied.add(current_vertice)   # 방문처리

        # 노드의 자식들(또는 인접 정점들)을 큐에 추가
        # 인접한 v들을 순회하면서 방문했는지 보고 방문하지 않았으면 큐에 추가
        for value in graph[current_vertice]:
            if value in is_visitied:
                continue
            queue.append(value)

        # 결과에 방문한 정점 추가
        visited.append(current_vertice)
    


    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

