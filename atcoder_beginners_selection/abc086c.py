N = int(input())
data = [[0, 0, 0]]
flag = 0
for n in range(N):
    data.append(list(map(int, input().split())))

    if (abs(data[n][0] - data[n+1][0]) - abs(data[n][1] - data[n+1][1]) + abs(data[n][2] - data[n+1][2])) % 2 == 0 \
        and abs(data[n][0] - data[n+1][0]) >= abs(data[n][1] - data[n+1][1]) + abs(data[n][2] - data[n+1][2]):
        pass
    else:
        flag = 1

if flag == 0:
    print('Yes')
else:
    print('No') 