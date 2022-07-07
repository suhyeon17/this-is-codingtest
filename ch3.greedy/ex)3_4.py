n, k = map(int, input().split())
cnt = 0

'''
while True:
    if n == 1:
        break
    elif n < k:
        x = n % k
        n -= (x - 1)
        cnt += (x - 1)
    else:
        x = n % k
        n -= x
        n /= k
        cnt += (x + 1)
'''

while True:
    x = (n // k) * k
    cnt += (n - x)
    n = x

    if n < k:
        break

    cnt += 1
    n /= k

cnt += (n - 1)

print(int(cnt))