class Solution:
    def backtracking(self, row, col, result, word, board, visited):

        if result == list(word):
            return True

        # 현재 원소를 추가하고 word와 순차 비교
        # 현재까지 맞으면 통과, 틀리면 pop, back
        result.append(board[row][col])
        visited[row][col] = True
        for i in range(len(result)):
            if result[i] != word[i]:
                result.pop()
                visited[row][col] = False
                return
        
        #       상 하 좌 우 시도
        if row > 0 and visited[row - 1][col] == False:
            if self.backtracking(row - 1, col, result, word, board, visited):
                return

        if row < len(board) - 1 and visited[row + 1][col] == False:
            if self.backtracking(row + 1, col, result, word, board, visited):
                return

        if col > 0 and visited[row][col - 1] == False:
            if self.backtracking(row, col - 1, result, word, board, visited):
                return

        if col < len(board[row]) - 1 and visited[row][col + 1] == False:
            if self.backtracking(row, col + 1, result, word, board, visited):
                return

        if result == list(word):
            return True

        result.pop()
        visited[row][col] = False
        return False




    def exist(self, board, word: str) -> bool:
        pass

    # 배열을 순서대로 순회하되, 각 원소마다 상,하,좌,우 백트래킹을 시도하도록 한다.
        result = []
        visited = [
            [ False for _ in row ]
            for row in board
        ]

        for row in range(len(board)):
            for col in range(len(board[0])):
                # 모든 원소에 대해 백트래킹 시도
                
                self.backtracking(row, col, result, word, board, visited)

        print(result)
        if result == list(word):
            return True
        else:
            return False



if __name__ == "__main__":
    a = Solution()

    list1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    s = "ABCCED"
    print(a.exist(list1, s))