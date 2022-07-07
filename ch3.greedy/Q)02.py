s = input()
rst = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or rst <= 1:
       rst += num
    else:
        rst *= num

print(rst)
