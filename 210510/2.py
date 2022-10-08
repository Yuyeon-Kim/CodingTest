# 다리를 지나는 트럭
# 문제 설명
# 트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
# ※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

# 예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

# 경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
# 0	[]	[]	[7,4,5,6]
# 1~2	[]	[7]	[4,5,6]
# 3	[7]	[4]	[5,6]
# 4	[7]	[4,5]	[6]
# 5	[7,4]	[5]	[6]
# 6~7	[7,4,5]	[6]	[]
# 8	[7,4,5,6]	[]	[]
# 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

# solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.
# 입출력 예
# bridge_length	weight	truck_weights	return
# 2	10	[7,4,5,6]	8
# 100	100	[10]	101
# 100	100	[10,10,10,10,10,10,10,10,10,10]	110
# 출처

# ※ 공지 - 2020년 4월 06일 테스트케이스가 추가되었습니다.

def solution(bridge_length, weight, truck_weights):#다리 길이, 다리가 버틸 수 있는 무게, 대기 트럭
    time=1#경과 시간
    run_truck=[]#진행중인 트럭
    run_truck_remain_time=[]#건너는 시간

    #남아있는 트럭이 있거나 진행중인 트럭이 있는 동안 반복
    while (truck_weights or run_truck):

        #진행중인 트럭이 있으면, time를 1 증가시킨다
        if run_truck:
            time+=1

        #남아있는 트럭이 있으면
        #진행중인 트럭의 총합+남아있는 트럭의 첫번째 요소의 합이 다리가 버틸 수 있는 무게보다 작으면
        #남아있는 트럭의 첫번째 요소를 진행중인 트럭으로 옮김
        #건너는 시간에 다리 길이를 추가함
        if truck_weights:
            if (sum(run_truck)+truck_weights[0])<=weight:
                #print("appended :", truck_weights[0])
                run_truck.append(truck_weights.pop(0))
                run_truck_remain_time.append(bridge_length+1)

        #건너는 시간 전체에 -1 하기
        for i in range(0, len(run_truck_remain_time)):
            run_truck_remain_time[i]=run_truck_remain_time[i]-1

        #건너는 시간이 0이 되면
        #진행중인 트럭과 건너는 시간에서 첫번째 요소 지움
        if run_truck_remain_time[0]==0:
            run_truck.pop(0)
            run_truck_remain_time.pop(0)

        # print("run truck:",run_truck, "run time:",run_truck_remain_time, "time:", time, "remain truck:",truck_weights)
    return time


print(solution(2, 10, [7, 4, 5, 6] ))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10] ))
