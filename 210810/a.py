def solution(orders, course):
    answer = []
    
    # 아이디어. 주문된 메뉴로 조합을 만들어 두번 주문되면 answer에 추가
    
    # order의 원소를 set으로 변환
    # orders=[set(i) for i in orders]
    # print(orders)
    # orders.sort(key=len)
    al=set()
    for c in course:
        for o in orders:
            if len(o)==c:
                al.add(o)
    
    # al의 모든 원소에 대해 order 하나하나 보며 두번 나오면 answer에 추가
    for a in al:
        count=0
        for o in orders:
            if set(a).issubset(set(o)):
                if count==1:
                    answer.append(a)
                    break
                count+=1

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
		
	