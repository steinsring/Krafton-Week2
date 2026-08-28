"""
[배열 - 2차원 배열 회전]

문제 설명:
- N x N 크기의 2차원 배열을 시계방향으로 90도 회전시킵니다.
- 배열의 인덱스 변환 규칙을 이해하는 문제입니다.

입력:
- matrix: N x N 크기의 2차원 리스트

출력:
- 시계방향으로 90도 회전된 2차원 리스트

예제:
입력:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

출력:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

힌트:
- 회전 후 위치: (i, j) -> (j, n-1-i)
- 새로운 배열을 만들어 값을 채워넣으세요
"""

def rotate_matrix_90(matrix):
    """
    2차원 배열을 시계방향으로 90도 회전
    
    Args:
        matrix: N x N 2차원 리스트
    
    Returns:
        회전된 2차원 리스트
    """
    n = len(matrix)
    
    # TODO: n x n 크기의 새로운 배열을 생성하세요 (0으로 초기화)
    pass
        
    # TODO: 원본 배열의 각 요소를 회전된 위치에 배치하세요
    # 힌트: (i, j) 위치의 요소는 회전 후 (j, n-1-i) 위치로 이동
    pass

    # 설계 : 원소가 0인 n x n 크기의 2차원 배열을 만들고, 
    #        모든 원소를 순회하며 rotated[j, n-1-i]위치에 원래 배열의 값을 넣는다.

    # n x n 크기의 0으로 초기화된 배열
    rotated = []

    row = [0] * n
    for i in range(n):
        
        rotated.append(row)     # row가 하나의 객체라서 반복문 안쪽에서 생성해야 함

    i = 0
    j = 0

    # 모든 원소 순회
    for row in matrix:
        for elem in row:
            rotated[j][n-1-i] = elem
            j += 1

        i += 1
        j = 0



    return rotated

def print_matrix(matrix):
    """배열을 보기 좋게 출력하는 헬퍼 함수"""
    for row in matrix:
        print(row)

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 3x3 배열
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("원본 배열:")
    print_matrix(matrix1)
    print("\n회전 후:")
    rotated1 = rotate_matrix_90(matrix1)
    print_matrix(rotated1)
    print()
    
    # 테스트 케이스 2: 4x4 배열
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    print("원본 배열:")
    print_matrix(matrix2)
    print("\n회전 후:")
    rotated2 = rotate_matrix_90(matrix2)
    print_matrix(rotated2)


