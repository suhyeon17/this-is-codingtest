n = int(input())
score = []
for i in range(n):
    name, kor, eng, math = input().split()
    score.append((name, int(kor), int(eng), int(math)))

#-붙이면 내림차순
score = sorted(score, key=lambda student:(-student[1], student[2], -student[3], student[0]))

for i in range(n):
    print(score[i][0])