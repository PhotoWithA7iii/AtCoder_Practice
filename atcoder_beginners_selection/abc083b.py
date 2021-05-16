N, A, B = map(str, input().split())

sum = 0
for i in range(1, int(N)+1):
    num = str(i)
    l = len(num)

    tmp = 0
    for j in range(l):
        tmp += int(num[j])

    if int(A) <= tmp <= int(B):
        sum += i

print(sum)

