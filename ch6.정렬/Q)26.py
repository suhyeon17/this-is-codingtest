n = int(input())
card = []
for i in range(n):
    card.append(int(input()))

card.sort(reverse=True)

while True:
    total = card[-2] + card[-1]
    card.pop()
    card.pop()

    idx = 0
    for i in card:
        if i <= total:
            idx = card.index(i)
            break


    card.insert(idx, total)

    if len(card) == 2:
        break

print(sum(card) + total)



