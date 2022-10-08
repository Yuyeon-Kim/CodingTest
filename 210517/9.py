import math

def solution(brown, yellow):
    answer = []

    
    #옐로우의 세로 찾기
    for i in range(1, math.ceil(math.sqrt(yellow)+1)):#루트 값보다 같거나 작은 정수까지 반복
        if yellow%i==0:#옐로우가 i로 나누어떨어지면, 
            #브라운이 옐로우의 (가로+세로+2)*2 인지 보자.
            if brown==(i+yellow//i+2)*2:
                answer=[yellow//i+2, i+2]
                break
    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(10, 2))