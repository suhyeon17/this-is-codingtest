def solution(s):
    #최대로 나눌 수 있는 단위 = len(s)//2
    maxK = len(s) // 2
    minLen = len(s)

    #k는 문자열 나누는 단위
    for k in range(1, maxK + 1):
        cnt = 1
        newS = []
        #문자열을 k개씩 나누면서 확인
        #ex)k = 2 -> ab|ab|cd|cd|ab|ab|cd|cd
        for i in range(0, len(s) + 1, k):
            #현재 k개로 나눈 문자열과 다음 k개의 문자가 같은지 비교
            now = s[i:i + k]
            next = s[i + k:i + (2 * k)]

            #같으면 cnt 1증가
            if now == next:
                cnt += 1
            #다르면 압축한 문자를 저장
            else:
                if cnt > 1:
                    newS.append(str(cnt))
                newS.append(now)
                #다르면 cnt=1이 됨
                cnt = 1

        # print(''.join(newS))

        # 최솟값 구하기
        newLen = len(''.join(newS))
        if minLen > newLen:
            minLen = newLen

    return minLen

s = input()

print(solution(s))




