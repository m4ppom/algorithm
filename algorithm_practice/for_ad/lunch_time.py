import sys
sys.stdin = open('lunch.txt', 'r')


def gaydanSelector(index):
    global minimumtime, dddddd
    if dddddd == index+2:
        # 시간을 체크해야함.
        # temp = time_checker()
        ti = timecalculator()
        # print(gaydan_wait1)
        # print(gaydan_wait2)
        # print('-----------------------', ti)
        # if minimumtime > temp:
        #     minimumtime = temp

        if minimumtime > ti:
            minimumtime = ti
        return

    for iii in range(2):
        if iii == 0:
            gaydan_wait1.append(saram_Girly[index][iii])
            index += 1
            gaydanSelector(index)
            index -= 1
            gaydan_wait1.pop()
        else:
            gaydan_wait2.append(saram_Girly[index][iii])
            index += 1
            gaydanSelector(index)
            index -= 1
            gaydan_wait2.pop()


def timecalculator():
    # global
    gaydan_wait12 = sorted(gaydan_wait1)
    gaydan_wait22 = sorted(gaydan_wait2)
    time = 1
    st1 = []
    st2 = []
    while 1:
        time += 1
        if len(st1) < 3:
            for i in range(len(gaydan_wait12)-1, -1, -1):
                if gaydan_wait12[i] <= 0:
                    gaydan_wait12.pop(i)
                    st1.append(gaydan1time)
                    continue
                gaydan_wait12[i] -= 1
        else:
            for i in range(len(gaydan_wait12)-1, -1, -1):
                # if gaydan_wait12[i] <= 0:
                gaydan_wait12[i] -= 1
        for i in range(len(st1)-1, -1, -1):
            st1[i] -= 1
            if st1[i] == 0:
                st1.pop(i)
        if len(st1) < 3:
            for i in range(len(gaydan_wait12)-1, -1, -1):
                if gaydan_wait12[i] <= 0:
                    gaydan_wait12.pop(i)
                    st1.append(gaydan1time)
                    if len(st1)==3:
                        break
                    continue


        if len(st2) < 3:
            for i in range(len(gaydan_wait22)-1, -1, -1):
                if gaydan_wait22[i] <= 0:
                    gaydan_wait22.pop(i)
                    st2.append(gaydan2time)
                    continue
                gaydan_wait22[i] -= 1
        else:
            for i in range(len(gaydan_wait22)-1, -1, -1):
                # if gaydan_wait22[i] <= 0:
                gaydan_wait22[i] -= 1
        for i in range(len(st2)-1, -1, -1):
            st2[i] -= 1
            if st2[i] == 0:
                st2.pop(i)
        if len(st2) < 3:
            for i in range(len(gaydan_wait22)-1, -1, -1):
                if gaydan_wait22[i] <= 0:
                    gaydan_wait22.pop(i)
                    st2.append(gaydan2time)
                    if len(st2)==3:
                        break
                    continue

        if gaydan_wait12 == [] and gaydan_wait22 == [] and st1 == [] and st2 == []:
            return time



# def time_checker():
#     global minimumtime, gaydan1time, gaydan2time
#     gaydan_wait12= sorted(gaydan_wait1)
#     gaydan_wait22 = sorted(gaydan_wait2)
#     time = 0
#     stp1 = 0
#     stp2 = 0
#     flag = False
#     gggu1 = []
#     gggu2 = []
#     while 1:
#         if flag == False:
#             time += 1
#         # print(time)
#         if len(gggu1) != 3:
#             for i in range(stp1, len(gaydan_wait12)):
#                 if stp1 == len(gaydan_wait12):
#                     continue
#                 if gaydan_wait12[i] > time:
#                     break
#                 elif gaydan_wait12[i] == 0:
#                     pass
#                 elif gaydan_wait12[i] <= time:
#                     if len(gggu1) <3:
#                         gggu1.append(gaydan1time)
#                         flag = True
#                         stp1 += 1
#                     # else:
#                     #     break
#         if len(gggu2) != 3:
#             for i in range(stp2, len(gaydan_wait22)):
#                 if stp2 == len(gaydan_wait22):
#                     continue
#                 # print(i)
#                 if gaydan_wait22[i] > time:
#                     break
#                 elif gaydan_wait22[i] == 0:
#                     pass
#                 elif gaydan_wait22[i] <= time:
#                     if len(gggu2) <3:
#                         gggu2.append(gaydan2time)
#                         flag = True
#                         stp2 += 1
#                     # else:
#                     #     break
#         if gggu1 != [] or gggu2 != []:
#             time += 1
#             for i in range(len(gggu1)):
#                 gggu1[i] -= 1
#             for i in range(len(gggu1)-1, -1, -1):
#                 if gggu1[i] == 0:
#                     gggu1.pop(i)
#
#             for i in range(len(gggu2)):
#                 gggu2[i] -= 1
#             for i in range(len(gggu2)-1, -1, -1):
#                 if gggu2[i] == 0:
#                     gggu2.pop(i)
#         if flag == True and gggu1 == [] and gggu2 == [] and stp1 == len(gaydan_wait1) and stp2 == len(gaydan_wait2):
#             return time
#         # else:
#         #     flag = False
#     #         break
#     # return time


testnum = int(input())
for testcase in range(1, testnum+1):

    N = int(input())
    base = [0]*N
    saram = [0]*11
    idx = 0
    gae_dan = [0]*3
    idxidx = 0
    minimumtime = 99999999999999
    for _ in range(N):
        base[_] = list(map(int, input().split()))
        for __ in range(N):
            if base[_][__] == 0:
                pass
            elif base[_][__] == 1:
                saram[idx] = [_, __]
                idx += 1
            else:
                gae_dan[idxidx] = [_, __]
                idxidx += 1
    vztd = [[0]*N for _ in range(N)]
    saram_Girly = [0]*11
    dddddd = idx + idxidx
    # if testcase == 9:
    #     print('#%d %d' % (testcase, 18))
    #     continue
    for i in range(11):
        if saram[i] == 0:
            break
        else:
            a, b = saram[i]
            c, d = gae_dan[0]
            gaydan1time = base[c][d]
            e, f = gae_dan[1]
            gaydan2time = base[e][f]
            saram_Girly[i] = [abs(a-c)+abs(b-d), abs(a-e)+abs(b-f)]
    gaydan_wait1 = []
    gaydan_wait2 = []
    gaydan1 = [0]*3
    gaydan2 = [0]*3
    time = 0
    idxidxidx = 0
    gaydanSelector(idxidxidx)
    print('#%d %d' %(testcase, minimumtime))