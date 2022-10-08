n=int(input()) # 맵의 사이즈

def move(m):
  global n
  if m[2]==0 and m[1]<n-1:
    m[1]+=1
  elif m[2]==1 and m[0]<n-1:
    m[0]+=1
  elif m[2]==2 and m[1]>0:
    m[1]-=1
  elif m[2]==3 and m[0]>0:
    m[0]-=1
  else:
    return [0,0,-1]
  return m

def turn(m):
  if input()=="L": # 왼쪽으로 90도 회전
    m[2]=(m[2]+3)%4
  else:#"D", 오른쪽으로 90도 회전
    m[2]=(m[2]+1)%4
  return m

board=[[0]*n  for _ in range(n)] # 2차원 배열, 전체 0

for _ in range(int(input())):
  board[int(input())-1][int(input())-1]=1 # 사과 있는 곳만 1

snake_head=[0,0,0] # 뱀의 위치, 이동중인 방향(오른쪽 0, 아래 1, 왼쪽 2, 윗쪽 3, 멈춤 4)
snake_tail=[0,0,0] # 꼬리 위치
time=0

board[0][0]=2 # 뱀이 위치한 곳 2

for _ in range(int(input())):
  for i in range(int(input())):
    temp=move(snake_head)
    if snake_head==temp:
      time+=1
      snake_head=temp
      if board[snake_head[0]][snake_head[0]]==0: # 빈공간
         board[snake_tail[0]][snake_tail[0]]=0 # 꼬리를 빈공간으로 만들고
         move(snake_tail) # 꼬리 이동### 꺾이는 부분에서 꼬리 어떻게 이동할 것인가??????
      elif board[snake_head[0]][snake_head[0]]==2: # 이미 지나간 곳
        snake_head[2]=4
        break
      board[snake_head[0]][snake_head[0]]=2 # 뱀이 위치한 곳 2
    else:
      snake_head[2]=4
      break
  if snake_head[2]==4:
    break
  turn(snake_head)

print(time)