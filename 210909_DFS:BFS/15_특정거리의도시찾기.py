n, m, k, x=map(int, input().split())
lst=[list(map(int,input().split())) for _ in range(m)]

inf=99999
distance=[inf]*n
distance[x-1]=0
check=True

while check:
  check=False
  for x, y in lst:
    if distance[y-1]>1+distance[x-1]:
      distance[y-1] = 1+distance[x-1]
      check=True

if distance.count(k)==0:
  print(-1)
else : 
  for i, d in enumerate(distance):
    if d==k:
      print(i+1)