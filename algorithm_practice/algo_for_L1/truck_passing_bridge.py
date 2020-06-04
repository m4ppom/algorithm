def solution(bridge_length, weight, truck_weights):
    answer = 0
    end = 0
    movin = 0
    the_one = 0
    last_num = 0
    len_truc = len(truck_weights)
    visited = [0] * len_truc
    while end != len_truc:
        for i in range(len_truc):
            if i > last_num + 2:
                break
            if the_one:
                the_one = 0
                answer -= 1
                break
            else:

                if visited[i] == 0:
                    if movin + truck_weights[i] <= weight and i == last_num + 1:
                        movin += truck_weights[i]
                        visited[i] = 1
                        the_one = 1
                        last_num = i
                        break

                elif visited[i] < bridge_length:
                    visited[i] += 1

                elif visited[i] == bridge_length:
                    movin -= truck_weights[i]
                    visited[i] = 777
                    end += 1

        answer += 1

    return answer