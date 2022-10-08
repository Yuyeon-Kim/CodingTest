# 두 큐 합 같게 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

# 해결방법: 합이 큰 쪽에서 작은 쪽으로 원소 하나씩 보낸다!

# 만들 수 없는 경우: 
# 모든 방법 실행했는데도 안될 때
# - i1과 i2가 같다: 불가능
# - 전체 길이만큼 반복하고도 1번 더 돌았다: 무한반복->불가능
# 모든 원소의 합이 홀수일 때
# 두 큐 중 한군데에 만들어야 할 큐의 합 보다 큰 원소가 있을 때


def solution(queue1, queue2):
    # 두 큐를 똑같이 만드는 것이 불가능한 경우
    sum_equal = (sum(queue1)+sum(queue2))/2
    if (sum_equal*2)%2 == 1 or max(queue1)>sum_equal or max(queue2)>sum_equal: # 모든 원소의 합이 홀수일 때, 두 큐 중 한군데에 만들어야 할 큐의 합 보다 큰 원소가 있을 때
        return -1

    connected_queue = queue1+queue2
    sum_q1, sum_all = sum(queue1), sum(queue1)+sum(queue2)
    i1, i2 = 0, len(queue1)
    count = 0

    while sum_q1*2 != sum_all: # q1의 합이 전체 합의 절반이 되었을 때
        if i1 == i2 or count>len(connected_queue)+1: # i1과 i2가 같다: 불가능 전체 길이만큼 반복하고도 1번 더 돌았다: 무한반복->불가능
            return -1
        if sum_q1*2 < sum_all: # q1이 더 작을 때
            sum_q1 += connected_queue[i2]
            i2= (i2+1)%len(connected_queue)
        else: # q1이 더 클 때
            sum_q1 -= connected_queue[i1]
            i1=(i1+1)%len(connected_queue)
        count+=1
    return count


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([4, 6, 5, 1], [3, 2, 7, 2]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 10, 1, 2], [1, 2, 1, 2]))
print(solution([1, 1], [1, 5]))
print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(solution([3, 4], [1, 4]))