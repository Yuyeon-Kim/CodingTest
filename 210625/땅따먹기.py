import numpy as np

def solution(land):
    answer = 0
    sortedLand=[]
    
    # 정렬 이용
    # 모든 최댓값의 인덱스를 찾는다.
    for j in land:
        a = np.array(j)
        s = a.argsort()
        sortedLand.append(list(zip(a[s[::-1]], s[::-1])))

    # print(sortedLand)

    for i in range(len(sortedLand)-1):
        # 만약 연속된 열의 인덱스 값이 같다면, 감소폭이 더 큰 값의 인덱스만 그대로 하고, 다른 값의 인덱스를 바꾼다
        # 바뀐 인덱스를 저장
        # 위의 과정을 연속된 열의 인덱스 값이 같지 않을 때까지 반복
        if sortedLand[i][0][1]==sortedLand[i+1][0][1]:
            if sortedLand[i][0][0]-sortedLand[i][1][0]<=sortedLand[i+1][0][0]-sortedLand[i+1][1][0]:
                # print(i, sortedLand[i][0])
                del sortedLand[i][0]
            else:
                # print(i, sortedLand[i+1][0])
                del sortedLand[i+1][0]
        # 인덱스에 맞는 값 모두 더해서 결과 출력
        # print(sortedLand[i][0][0])
        answer+=sortedLand[i][0][0]

    answer+=sortedLand[len(sortedLand)-1][0][0]
    
    return answer




print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))