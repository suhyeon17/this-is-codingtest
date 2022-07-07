n = input()
#문자열 절반 길이 찾기
halfLen = len(n) // 2 #그냥 /쓰면 결과가 float라 반복문에서 문제 생김
left = 0
right = 0

#left합 구하기
for i in range(halfLen):
    left += int(n[i])
#right합 구하기
for j in range(halfLen, len(n)):
    right += int(n[j])

#결과 출력
if left == right:
    print('LUCKY')
else:
    print('READY')
