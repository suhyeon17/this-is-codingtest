def makeUV(s):
    cntL = 0
    cntR = 0
    u = ''
    v = ''

    for i in s:
        if i == '(':
            cntL += 1
        else:
            cntR += 1
        u += i

        if cntL == cntR:
            break

    v = s.replace(u, '', 1)

    return u, v

def solution(p):
    answer = ''

    #step1
    if p == '':
        return ''

    #step2
    u, v = makeUV(p)

    #step3
    if u[-1] == ')': #u의 마지막이 )이면 무조건 올바름 !중요 포인트!
        u += solution(v)

        return u

    #step4
    answer += '('
    answer += solution(v)
    answer += ')'
    for i in range(1, len(u)-1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('

    return answer
