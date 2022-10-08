def solution(number, k):
    length = len(number) - k # 남길 자릿수
    answer = []
    end = len(number) - (length-1)# end : number의 길이에서 남길 자릿수만큼 빼기(더 저장해야할 자릿수 +1 만큼 남음) (=k+1)
    while len(answer) != length: # answer가 남길 자릿수만큼 채워지면 루프 종료
        temp = "0"
        for i in range(len(number[0:end])):# 해당 범위 내에서 제일 큰 수 선택
            if number[i] > temp:
                temp = number[i]
                p = i
                if number[i] == "9":# 9이면 가장 큰 수이므로, 이 수 선택
                    break
        if temp == "0":
            p = 0
        answer.append(temp) # answer에 선택된 값 저장
        number = number[p+1:]# number 를 선택된 값 이후로 슬라이싱해서 저장
        end = len(number) - (length - 1 -len(answer))# end를 업데이트 : number의 길이에서 남길 자릿수 -1 만큼 빼기(더 저장해야할 자릿수 +1 만큼 남음), 이미 뺀 자릿수만큼 빼기

    answer = ''.join(answer)
    return answer