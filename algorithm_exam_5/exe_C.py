N = int(input())

s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if N == 0:
    print(0)
    exit()

a = ""
while N:
    a = s[N % 36] + a
    N //= 36

print(a)