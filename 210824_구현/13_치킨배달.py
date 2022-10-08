from itertools import combinations

# 입력
m, k = map(int, input().split()) #마을 넓이, 남을 치킨집의 수
board=[list(map(int, input().split())) for _ in range(m)]
buildings=[[],[],[]] # 아무것도 없는 곳, 집, 치킨집
for i in range(m):
  for j in range(m):
    buildings[board[i][j]].append([i,j])

# 계산
res=200000 # 큰 수
# 치킨집 남는 모든 조합에 대해 for문 돌리며 마을의 치킨거리의 최솟값 구함
for reduced_chickens in list(combinations(buildings[2], k)):
  mgt=0 # 마을의 치킨거리
  for house in buildings[1]: # 모든 집에 대해 치킨거리의 최솟값 구함
    ht=20000 # 큰 수
    for r_c in reduced_chickens: # 각각의 치킨집에 대해 치킨거리 구함
      ht=min(ht, abs(house[0]-r_c[0])+abs(house[1]-r_c[1])) # 작은 값으로 업데이트
    mgt+=ht # 마을의 치킨거리의 합에 더해줌
  res=min(res, mgt) # 작은 값으로 업데이트

print(res)