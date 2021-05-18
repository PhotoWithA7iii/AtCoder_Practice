N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
New_A = []
for i in range(N+1):
    if i == 0:
        New_A.append(A[i])
    elif 0 < i < N:
        New_A.append(A[i]-A[i-1])
    else:
        New_A.append(L-A[i-1])

for 


