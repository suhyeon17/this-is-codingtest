#큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse = True)

ans = 0
'''
for i in range(m // (k + 1)):
    ans += (data[0] * k)
    ans += data[1]

if m % (k + 1) != 0:
    ans += (data[0] * (m % (k + 1)))
'''
#가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k
count += m % (k + 1)

ans += count * data[0]
ans += (m - count) * data[1]

print(ans)

