from __future__ import annotations
from typing import Any, Type

class Node:
    # BST 노드
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        # constructor
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    # BST

    def __init__(self):
        # constructor
        self.root = None

    def search(self, key: Any) -> Any:
        # 키가 key인 노드를 검색
        node = self.root
        while node is not None:     # node가 없을때까지
                
            if key == node.key:     # key와 p의 키가 같으면 성공
                return node.value
            elif key < node.key:    # key가 작으면 왼쪽에서 검색
                node = node.left
            else:
                node = node.right   # key가 크면 오른쪽에서 검색

        return None                 # 검색 실패

    def add_node(self, node: Node, key: Any, value: Any) -> None:
        # node를 루트로 하는 서브트리에 {key : value}인 노드 삽입

        # key가 이미 존재하는 경우
        if key == node.key:
            return False
        # 왼쪽 서브트리로
        if key < node.key:
            # 왼쪽 자식이 없으면 노드 추가
            if node.left is None:
                node.left = Node(key, value, None, None)
            else:
                self.add_node(node.left, key, value)

        # 오른쪽 서브트리로
        if key > node.key:
            # 오른쪽 자식이 없으면 노드 추가
            if node.right is None:
                node.right = Node(key, value, None, None)
            else:
                self.add_node(node.right, key, value)
                
        return True

    def add(self, key: Any, value: Any) -> bool:
        # {key : value}인 노드 삽입

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return self.add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        # {key} 노드 삭제
        current_node = self.root
        parent = None
        is_left_child = True    # 현재 노드가 부모의 왼쪽 자식인지 판단

        while True:
            # 더이상 진행할 수 없는 경우
            if current_node is None:
                return False

            # 키를 찾은경우
            if key == current_node.key:
                break
            # 못찾은 경우
            else:
                # 현재 노드를 부모로 하고 키에 크기에 따라 왼쪽 또는 오른쪽을 탐색
                parent = current_node
                if key < current_node.key:
                    is_left_child = True
                    current_node = current_node.left
                else:
                    is_left_child = False
                    current_node = current_node.right

        # 왼쪽에만 자식이 없는경우 or 둘다 없는 경우
        if current_node.left is None:
            # 루트 노드인 경우 오른쪽 자식을 루트로
            if current_node is self.root:
                self.root = current_node.right
            # 현재 노드가 부모의 왼쪽 자식이므로 현재 노드의 오른쪽 자식을 부모 왼쪽자식으로 연결
            elif is_left_child:
                parent.left = current_node.right    # 자식이 둘다없는경우 둘다 None
            # 아니면 부모의 오른쪽 자식으로 연결
            else:
                parent.right = current_node.right
        # 오른쪽에만 자식이 없는 경우
        elif current_node.right is None:
            # 루트 노드인경우 현재 노드의 왼쪽 자식을 루트로
            if current_node is self.root:
                self.root = current_node.left
            # 현재 노드가 부모의 왼쪽 자식이므로 현재 노드의 왼쪽 자식을 부모 왼쪽으로 연결
            elif is_left_child:
                parent.left = current_node.left
            # 아니면 부모의 오른쪽 자식으로 연결
            else:
                parent.right = current_node.left
        # 자식 노드가 두개인 경우 삭제
        else:
            left_biggest_node_parent = current_node        # 현재 노드의 위치를 부모로(찾은 노드를 현재노드의 위치로 옮겨야함)
            left_biggest_node = current_node.left    # subtree : 왼쪽 서브트리의 루트
            is_left_child = True                # 왼쪽 자식이 있으므로

            # 오른쪽 자식이 없는 노드(= 왼쪽 서브트리에서 가장 큰 노드)
            while left_biggest_node.right is not None:
                left_biggest_node_parent = left_biggest_node
                left_biggest_node = left_biggest_node.right   # 서브트리의 오른쪽만 탐색
                is_left_child = False

            # 찾은 가장 큰 노드(t)를 현재 노드에 값과 키를 넣고
            current_node.key = left_biggest_node.key
            current_node.value = left_biggest_node.value
            # t가 부모의 왼쪽 자식인 경우 t의 자식을 부모에 왼쪽에 연결 
            if is_left_child:
                left_biggest_node_parent.left = left_biggest_node.left
            # 아니면 t의 자식을 부모의 오른쪽에 연결
            else:
                left_biggest_node_parent.right = left_biggest_node.left
        return True

    def print_subtree(self, node: Node):
        if node is not None:
            self.print_subtree(node.left)
            print(f'{node.key} {node.value}')
            self.print_subtree(node.right)


    def dump(self):
        # 모든 노드를 키의 오름차순으로 출력
       self.print_subtree(self.root)


def main():
    """빈 BST에서 시작해 삽입과 삭제 과정을 트리 모양으로 출력한다."""
    tree = BinarySearchTree()

    def tree_height(node):
        if node is None:
            return 0
        return 1 + max(tree_height(node.left), tree_height(node.right))

    def show_tree():
        """루트가 위, 왼쪽/오른쪽 자식이 아래에 나란히 보이도록 출력한다."""
        if tree.root is None:
            print('(빈 트리)')
            return

        height = tree_height(tree.root)
        nodes = [tree.root]
        cell_width = 14

        for depth in range(height):
            slots = 2 ** depth
            gap = max(1, (2 ** (height - depth - 1)) * cell_width)
            line = []

            for _ in range(slots):
                node = nodes.pop(0) if nodes else None
                if node is None:
                    line.append('')
                    nodes.extend([None, None])
                else:
                    line.append(f'{node.key}({node.value})')
                    nodes.extend([node.left, node.right])

            print(''.join(label.center(gap) for label in line).rstrip())

    def print_state(message):
        print(f'\n[{message}]')
        show_tree()

    # 처음에는 루트가 없는 빈 트리이다.
    print_state('시작')

    # 한 노드씩 삽입되는 과정을 확인한다.
    for key, value in [
        (50, 'root'),
        (30, 'left'), (70, 'right'),
        (20, 'left-left'), (40, 'left-right'),
        (60, 'right-left'), (80, 'right-right'),
    ]:
        tree.add(key, value)
        print_state(f'삽입: {key}({value})')

    # 리프 노드, 자식이 하나인 노드, 자식이 둘인 루트를 차례로 삭제한다.
    for key in (20, 30, 50):
        tree.remove(key)
        print_state(f'삭제: {key}')


if __name__ == '__main__':
    main()
