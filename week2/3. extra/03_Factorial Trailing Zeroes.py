class Solution:
    def trailingZeroes(self, n: int) -> int:
        pass

    # 뒤에 붙는 0은 팩토리얼 안에 5의 개수와 같다.
    # 0이 만들어지려면 5 * 짝수일 때 만들어지는데, 짝수는 이미 충분하니 5의 개수를 세면 된다.
    # 팩토리얼을 계산하지 않고, 계산식에서 5의 개수를 세자
        if n < 5:
            return 0

        count = 0
        for i in range(5, n + 1, 5):
            while i > 0 and i % 5 == 0 :
                i = i // 5
                count += 1

        return count


if __name__ == "__main__":
    a = Solution()

    # list1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # s = "ABCCED"
    print(a.trailingZeroes(50))