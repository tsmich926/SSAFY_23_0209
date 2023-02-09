#입력받은 문자열을 거꾸로해도 같은지 판별해주는 함수
##수정완


def ispln(s1):
    if list(s1) == list(reversed(s1)):
        return 1
    return 0

T = 10
for tc in range(1,T+1):
    M = int(input())
    BRD = []
    cnt = 0
    # 2. 보드 만들기
    for brd in range(8):
        BRD.append(input())
    # 3. 가로
    for row in range(8):
        for i in range(8 - M + 1):
            # temp = BRD[row][i:M + i]
            temp = ''
            for j in range(i, M + i):
                temp += BRD[row][j]
            if ispln(temp) == 1:
                cnt += 1
    # 4. 세로
    for col in range(8):
        for j in range(8 - M + 1):
            temp = ''
            for k in range(M):
                temp += BRD[j + k][col]
            if ispln(temp) == 1:
                cnt += 1
    print(f'#{tc} {cnt}')
