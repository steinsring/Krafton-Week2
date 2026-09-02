class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf

        # 노드 객체
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    


class Solution:
    def is_area_same_value(self, grid, start_row, start_col , n):
        first_value = grid[start_row][start_col]
        for i in range(start_row, start_row + n):
            for j in range(start_col, start_col + n):
                if grid[i][j] != first_value:
                    return False
        return True

    def recursion(self, parent, grid, start_row, start_col, n):

        # 모두 같은 수 일경우 val 확정 후 종료 
        if self.is_area_same_value(grid, start_row, start_col, n):
            if grid[start_row][start_col] == 0:
                parent.val = False
                parent.isLeaf = True
            else:
                parent.val = True
                parent.isLeaf = True
            return
        
        

        mid_row = start_row + n //2 - 1
        mid_col = start_col +  n //2 - 1
        parent.topLeft = Node(0, False, None, None, None, None)
        parent.topRight = Node(0, False, None, None, None, None)
        parent.bottomLeft = Node(0, False, None, None, None, None)
        parent.bottomRight = Node(0, False, None, None, None, None)

        self.recursion(parent.topLeft, grid, start_row, start_col, n // 2)
            
        self.recursion(parent.topRight, grid, start_row, mid_col + 1, n // 2)
            
        self.recursion(parent.bottomLeft, grid, mid_row + 1, start_col, n // 2)
            
        # 영역 안에 다른 수가 있을 경우 재귀
        self.recursion(parent.bottomRight, grid, mid_row + 1, mid_col + 1, n // 2)
            

        
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        # 행렬을 순회하면서 모든값이 같은지 확인하고
        # 값이 같다면 종료
        # 값이 같지 않다면 4개 영역으로 나눈다.

        # 4개의 영역으로 나누었을 때
        # 각 영역마다 값이 같은지 확인
        # 틀린 값만 다시 4개 영역으로 나눈다.
        n = len(grid)
        self.root_node = Node(0, False, None, None, None, None)
        self.recursion(self.root_node, grid, 0, 0, n)

        return self.root_node



        

if __name__ == "__main__":
    a = Solution()

    list1 = [[1,1,0,0],
             [0,0,1,1],
             [1,1,0,0],
             [0,0,1,1]]

    root = a.construct(list1)

    def print_node(node, name="root"):
        if node is None:
            print(f"{name}: None")
            return

        print(
            f"{name}: "
            f"val={node.val}, "
            f"isLeaf={node.isLeaf}"
        )

        print_node(node.topLeft, name + ".topLeft")
        print_node(node.topRight, name + ".topRight")
        print_node(node.bottomLeft, name + ".bottomLeft")
        print_node(node.bottomRight, name + ".bottomRight")

    print_node(root)
    print("---")