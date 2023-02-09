# #브루트포스
# p = "is"
# t= "this is a book"
# M = len(p) #찾을 단어
# N = len(t) #여기서 찾기

# def force(p,t):
#     M = len(p) #찾을 단어
#     N = len(t) #여기서 찾기
#     i = 0 #t에서의 비교위치
#     j = 0 #p에서의 비교위치
#     while i < N and j < M: #비교할 문장이 남아있고 패턴을 찾기 전이면
#         if t[i]!= p[j] : #서로 다른 글자를 만나면 
#             i = i - j   #비교를 시작한 위치로
#             j = -1 #패턴의 시작 전으로 
#         i += 1
#         j += 1
#     if j == M : 
#         return i-M    
#     else : return -1

# print(force('is','this is a book'))

# def bf2(p,t,N,M):
#     for i in range(N-M+1):
#         for j in range(M):
#             if t[i+j] != p[j]:
#                 break
#         else:
#             return i
#         return -1
#     print(bf2(p,t))

--------------------------------------
T = int(input())
for tc in range(1, T+1):
    a, b = input().split()
    len_a = len(a)
    len_b = len(b)
    idx = 0
    cnt = 0
    #a를 타이핑하며 b의 첫글자와 같은 글자가 나오면 b의 길이만큼 잘라서 b와 같은지 확인
    #같다면 입력값 1을 증가시키고 다음 입력 글자를 b의 길이만큼 넘어간다 #건너뛰어서 i += len_b 다음꺼 확인
    #아니라면 입력값 1을 증가시키고 다음 글자를 확인
    while idx < len_a:
        if a[idx] == b[0]:
            if a[idx:idx+len_b] == b:  
                cnt += 1
                idx += len_b
            else:
                cnt += 1  #다음으로 넘어가서 비교
                idx += 1
        else:               
            cnt += 1        #다음으로 넘어가서 비교
            idx += 1
    print('#{tc} {cnt}'.format(tc,cnt))
