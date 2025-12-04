def solution(N, stages):
    total_user = len(stages)
    failure_rate = []
    
    for i in range(N):
        cur_stage = i + 1
        challenge_cnt = 0
        fail_cnt = 0
        for stage in stages:
            if stage >= cur_stage:
                challenge_cnt += 1
                if stage == cur_stage:
                    fail_cnt += 1
        if challenge_cnt == 0:
            failure_rate.append(0)
        else:
            failure_rate.append(fail_cnt / challenge_cnt)
    
    sorted_with_index = sorted(enumerate(failure_rate), key=lambda x:x[1], reverse = True)    
    answer = [index + 1 for index, value in sorted_with_index]
    
    return answer