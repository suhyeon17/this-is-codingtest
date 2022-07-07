n = int(input())
house = list(map(int, input().split()))

house.sort()

#가운데 위치한 집에 설치하면 최솟값
if n%2 == 0:
    print(house[(n//2)-1])
else:
    print(house[n//2])