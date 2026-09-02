class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a

        return self.gcd(b, a % b)

    def maxPoints(self, points: List[List[int]]) -> int:
        pass

        # 직선은 모두 1차 방정식 y=ax + b의 형태이다.
        # 이때 x,y값을 알고 있고 대입했을 때, (a, b)의 값이 같다면 같은 직선이다.
        # n^2번 해서 결국 모든 기울기를 구해야한다

        slope = {}

        max_points = 0

        if len(points) == 1:
            max_points = 1

        # 각 점끼리 모든 기울기 구하기
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]

                

                # 수직, 수평선
                if dx == 0 and dy != 0:
                    key = (0, 1, points[i][0])
                    slope.setdefault(key, set()).add(tuple(points[i])) # 좌표값중 중복을 제거. 그리고 set은 list를 넣을 수 없기에 tuple로 변환
                    slope[key].add(tuple(points[j]))
                    continue
                elif dy == 0 and dx != 0:
                    key = (1, 0, points[i][1])
                    slope.setdefault(key, set()).add(tuple(points[i])) # 좌표값중 중복을 제거. 그리고 set은 list를 넣을 수 없기에 tuple로 변환
                    slope[key].add(tuple(points[j]))
                    continue

                b = points[i][1] - (dy/dx) * points[i][0]

                # 기울기 절대값으로 통일
                if dx < 0 and dy < 0:
                    dx *= -1
                    dy *= -1

                g = self.gcd(dx, dy)
                key = (dx // g, dy // g, b)
                slope.setdefault(key, set()).add(tuple(points[i])) # 좌표값중 중복을 제거. 그리고 set은 list를 넣을 수 없기에 tuple로 변환
                slope[key].add(tuple(points[j]))                    # 중복되지 않은 좌표값들을 set으로 저장해 이후 개수를 센다

        for dic in slope.values():
            if len(dic) > max_points:
                max_points = len(dic)

        return max_points

            
                

if __name__ == "__main__":
    a = Solution()

    list1 =[[0,1],[0,2],[2,2],[1,0],[2,0]]
    # s = "ABCCED"
    print(a.maxPoints(list1))