n = int(input())
dict = {}
for i in range(n):
    key, val = input().split()
    dict[key] = val

dict = sorted(dict.items(), key = lambda item:item[1])

for key, val in dict:
    print(key, end = ' ')