# 1. 제일 큰수를 K번
# 2. 제일 큰 수의 인덱스 제외하고 제일 큰 수를 1번
# 3. 1~2번을 반복(M번)
NMK=list(map(int, input().split()))
nums=sorted(list(map(int, input().split()))) # 오름차순 정렬
print(sum(nums[NMK[0]-1-(i%(NMK[2]+1)==0)] for i in range(1, NMK[1]+1))) # K+1로 나눈 나머지가 0이 아닐 때는 제일 큰수, 0일 때는 두번째로 큰 수 더함