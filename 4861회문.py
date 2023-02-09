# T = 10
# for tc in range(1,T+1):
#     N,M = input().split()
#     arr = [list(input()) for _ in range(N)]




# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # 정답 리스트
#     goal_list = []
#
#     # array 형식 변환
#     tx_list = []
#     for i in range(N):
#         N_str_list = list(map(str, input().split()))
#         tx_list += N_str_list
#
#     # print(tx_list[0][0])
#
#     # 가로 확인
#     for j in range(N):
#         for k in range(N-M+1):
#             cnt = 0
#             for t in range(M):
#                 if tx_list[j][t+k] == tx_list[j][M+k-t-1]:
#                     cnt += 1
#             if cnt == M:
#                 print("#{}".format(tc), end=" ")
#                 print(tx_list[j][k:k+M])
#
#             # 세로 확인
#             for k in range(N-M+1):
#                 cnt = 0
#                 for t in range(M):
#                     if tx_list[t+k][j] == tx_list[M+k-t-1][j]:
#                         cnt += 1
#                 if cnt == M:
#                     print("#{}".format(tc), end=" ")
#
#                     for i in range(M):
#                         print(tx_list[k+i][j], end="")
#                     print()

--------------------------------------------------
<sol1>
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 회문 1개 존재, 회문 찾아서 BREAK
    ans = ''
    # 가로
    for row in range(N):  # 한줄 건너뛰는
        for i in range(N - M + 1):  # 한줄안에서 얼마나 돌건지
            flag = True
            for j in range(M // 2):  # 앞과 뒤 비교하는 것
                if arr[row][i + j] != arr[row][i + M - 1 - j]:
                    flag = False
                    break
            if flag:
                ans = "".join(map(str, arr[row][i:]))
                break
    else:
        # 세로
        for col in range(N):
            for i in range(N - M + 1):
                flag = True
                for j in range(M // 2):
                    if arr[i + j][col] != arr[i + M - 1 - j][col]:
                        flag = False
                        break
                if flag:
                    for k in range(M):
                        ans += arr[i + k][col]
                    break
    print('#{} {}'.format(tc, ans))


    -----------------------------------------------
    < sol2 >

    T = int(input())

    for t in range(T):
        N, M = map(int, input().split())

        word_lst = []
        for i in range(N):
            word = input()
            word_lst.append(word)
        # print(word_lst)

        result = ''
        for i in range(0, N):
            for j in range(0, N - M + 1):
                new_word1 = word_lst[i][j:j + M]

            if new_word1 == new_word1[::-1]:
                result = new_word1
                break
        else:
            for j in range(N):
                new_word2 = ''
                for i in range(N):
                    new_word2 += word_lst[i][j]

                for m in range(0, N - M + 1):
                    new_word3 = new_word2[m:m + M]

                    if new_word3 == new_word3[::-1]:
                        result = new_word3
                        break

        print(f'#{t + 1} {result}')
----------------------------------------------
<sol3>

def isP(c1):
    if list(c1) == list(reversed(c1)):
        return 1
    return 0


# 1. 입력값 받기
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    BRD = []
    pal = 0

    # 2. 보드 만들기
    for brd in range(N):
        BRD.append(input())

    # 3. 가로
    for row in range(N):
        for i in range(N - M + 1):
            # temp = BRD[row][i:M + i]

            temp = ''
            for j in range(i, M + i):
                temp += BRD[row][j]
            if isP(temp) == 1:
                print(f'#{tc + 1} {temp}')

    # 4. 세로
    for row in range(N - M + 1):
        for j in range(N):
            temp = ''
            for k in range(M):
                temp += BRD[row + k][j]
            if isP(temp) == 1:
                print(f'#{tc + 1} {temp}')