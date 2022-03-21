# 괄호

N = int(input())
result = ""

for i in range(N):
    testcase = input()
    cnt = 0
    for c in testcase:
        cnt += 1 if c == '(' else -1
        if cnt < 0:
            result += "NO\n"
            break
    else: # for else 구문
        result += "YES\n" if cnt == 0 else "NO\n"

print(result)