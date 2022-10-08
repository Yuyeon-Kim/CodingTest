# 파이썬
def pop_num(b, m, n):
    pop_set = set()
    # search
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i-1][j-1] == b[i-1][j] == b[i][j-1] != '_':
                pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
    # set_board
    for i, j in pop_set:
        b[i][j] = 0        
    for i, row in enumerate(b):
        empty = ['_'] * row.count(0)
        b[i] = empty + [block for block in row if block != 0]
    return len(pop_set)
     
def solution(m, n, board):
    count = 0
    b = list(map(list,zip(*board)))
    while True:
        pop = pop_num(b, m, n)
        if pop == 0: return count
        count += pop
#출처 : https://velog.io/@tjdud0123/%ED%94%84%EB%A0%8C%EC%A6%88-4%EB%B8%94%EB%A1%9D-2018-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python

# 내가 풀이한 것
# def solution(m, n, board):
#     answer = 0
#     board=[list(x) for x in board]
#     # print(board)
#     while True:
#         dir={}#위치 초기화
#         for i in range(1, m):#대각선 위, 위, 왼쪽이 같으면, 해당 위치 set에 저장(중복 x)
#             for j in range(1, n):
#                 # print(i, j)
#                 if board[i-1][j-1]==board[i-1][j]==board[i][j-1]==board[i][j]:
#                     dir.update([(i-1,j-1),(i-1,j),(i,j-1),(i,j)])
                    
#         if not dir:#비었으면, 지울 블록이 없는 것이므로 break
#             break
#         answer+=len(dir)#지운 개수 저장
#         print(dir)
#         for i in dir:#블록 지우기(임의로 0으로 만들기)
#             print(i)
#             board[i[0]][i[1]]='0'
        
#         for j in range(n): #블록 밑으로 끌어내리기
#             while True:
#                 zero=m
#                 nonzero=m
#                 for i in range(m-1):
#                     if board[i][j]=='0' and board[i+1][j]!='0' and nonzero!=m:#문자를 한번 만난 뒤, 0 만나면
#                         zero=i
#                         break
#                     else:
#                         nonzero=i
#                 else:#0을 만나기 전 문자 안만남
#                     break
                    
#                 #0 만나기 전 만났던 알파벳들을 알파벳 나오기 전에 있는 0들과 교환
#                 while board[nonzero][j]!='0':
#                     board[zero][j]=board[nonzero][j]
#                     board[nonzero][j]='0'
#                     if nonzero==0:
#                         break
#                     zero-=1
#                     nonzero-=1   

#     return answer