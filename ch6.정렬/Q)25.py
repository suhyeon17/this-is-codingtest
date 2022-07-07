n = int(input())
stages = list(map(int, input().split()))

def solution(N, stages):
    score = []

    stages.sort()
    cnt = [0] * (N+2)

    for i in range(len(stages)):
        cnt[stages[i]] += 1 #해당 스테이지를 도전하는 도전자 수

    for i in range(1, len(cnt)-1):
        if sum(cnt[i:]) == 0:  #해당 스테이지에 도달한 유저가 없을 때
            score.append((i, 0))
        else:
            score.append((i, (cnt[i] / sum(cnt[i:]))))  #해당 스테이지의 실패율 계산
    #점수 내림차순
    score = sorted(score, key = lambda x:x[1], reverse=True)

    answer = []
    for i in range(len(score)):
        answer.append(score[i][0])

    return answer

print(solution(n, stages))