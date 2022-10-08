import itertools

n=int(input())
A=list(map(int, input().split()))
operator=[]# 연산자 목록 0-3 : +-*/
for i, n in enumerate(list(map(int, input().split()))):
  operator+=[i]*n

min=99999
max=0
res=0

def cal(a, b, op):# 연산자에 따른 계산
  res=a
  if op==0:
    res+=b
  elif op==1:
    res-=b
  elif op==2:
    res=int(res*b)
  elif op==3:
    res=int(res/b)
  return res

for per in itertools.permutations(operator):

  res=A[0]
  for idx, An in enumerate(A[1:]):
    res=cal(res, An, per[idx])
  
  if res<min:
    min=res
  if res>max:
    max=res

print(max)
print(min)