# while idx == len(s1)
# 문자열이 몇번째 있는지 검색
# if 문자열이 있으면
#     cnt += 1
#     idx 문자열len 만큼 건너뜀
# else:
#     cnt +=1
#     idx 다음칸으로 건너뜀

# def BruteForce(search,arr):
#     i = 0
#     j = 0 
#     cnt = 0
#     while j < len(search) and i< len(arr) :
#         if arr[i] != search[j]:
#             i = i -j
#             j = -1
#         i = i+1
#         j=  j+1
#     if [j] == len(search) :
#         return i - len(search)
#     else:
#         return -1


# print(BruteForce('na','bananana'))



#문자열 갯수세주는 함수
# def BruteForce(search,arr):
#     i = 0
#     j = 0 
#     cnt = 0
#     while j < len(search) and i< len(arr) :
#         if arr[i] == search[j]:
#             i = i+1
#             j=  j+1
#             cnt += 1
#             print(cnt)
#         else :
#             i = i -j
#             j = -1
#             i = i+1
#             j=  j+1
#     return cnt


# print(BruteForce('banana','bana'))


# T = int(input())
# for tc in range(1,T+1):
#     s1 ,s2 = input().split()
#     cnt = BruteForce(s1,s2)
#     print(cnt)
    # mini = len(s1)-(cnt * len(s2))
    # print(mini)

# def BruteForce(search,arr):
#     i = 0
#     j = 0 
#     cnt = 0
#     while j < len(search) and i< len(arr) :
#         if arr[i] != search[j]:
#             i = i -j
#             j = -1
#         i = i+1
#         j=  j+1
#         else arr[i] == search[j]:
#             cnt +=1
#     return cnt

#문자열 갯수세주는 함수
# def BruteForce(search,arr):
#     i = 0
#     j = 0 
#     cnt = 0
#     while j < len(search) and i< len(arr) :
#         if arr[i] == search[j]:
#             i = i+1
#             j=  j+1
#             cnt += 1
#         else :
#             i = i+1
#             j=  j+1
#             i = i -j
#             j = -1
#     return cnt




def BruteForce(search,arr):
    n = len(arr)
    m = len(search)
    i =0 #arr의 인덱스
    j =0 #search 의 인덱스 
    while j < m and i<n: #각 인덱스가 길이보다 짧은동안 
        if arr[i]!=search[j]: #만약에 다른경우
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == m :
        return i-m
    else:
        return -1


print(BruteForce('banana','bana'))

--------------------------------------
def find(T,P):
    lenT=len(T)
    lenP=len(P)
    cnt = 0
    # for idxT in range(lenT - lenP +1):
        idxP =0
        while idxP<lenP and T[idxT+idxP] == P[idxP]:
            idxP += 1
        if idxP ==lenP:
            cnt += 1
            idxT += lenP
        else:
            idxT += 1
    return cnt
