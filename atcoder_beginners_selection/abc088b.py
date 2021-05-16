N = int(input())
a_l = list(map(int, input().split()))
a_l.sort(reverse=True)
Alice = 0
Bob = 0
for i, item in enumerate(a_l, 1):
    if i % 2 != 0:
        Alice += item
    else:
        Bob += item

print(Alice - Bob)