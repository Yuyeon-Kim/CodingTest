def solution(numbers):
    #숫자가 큰게 있는거 순으로 정렬?
    #숫자가 여러개인거보다 아닌게 더 큼
    numbers=[str(i) for i in numbers]
    
    numbers.sort(reverse=True, key=lambda x:(x[0], x[0] if len(x)==1 else x[1], x[0] if len(x)==1 else x[1] if len(x)==2 else x[2], x[0] if len(x)==1 else x[1] if len(x)==2 else x[2] if len(x)==3 else x[3] ))
    print(numbers)
    return ''.join(numbers)


print(max("123"))