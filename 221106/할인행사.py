def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        for w, n in zip(want, number):
            if discount[i:i+10].count(w)<n:
                break
        else:
            answer+=1
    return answer