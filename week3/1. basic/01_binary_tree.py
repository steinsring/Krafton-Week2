"""
[이진 트리 - Binary Tree 기본]

문제 설명:
- 이진 트리의 기본 구조를 구현합니다.
- 각 노드는 최대 2개의 자식(왼쪽, 오른쪽)을 가집니다.
- 전위, 중위, 후위 순회를 구현합니다.
- 각 노드가 최대 2개의 자식 노드(왼쪽, 오른쪽)를 가질 수 있는 트리 구조.

입력:
- 트리 노드들

출력:
- 전위 순회: 루트 → 왼쪽 → 오른쪽
- 중위 순회: 왼쪽 → 루트 → 오른쪽
- 후위 순회: 왼쪽 → 오른쪽 → 루트

예제:
트리 구조:
      1
     / \
    2   3
   / \
  4   5

전위: [1, 2, 4, 5, 3]
중위: [4, 2, 5, 1, 3]
후위: [4, 5, 2, 3, 1]

힌트:
- 재귀로 간단히 구현 가능
- 순회 순서만 다름
"""

class TreeNode:
    """이진 트리 노드"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def extract_value(result: list, values : list):
    for i in values:
        result.append(i)

def preorder(root):
    """전위 순회: 루트 → 왼쪽 → 오른쪽"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    # TODO: 루트 값 추가
    # TODO: 왼쪽 서브트리 순회
    # TODO: 오른쪽 서브트리 순회
    
    # root가 없으면 빈 리스트
    if root == None:
        return []

    # 루트값을 결과에 추가 및 왼 -> 오 순서로 재귀
    result.append(root.value)
    extract_value(result, preorder(root.left))
    extract_value(result, preorder(root.right))

    return result

def inorder(root):
    """중위 순회: 왼쪽 → 루트 → 오른쪽"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    # TODO: 왼쪽 서브트리 순회
    # TODO: 루트 값 추가
    # TODO: 오른쪽 서브트리 순회

    if root == None:
        return []

    extract_value(result, inorder(root.left))
    result.append(root.value)
    extract_value(result, inorder(root.right))

    return result

def postorder(root):
    """후위 순회: 왼쪽 → 오른쪽 → 루트"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    # TODO: 왼쪽 서브트리 순회
    # TODO: 오른쪽 서브트리 순회
    # TODO: 루트 값 추가

    if root == None:
        return []

    extract_value(result, postorder(root.left))
    extract_value(result, postorder(root.right))
    result.append(root.value)
    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 트리 생성:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("=== 이진 트리 순회 ===")
    print(f"전위 순회: {preorder(root)}")
    print(f"중위 순회: {inorder(root)}")
    print(f"후위 순회: {postorder(root)}")

