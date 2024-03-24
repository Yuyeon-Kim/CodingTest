def BFS(start, maps):
    # start: (x, y)에서부터 maps의 제일 오른쪽 아래에 있는 점까지의 최소 경로 구하는 메서드
    n = len(maps[0])
    m = len(maps)
    
    visited = [[0]*n for _ in range(m)]
    
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    queue = []
    queue.append(start)
    visited[0][0] = 1
    while queue:
        x, y = queue.pop(0)
        
        for dx, dy in move:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m and maps[ny][nx] == 1 and visited[ny][nx]==0: # 진행 가능한 조건
                # print(nx, ny, visited[y][x])
                # print(visited)
                queue.append((nx, ny))
                visited[ny][nx] = visited[y][x]+1 # 틀렸었음
    return visited[m-1][n-1]
            
        
def solution(maps):
    ans = BFS((0, 0), maps)
    return -1 if ans == 0 else ans

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))