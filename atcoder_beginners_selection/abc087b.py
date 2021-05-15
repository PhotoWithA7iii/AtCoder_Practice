# A = int(input())
# B = int(input())
# C = int(input())
# X = int(input())

# cnt = 0
# yen_500 = X // 500
# for i in range(A+1):
#     X_1 = X
#     X_1 -= 500*i

#     if X_1 < 0:
#         break

#     yen_100 = X_1 // 100
#     for j in range(B+1):
#         X_2 = X_1
#         X_2 -= 100*j

#         if X_2 < 0:
#             break

#         if X_2 == 0:
#             cnt += 1
#         elif X_2 > 0 and X_2 // 50 <= C:
#             cnt += 1


# print(cnt)

A, B, C, X = [int(input()) for i in range(4)]
print(sum(500*a+100*b+50*c == X for a in range(A+1) for b in range(B+1) for c in range(C+1)))