import collections
# collections.deque


def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result


# m = [69, 10, 30, 2, 16, 8, 31, 22]
#
# print(merge_sort(m))

b = collections.deque([1, 5, 2, 4, 3])
a = [1, 5, 2, 4, 3]
q =[]
for i in range(len(b)):
    if len(q) == 0:
        q.append(b[i])
        print('처음', q)
    else:
        for j in range(len(q)):
            if b[i] > q[j]:
                if j == len(q)-1:
                    q.insert(j+1, b[i])
                    print('ㅁㅁ', q)
                    break
                pass
            elif b[i] < q[j]:
                q.insert(j, b[i])
                print(q)

print(q)

#
c = ['a']
c.extend(b)
print(c)
print(type(c))
print(type(b))

