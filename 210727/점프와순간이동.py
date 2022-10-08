# 모범 풀이 1
def solution(n):
    return bin(n).count('1')# 2진법 사용한 풀이
    # 2로 나눴을 때 나머지가 1일때만 answer에 더하면 되기 때문

# 모범 풀이 2
def solution2(n):
    answer = 1
    while n > 1:
        answer += n % 2
        n = n // 2
    return answer