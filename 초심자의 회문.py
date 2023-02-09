def ispellin(s):
    leng = len(s)
    i = 0
    cnt =0
    for i in range( 0,leng // 2):
        if s[i] == s[leng-1-i] :
            cnt += 1
        i += 1
    if cnt == leng//2 :
        return 1
    else:
        return 0


T = int(input())
for tc in range(1,T+1):
    s = input()
    sol = ispellin(s)
    print(f'#{tc} {sol}')



