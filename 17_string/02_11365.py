# !밀비 급일
import sys

while(True):
    str = sys.stdin.readline().strip()
    if str == 'END':
        break
    print(str[::-1])