N = int(input())
A = list(map(int, input().split()))

Flag = True
c = 0
while Flag:
    Flag = all(item % 2 == 0 for item in A)
    tmp = []

    if Flag == False:
        print(c)
        break
    else:
        tmp = list(map(lambda x: x//2, A))
        A = tmp
        c += 1