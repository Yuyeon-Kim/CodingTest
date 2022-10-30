# https://school.programmers.co.kr/learn/courses/30/lessons/132265

# 문제 정리
# 1. 주어진 배열을 2개로 나눈다(회전은 생각하지 않고 한번만 자르면 되는듯?)
# 2. 나눠진 2개의 배열에는 똑같은 숫자의 종류 개수를 가진다
# 3. 나눠진 배열의 원소 수는 생관하지 않는다. 
# 4. 숫자의 종류가 완전히 똑같지 않아도 된다. "종류 수"만 똑같으면 된다. (ex [1, 3], [2, 4])

# 문제 풀이 아이디어 # 1
# 1. 부르트 포스 사용해서 하나하나 나눈다.
# 2. 같은 값 중복이 안되는 set 이용해서 숫자 종류 수를 구한다.
# 3. 숫자 종류 수가 같으면 answer++
# => 시간초과!

# 문제 풀이 아이디어 # 2
# 위의 아이디어가 시간 초과이므로, 데이터를 저장해 시간을 줄이자 -> 정보 저장 테이블 만들자
# 앞 & 뒤에서부터 개수 세기 리스트 만들고, 그 값이 같으면 answer++
# => 조금 더 나아진 시간초과!

# 문제 풀이 # 3
# 힌트 봄! set을 사용하지 않고 loop 밖에서 개수 세기
# 해시 테이블 사용

def solution1(topping):
    answer = 0
    for i in range(1, len(topping)): # 1~토핑 배열 끝 인덱스
        if len(set(topping[:i])) == len(set(topping[i:])): # 숫자 종류 수 같으면
            answer += 1
    return answer

def solution2(topping):
    answer = 0
    frontCount = []
    backCount = [] # list 숫자 개수, 처음에는 항상 1 넣으려면 [1] 하고, 아래 for문에서 반복개수 바꾸기
    frontSet = set()
    backSet = set() # set 숫자 개수

    for f, b in zip(topping[:-1], reversed(topping)): # 원래 리스트보다 하나 짧게 한다. zip은 짧은 원소에 맞추므로 둘중 하나만 짧게 만들면 된다.
        frontSet.add(f)
        backSet.add(b)
        frontCount.append(len(frontSet))
        backCount.insert(0, len(backSet))
      
    for f, b in zip(frontCount, backCount):
        if f == b:
            answer+=1

    return answer


def solution(topping):
    answer = 0

    lenTopping = len(topping)

    frontHash = [False]*10001 # 원소 수 10000, 인덱스 10000까지 쓰려고 10001개 만듦
    backHash = [False]*10001
    frontCount = [0] * lenTopping
    backCount = [0] * lenTopping
    for i, fb in enumerate(zip(topping[:-1], reversed(topping))):
        if frontHash[fb[0]] == False:
            frontHash[fb[0]] = True
            frontCount[i+1] = frontCount[i] + 1
        else:
            frontCount[i+1] = frontCount[i]

        if backHash[fb[1]] == False:
            backHash[fb[1]] = True
            backCount[lenTopping - i - 2] = backCount[lenTopping - i -1] + 1
        else:
            backCount[lenTopping - i - 2] = backCount[lenTopping - i -1]

    for f, b in zip(frontCount[1:], backCount):
        if f == b:
            answer+=1
    
    return answer

  

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))