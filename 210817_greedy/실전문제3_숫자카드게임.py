n, m=map(int , input().split())
nums=list( list(map(int, input().split())) for _ in range(n)) # 2차원 배열
print(max(min(nums[i]) for i in range(n))) # 각 행의 최솟값 중 최댓값