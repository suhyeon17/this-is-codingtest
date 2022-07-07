n, m = map(int, input().split())

'''
data = []
min_values = []
for i in range(n):
    data.append(list(map(int, input().split())))
    #현재 줄에서 가장 작은 수 찾아서 행마다 작은 수로 구성된 리스트 생성
    min_values.append(min(data[i]))

rst = max(min_values)
'''

rst = 0
for i in range(n):
    data = list(map(int, input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    rst = max(rst, min_value)

print(rst)
