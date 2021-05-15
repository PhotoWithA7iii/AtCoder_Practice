S = input()

# count関数を使用する場合
print(S.count('1'))

# count関数を使用しない場合
c = 0
for i in S:
    if i == '1':
        c += 1

print(c)