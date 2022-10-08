n, k = map(int, input().split())
lst= [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

di=[0,0,-1,1]
dj=[-1,1,0,0]

def num_classification():#번호별로 저장
  global n, k, lst
  num_lst=[[] for _ in range(k+1)]
  for i in  range(n):
    for j in range(n):
      num_lst[lst[i][j]].append((i,j))
  return num_lst

for time in range(s):
  num_lst=num_classification()
  for num, idxs in enumerate(num_lst[1:]):
    for idx in idxs:
      for direction in range(4):
        i=idx[0]+di[direction]
        j=idx[1]+dj[direction]
        if 0<=i<n and 0<=j<n and lst[i][j]==0:
          lst[i][j]=num+1

print(lst[x-1][y-1])