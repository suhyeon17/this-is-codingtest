n, m = map(int, input().split())
ball = list(map(int, input().split()))

'''시간이 오래걸릴 것 같음
cnt = 0
for i in range(len(ball)):
    for j in range(i, len(ball)):
        if ball[i] != ball[j]:
            cnt += 1
'''

array = [0] * m #무게가 m인 공의 개수를 담을 리스트
for i in ball:
    array[i] += 1 #무게 개수 카운트

cnt = 0
for i in range(1, m+1):
    #[1, 2, 2, 3, 3] -> array = [1, 2, 2]
    n -= array[i] #A가 선택할 수 있는 볼링공의 개수 제외
    cnt += array[i] * n 

print(cnt)