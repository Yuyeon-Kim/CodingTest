# 1. 모든 0을 1로 만든다
# 2. 모든 1을 0으로 만든다
# 둘 중 더 빠른 것 선택

nums=list(input().replace("01", "0 1").replace("10", "1 0").split())# 0끼리 묶고, 1끼리 묶음
res=[0,0] # 0으로 이루어진 문자열 수, 1로 이루어진 문자열 수
for num in nums:
  res[num.find("1")+1]+=1 # 0으로 이루어진 문자열일때는 res[0], 1로 이루어진 문자열일때는 res[1]에 +1
print(min(res)) # 더 작은 값 선택