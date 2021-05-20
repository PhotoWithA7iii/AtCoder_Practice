def Parentheses_function(S):
    new_S = []
    for k in S:
        new_S.append('(' + k + ')')
        new_S.append(k + '()')
        new_S.append('()' + k)
        
    return new_S

if __name__ == "__main__":
    N = int(input())
    S = ['()']
    C_S = []
    LR_S = []
    if N % 2 == 0 and N > 2:
        for i in range(N//2 - 1):
            C_S.append(Parentheses_function(S))
            S = sum(C_S, [])

    for n in set(S):
        if len(n) == N:
            print(n)