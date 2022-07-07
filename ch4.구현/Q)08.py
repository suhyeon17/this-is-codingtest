s = list(input())
#sort -> 숫자 순으로 정렬 후 문자 정렬됨
s.sort()

#처음으로 영어가 등장할 때의 index를 구함
idx = 0
for i in range(len(s)):
    #ascii코드를 이용하여 숫자의 아스키코드를 벗어나면 break
    #참고 '0'이 아스키코드로 49임
    if s[i] < '0' or s[i] > '9':
        idx = i
        break

#idx까지의 합을 구함
num = 0
for i in range(idx):
    num += int(s[i])

#조건에 맞게 list를 문자로 출력
print(''.join(s[idx:]) + str(num))