test = input().split()
garo = int(test[0])
sero = int(test[1])

cut_no = int(input())
garo_list = [0]*garo
sero_list = [0]*sero
for i in range(cut_no):
    cut_info = list(map(int, input().split()))
    if cut_info[0] == 0:
        sero_list[cut_info[1]] = 1
    else:
        garo_list[cut_info[1]] = 1
sero_max = 0
garo_max = 0
idx1 = 0
idx2 = 0
for i in range(sero):
    if sero_list[i] == 1:
        if i - idx1 > sero_max:
            sero_max = i - idx1
        idx1 = i
if sero - idx1 >sero_max:
    sero_max = sero-idx1

for i in range(garo):
    if garo_list[i] == 1:
        if i - idx2 > garo_max:
            garo_max = i - idx2
        idx2 = i
if garo - idx1 >garo_max:
    garo_max = garo-idx2
max_area = garo_max * sero_max
print(max_area)