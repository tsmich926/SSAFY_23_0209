# set 으로 글자 중복제거
# 딕셔너리 사용해서 갯수세기
# 딕셔너리에 키로 추가
T = int(input())
for tc in range(1,T+1):
    s1 = input()
    s2 = input()
    lst1 =list(set(s1))     #set한다음 요소를 꺼내기 위해 list로 바꿔줌
    my_cnt = {}             # 찾을 알파벳을 각각 카운트해줄 딕셔너리를 만듬
    for i in lst1:
        my_cnt[i] = 0         #초기값으로 0을 넣음 
        for m in range(len(s2)):
            if i == s2[m]:
                my_cnt[i] += 1
    max = 0
    for i in lst1:
        if my_cnt[i] > max :
            max = my_cnt[i]
    print(f'#{tc} {max}')












    # lst = []
    # for i in range(len(ss1)):
    #     for m in range(len(s2)):
    #         if ss1[i] == s2[m]:
    #             cnt += 1
    #             lst.append(cnt) 
    # print(lst)

