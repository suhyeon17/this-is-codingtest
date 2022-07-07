n = int(input())
stocks = list(map(int, input().split()))
m = int(input())
buys = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return 'no'

    mid = (start + end) // 2

    if array[mid] == target:
        return 'yes'
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for buy in buys:
    print(binary_search(stocks, buy, 0, n-1), end = ' ')

