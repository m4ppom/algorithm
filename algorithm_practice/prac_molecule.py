import sys
sys.stdin = open('inpu.txt', 'r')



dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
testcase = int(input())

for test_num in range(1, testcase + 1):
    collapse = 0
    time = 0
    result = 0
    base = [[0 for _ in range(2001)]for _ in range(2001)]
    atom_num = int(input())
    atoms = [0] * atom_num
    for h in range(atom_num):
        atoms[h] = list(map(int,input().split()))
        atoms[h][0] += 1000
        atoms[h][1] += 1000
        # print(type(atoms[i][0]))
        x = atoms[h][0]
        y = atoms[h][1]
        c = atoms[h][2]
        e = atoms[h][3]
        base[y][x] = e
    # print(atoms)
    nothing = [1]* atom_num
    while time < 2000:
        time += 1
        intime=[1]* atom_num
        # visited = [0]*atom_num
        for i in range(atom_num):
            if nothing[i] == 0:
                continue
            if atoms[i][1] + dy[atoms[i][2]] == 2000 or atoms[i][0] + dx[atoms[i][2]] == 2000 or atoms[i][1] + dy[atoms[i][2]] == -1 or atoms[i][0] + dx[atoms[i][2]] == -1:
                atoms[i][3] = 0
                nothing[i] = 0
            elif atoms[i][1] + dy[atoms[i][2]] < 2001 and atoms[i][0] + dx[atoms[i][2]] < 2001 and atoms[i][1] + dy[atoms[i][2]] > -1 and atoms[i][0] + dx[atoms[i][2]] > -1:
                # visited[i] = 1
                atoms[i][1] = atoms[i][1] + dy[atoms[i][2]]
                atoms[i][0] = atoms[i][0] + dx[atoms[i][2]]
        for i in range(atom_num):
            # if nothing[i] == 0:
            #     continue
            for find in range(atom_num):
                if i == find:
                    continue
                if nothing[find] == 0:
                    continue


                elif atoms[i][1] == atoms[find][1] and atoms[i][0] == atoms[find][0] and atoms[i][3] != 0 and atoms[find][3] != 0 and nothing[find] == 1:
                    # and atoms[i][3] != 0 and atoms[find][3] != 0
                    # print('aasdas',atoms[i], atoms[find])
                    collapse = collapse + atoms[i][3] + atoms[find][3]
                    atoms[i][3] = 0
                    atoms[find][3] = 0
                    nothing[i] = 0
                    nothing[find] = 0
                    intime[i] = 0
                    intime[find] = 0
                elif atoms[i][1] + dy[atoms[i][2]] == atoms[find][1] and atoms[i][0] + dx[atoms[i][2]] == atoms[find][0] and atoms[find][1] + dy[atoms[find][2]] == atoms[i][1] and atoms[find][0] + dx[atoms[find][2]] == atoms[i][0]:
                    if nothing[find] == 1 and nothing[i]==1 and nothing[find]==1 and atoms[find][3] != 0 and intime[i] != 0 and intime[find] != 0:
                        # print('hhhh',atoms[i], atoms[find])
                        collapse = collapse + atoms[i][3] + atoms[find][3]
                        atoms[i][3] = 0
                        atoms[find][3] = 0
                        nothing[i] = 0
                        nothing[find] = 0
                elif atoms[i][1] == atoms[find][1] and atoms[i][0] == atoms[find][0] and nothing[find] == 1 and intime[i] == 0:
                    # and atoms[i][3] != 0 and atoms[find][3] != 0
                    # print('aasdas',atoms[i], atoms[find])
                    collapse = collapse + atoms[i][3] + atoms[find][3]
                    atoms[i][3] = 0
                    atoms[find][3] = 0
                    nothing[i] = 0
                    nothing[find] = 0
                    intime[i] = 0
                    intime[find] = 0
    print('#{} {}'.format(test_num, collapse))
                # print(collapse)

                # elif atoms[i][1] == atoms[find][1] and atoms[i][0] == atoms[find][0] and nothing[find] == 1:
                #     collapse += atoms[i][3] + atoms[find][3]
                #     atoms[i][3] = 0
                #     atoms[find][3] = 0
                #     nothing[i] = 0
                #     nothing[find] = 0
                # elif atoms[i][1] + dy[atoms[i][2]] == atoms[find][1] and atoms[i][0] + dx[atoms[i][2]] == atoms[find][0] and atoms[find][1] + dy[atoms[find][2]] == atoms[i][1] and atoms[find][0] + dx[atoms[find][2]] == atoms[i][0]:
                #     if nothing[find] == 1 and nothing[i] == 1 and atoms[i][3] != 0 and atoms[find][3] != 0:
                #         print('hhhh',atoms[i], atoms[find])
                #         collapse = collapse + atoms[i][3] + atoms[find][3]
                #         atoms[i][3] = 0
                #         atoms[find][3] = 0
                #         nothing[i] = 0
                #         nothing[find] = 0
                #         continue
    # print('#{} {}'.format(test_num, collapse))
            # # print(i)
            # # print(i,'aaa',time)
            # if visited[i] == 1:
            #     continue
            # if atoms[i][3] == 0:
            #     continue
            # if base[atoms[i][1]][atoms[i][0]] == 0:
            #     atoms[i][3] = 0
            #     # print('asdsadsad')
            #     continue
            # elif atoms[i][1] + dy[atoms[i][2]] == 2000 or atoms[i][0] + dx[atoms[i][2]] == 2000 or atoms[i][1] + dy[atoms[i][2]] == -1 or atoms[i][0] + dx[atoms[i][2]] == -1:
            #     base[atoms[i][0]][atoms[i][1]] = 0
            #     atoms[i][3] = 0
            #     continue
            # elif atoms[i][1] + dy[atoms[i][2]] < 2001 and atoms[i][0] + dx[atoms[i][2]] < 2001 and atoms[i][1] + dy[atoms[i][2]] > -1 and atoms[i][0] + dx[atoms[i][2]] > -1:
            #     for find in range(i+1, atom_num):
            #         if atoms[i][1] + dy[atoms[i][2]] == atoms[find][1] and atoms[i][0] + dx[atoms[i][2]] == atoms[find][0]:
            #             visited[find] = 1
            #         else:
            #             visited[i] = 1
            #             base[atoms[i][1]][atoms[i][0]] = 0
            #             if base[atoms[i][1] + dy[atoms[i][2]]][atoms[i][0] + dx[atoms[i][2]]] != 0:
            #                 collapse += atoms[i][3] + base[atoms[i][1] + dy[atoms[i][2]]][atoms[i][0] + dx[atoms[i][2]]]
            #                 base[atoms[i][1] + dy[atoms[i][2]]][atoms[i][0] + dx[atoms[i][2]]] = 0
            #                 atoms[i][3] = 0
            #                 atoms[i][1] = atoms[i][1] + dy[atoms[i][2]]
            #                 atoms[i][0] = atoms[i][0] + dx[atoms[i][2]]
            #             elif base[atoms[i][1] + dy[atoms[i][2]]][atoms[i][0] + dx[atoms[i][2]]] == 0:
            #                 atoms[i][1] = atoms[i][1] + dy[atoms[i][2]]
            #                 atoms[i][0] = atoms[i][0] + dx[atoms[i][2]]
            #                 base[atoms[i][1]][atoms[i][0]] = atoms[i][3]
    # print('#{} {}'.format(test_num, collapse))