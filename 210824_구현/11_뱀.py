def print_board(n, board, snake, time, rot_num): # 출력 함수
  print("time :",time, "rotate num :",rot_num)
  for i in range(n):
    for j in range(n):
      if [i,j] in snake:
        print("S", end="")
      else:
        print(board[i][j], end="")
      print(" ", end="")
    print()

# 입력
n=int(input()) # 맵의 사이즈
board=[[0]*n  for _ in range(n)] # 2차원 배열, 전체 0
for _ in range(int(input())):
  x, y=map(int, input().split())
  board[x-1][y-1]=1 # 사과 있는 곳만 1
xc=[input().split() for _ in range(int(input()))] # 입력 값 만큼 입력 받음

snake=[[0,0]] # 뱀이 지나간 자리
rotate_num=0 # 이동중인 방향(오른쪽 0, 아래 1, 왼쪽 2, 윗쪽 3, 멈춤 4)
rotate=[[0,1],[1,0],[-1,0],[0,-1],[0,0]] # 회전 값
time=0

for x, c in xc:
  # x회만큼 전진
  for i in range(int(x)):
    # print_board(n, board, snake, time, rotate_num)
    temp=[snake[len(snake)-1][0]+rotate[rotate_num][0],snake[len(snake)-1][1]+rotate[rotate_num][1]]
    if 0<=temp[0]<n and 0<=temp[1]<n and temp not in snake: # 범위에 알맞고 이미 지나가지 않았으면
      time+=1 # 시간 1 증가
      snake.append(temp) # 지나간 자리에 추가
      if board[temp[0]][temp[1]]==0:# 사과 없으면
        snake.pop(0) # 제일 이전에 추가된거 삭제
      else: # 사과 있으면
        board[temp[0]][temp[1]]=0 # 사과 삭제
    else:
      rotate_num=4
      break
  if rotate_num==4:
    break
    
  # 회전
  if c=="L": # 왼쪽으로 90도 회전
    rotate_num=(rotate_num+3)%4
  else:#"D", 오른쪽으로 90도 회전
    rotate_num=(rotate_num+1)%4

print(time+1)