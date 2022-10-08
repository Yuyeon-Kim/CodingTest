from itertools import combinations as combi

def solution(relation):

    row = len(relation)
    col = len(relation[0])
    
    # 전체 가능한 조합을 모두 만든다
    candidates = []
    for i in range(1, col + 1):
        candidates.extend(combi(range(col), i)) # 인덱스의 조합을 저장

    # 유일성을 만족하는 조합만 남긴다
    unique = []
    for candi in candidates:
        tmp = [tuple([item[i] for i in candi]) for item in relation]# 튜플 형태로 키를 저장
        if len(set(tmp)) == row: # set 이용해 중복을 제거한 경우에 중복이 없을 때
            unique.append(candi) # 유일성 만족하므로 unuque에 추가

    # 최소성을 만족하지 않는 조합을 제거한다
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if set(unique[j]) == set(unique[i]) & set(unique[j]):
                # unique[j]가 unique[i]의 부분집합일 때 최소성 만족 못하므로 answer에서 지우기
                answer.discard(unique[j])

    return len(answer)