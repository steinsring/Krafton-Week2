"""
[동적 프로그래밍 - 계단 오르기 (상향식 / Bottom-up)]

문제 설명:
- 상향식 DP로 계단을 오르는 방법의 수를 계산합니다.
- 한 번에 1칸 또는 2칸을 오를 수 있습니다.
- n번째 계단까지 오르는 경우의 수를 구합니다.

입력:
- n: 계단의 수

출력:
- n번째 계단까지 오르는 방법의 수

예제:
입력: n = 4
출력: 5
설명: 
  1. 1+1+1+1
  2. 1+1+2
  3. 1+2+1
  4. 2+1+1
  5. 2+2

힌트:
- dp[i] = 계단 i까지 오르는 방법의 수
- dp[i] = dp[i-1] + dp[i-2]
- 작은 문제부터 차례로 계산

DP 문제 풀이 순서:
1. 부분 문제 정의: dp[i]가 무엇인지 정의
2. 점화식 도출: dp[i]를 이전 값으로 표현
3. 초기값 설정: dp[0], dp[1] 등
4. 계산 순서 결정: 상향식 or 하향식
5. 구현 및 검증
"""

def climb_stairs(n, dp = None):
    """
    계단 오르기 (상향식 DP)
    
    Args:
        n: 계단의 수
    
    Returns:
        n번째 계단까지 오르는 방법의 수
    """
    # TODO: 특별한 경우 처리
    # TODO: dp 배열 생성 및 초기화
    # TODO: 작은 문제부터 차례로 계산

    # 상향식과 하향식의 차이는 무엇인가
    # 각각 어디에 응용할 수 있는가
    # 실질적으로 얼마나 줄어드는지 측정할 수 있는가

    if n == 0:
        return 1

    if n == 1:
        return 1

    if dp == None:
        dp = [1, 1]

    if len(dp) > n: # len은 왜 sizeof를 반환하는가 / capacity를 반환할 수 있지 않을까 / c++에서는 벡터에서 이 두개가 중요했다
        return dp[n]
    
    dpn = climb_stairs(n - 1, dp) + climb_stairs(n - 2, dp)
    dp.append(dpn)
    
    return dp[n]

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 계단 오르기 ===")
    for i in range(1, 11):
        result = climb_stairs(i)
        print(f"{i}번 계단: {result}가지")
    print()
    
    # 테스트 케이스 2: 큰 수
    n = 20
    result = climb_stairs(n)
    print(f"{n}번 계단: {result}가지")
    print()
    
    # 계단별 경로 예시
    print("=== 4번 계단의 경로 ===")
    print("1. 1+1+1+1")
    print("2. 1+1+2")
    print("3. 1+2+1")
    print("4. 2+1+1")
    print("5. 2+2")


