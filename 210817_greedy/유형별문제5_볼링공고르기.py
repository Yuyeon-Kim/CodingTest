n, m=map(int, input().split())
nums=list(map(int, input().split()))
res=0
for iidx, i in enumerate(nums[:-1]):
  for j in nums[iidx+1:]:#i 제외한 i 뒤의 글자들
    if i!=j:#i와 같지 않으면 한 쌍을 만들 수 있음
      res+=1
print(res)