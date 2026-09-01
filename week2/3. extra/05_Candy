class Solution:
    def candy(self, ratings: List[int]) -> int:

        # 왼쪽부터 순차적으로 현재값의 왼쪽만 보면서 계산
        # 반대도 독같이
        # 그렇게 만들어진 두 배열중, 양쪽을 비교하면서 조건에 맞는 값만 선택
        # 최소값 지정

        left_candy = [1 for _ in ratings]
        right_candy = [1 for _ in ratings]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left_candy[i] = left_candy[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_candy[i] = right_candy[i + 1] + 1

        candy = [1 for _ in ratings]
        # candy[0] = right_candy[0]
        # candy[len(candy) - 1] = left_candy[len(candy) - 1]

        for i in range( len(candy)):
            candy[i] = max( left_candy[i] , right_candy[i])

        total = 0
        for c in candy:
            total += c
        return total
                
            
                

        


if __name__ == "__main__":
    a = Solution()

    list1 =[1,2,2]
    # s = "ABCCED"
    print(a.candy(list1))