from operator import itemgetter
def solution(food_times, k):
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i+1))
    foods.sort() #튜플의 첫번째 값을 기준으로 정렬

    pretime = 0 #이전 음식을 먹는데 걸리는 시간
    for i, food in enumerate(foods): #i는 인덱스, food[0]는 음식 먹는데 걸리는 소요시간
        diff = food[0] - pretime #이전 음식을 먹는데 걸리는 시간과 현재 음식을 먹는데 걸리는 시간의 차이이므로 diff는 칸 하나의 높이

        if diff != 0:
            spend = diff * n #칸 하나의 높이 * 남은 음식 수
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key = itemgetter(1))
                return sublist[k][1]
        n-= 1

    return -1