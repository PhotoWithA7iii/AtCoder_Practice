S = str(input())
l = ["eraser", "dreamer", "dream", "erase"]
S = S.replace(l[0],"")
S = S.replace(l[3],"")
S = S.replace(l[1],"")
S = S.replace(l[2],"")
print("YES" if len(S)==0 else "NO")