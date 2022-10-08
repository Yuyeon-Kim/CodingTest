def solution(n, t, m, p):
    answer = ''
    al=''
    lst=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    x=(t-1)*m+p
    i=0
    #구할 자릿수 = (미리 구할 숫자의 개수-1) * 게임에 참가하는 인원 + 튜브의 순서=(t-1)*m+p
    #ex 구할 자릿수 = (1-1)*3+2
    # 구할 자릿수 = (2-1)*3+2
    
    #튜브가 말할 자릿수: p+m*(바퀴 수 -1)
    
    while len(al)<=x:
        #i를 n 진수로 바꾸기
        div=i
        if div==0:
          njin='0'
        else:
          njin=''
        while 1:
          if div==0:
            break
          njin=lst[div%n]+njin
          div//=n
        print(njin)
        al+=njin
        i+=1
        
    for i in range(t):
        answer=answer+al[p+m*i-1]
    
    return answer

print()
print(solution(2, 4, 2, 1))
print()
print(solution(16, 16, 2, 1))
print()
print(solution(16, 16, 2, 2))
