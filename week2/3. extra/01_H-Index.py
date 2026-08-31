class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # 배열을 정렬하고, 순회하며 최소 그 수 이상인 논문의 개수를 찾아라
        # 이때 논문의 개수가 현재 수와 보다 많다면 저장

        citations.sort()
        h_index = 0
        for i in range(len(citations)):
            first = citations.index(citations[i])
            # 둘 중 작은 값을 찾아서
            h = min(len(citations) - first, citations[i])  # citations[i] : 인용된 횟수 // len(ciations) - first : 최소 n번 인용된 문서의 갯수
            # 이전에 기록된 값과 비교해 큰값 찾기
            h_index = max(h_index, h)
            
        return h_index


if __name__ == "__main__":
    a = Solution()

    list1 = [3,0,6,1,5]

    print(a.hIndex(list1))