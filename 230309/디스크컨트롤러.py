def solution(jobs):
    job_len = len(jobs)
    time = 0
    answer = 0 #요청된 시간과 실행된 시간의 차이의 평균을 구할 것
    queue = [jobs[0][0]]
    # job_idx = 1
    while queue or jobs:
        input_job = jobs.pop(0)
        for i, ce in enumerate(queue):
            if input_job[1] < ce[1]:
                queue.insert(i, input_job)
                # print("insert", input_job, "to queue's", i, "idx")
                break
        else:
            queue.append(input_job)
            # print("insert", input_job, "to queue's last idx")
        print(queue)
        if  queue[0][0] <= time:
            print(time)
            current_job = queue.pop(0)
            time+=current_job[1]
            answer+= time - current_job[0]
            print(current_job, answer, time, current_job[0])
        else:
            time+=1
            
    return answer/job_len

print(solution([[0, 3], [1, 9], [2, 6]]))