n, k, i=map(int, input().split()+[0])
while(n>1):
  i+=1 # 반복 횟수 +1
  n=n-1 if n%k else n/k # 나누어떨어지면 나누고, 아니면 -1 하기
print(i)