def bfs(computers):
    # 0번 컴퓨터부터 bfs

    networks = 0
    
    visited = [0]* len(computers)
    
    queue = []
    
    while 0 in visited:
        networks+=1
        
        first_idx = visited.index(0)
        
        visited[first_idx] = networks
        queue.append(first_idx)
        
        while queue:
            com = queue.pop(0)
            
            for connected_com in computers[com]:
                queue.append(connected_com)
                visited[connected_com] = networks
                print(com, connected_com, visited)

        return max(networks)        

def solution(n, computers):
    return bfs(computers)

print(solution(3, 	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))