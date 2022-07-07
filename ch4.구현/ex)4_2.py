n = int((input()))
cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            #매 시각 안에 '3'아 포함되면 카운트
            if '3' in str(i) + str(j) + str(k): #문자열인게 중요~~
                cnt += 1

print(cnt)