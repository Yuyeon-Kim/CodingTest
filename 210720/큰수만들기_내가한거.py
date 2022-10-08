
def solution(number, k):
    import itertools
    return max(["".join(list(i)) for i in itertools.combinations(number,len(number)-k)])

def solution2(number, k):
    import itertools

    max=tuple("0")
    for i in itertools.combinations(number,len(number)-k):
        if max<i:
            max=i
    return "".join(list(max))

# print(solution2("4177252841", 4))
# import itertools
# print(list(itertools.combinations(["1","2","3","4"],2)))
# print(list(itertools.combinations(["4","3","2","1"],2)))
# print(int("".join(list(('1', '2')))))
# print(max(["21", "214", "2"]))

# print(('2','1','6')>('0','2','1','2'))

