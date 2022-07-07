s = input()
cnt1 = 0
cnt0 = 0

if s[0] == '0':
    cnt1 += 1
else:
    cnt0 += 1
'''
for i in range(1, len(s)-1):
    if s[i] == '0' and s[i+1] == '1':
        cnt1 += 1

for i in range(len(s)-1):
    if s[i] == '1' and s[i+1] =='0':
        cnt0 += 1
'''

for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt1, cnt0))