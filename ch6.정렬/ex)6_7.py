n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#A와 최솟값과 B의 최댓값을 바꿔치기 하기위해 A는 오름차순 정렬, B는 내림차순 정렬
a.sort()
b.sort(reverse = True)

for i in range(k):
    a[i], b[i] = b[i], a[i] #swap

print(sum(a))
