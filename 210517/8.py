import itertools

def isDecimal(number):#소수이면 1 출력 아니면 0 출력
    if number<=1:
      return False
    for i in range(2, number):
        if number%i==0:
            return False
    else:
        return True

def solution(numbers):
    answer = 0
    temp=[]
    all=[]
    for i in range(1, len(numbers)+1):
        temp=list(itertools.permutations(numbers, i))
        for j in range(len(temp)):
          all+=[int(''.join(map(str, temp[j])))]
    print(all)
    all=list(set(all))#중복 값 제거
    print(all)
    
    for i in all:
        if isDecimal(i):
            answer+=1

    return answer


print(solution("17"))
print(solution("011"))
print(solution("17"))