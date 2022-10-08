n=int(input())
fears=sorted(list(map(int, input().split()))) # 오름차순 정렬
res=0 # 그룹 수
people=0 # 그룹 내 사람 수
for fear in fears:
  people+=1 # 그룹 내 사람 수 +1
  if people>=fear: # 사람 수가 공포도 이상이면 팀 구성 가능
    res+=1 # 팀 개수 +=1
    people=0 # 그룹 내 사람 수 초기화
print(res)