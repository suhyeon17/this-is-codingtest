n = int(input())
data = list(map(int, input().split()))

data.sort()
group = 0
person = 0

for i in data:
    person += 1

    if person >= i:
        group += 1
        person = 0

print(group)
