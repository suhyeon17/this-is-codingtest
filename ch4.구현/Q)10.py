def solution(key, lock):
    lockLen = len(lock)
    keyLen = len(key)
    tmpLen = lockLen + (keyLen - 1) * 2
    # lock을 확장한 빈 2차원 배열 생성
    tmp = [[-1] * tmpLen for _ in range(tmpLen)]
    # 확장한 lock의 가운데를 자물쇠로 채움
    for i in range(keyLen - 1, keyLen + lockLen - 1):
        for j in range(keyLen - 1, keyLen + lockLen - 1):
            tmp[i][j] = lock[i - (keyLen - 1)][j - (keyLen - 1)]

    #자물쇠의 모든 부분이 1이 되어야 열림! 최초의 1의 갯수 세기
    cnt1 = 0
    for i in range(lockLen):
        for j in range(lockLen):
            if lock[i][j] == 1:
                cnt1 += 1

    cnt0 = 0
    open = True
    answer = False
    # 한번 회전할 때마다 모든 경우의 수 탐색
    for n in range(4):
        for i in range(tmpLen - keyLen + 1):
            for j in range(tmpLen - keyLen + 1):
                for k in range(keyLen):
                    for l in range(keyLen):
                        #확장된 자물쇠 부분은 검사할 필요가 없으므로 패스
                        if tmp[i+k][j+l] == -1:
                            continue
                        #확장된 부분 중 자물쇠의 홈과 열쇠의 홈이 맞으면 열리지 않음
                        elif tmp[i+k][j+l] == 0:
                            if key[k][l] == 0:
                                open = False
                                break
                            #확장된 부분 중 자물쇠의 홈과 열쇠의 돌기가 맞으면 +1
                            else:
                                cnt0 += 1
                        #확장된 부분 중 자물쇠의 돌기와 열쇠의 돌기가 맞으면 열리지 않음
                        else:
                            if key[k][l] == 1:
                                open = False
                                break
                            #확장된 부분 중 자물쇠의 돌기과 열쇠의 홈이 맞으면 여는데 이상이 없음
                            else:
                                continue

                #여는데 이상이 없고 자물쇠의 모든 홈이 채워져 있으면 열림
                if ((cnt0 + cnt1) == lockLen * lockLen) and open:
                    answer = True
                    return answer
                else:
                    open = True
                    answer = False
                    cnt0 = 0
        #열리지 않으면 회전
        key = turn_right(key)

    return answer

def turn_right(x):
    n = len(x)
    turn = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            turn[j][n - 1 - i] = x[i][j]

    return turn

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
