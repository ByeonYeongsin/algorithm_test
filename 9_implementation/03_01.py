# 8진수 2진수
import sys

# num = sys.stdin.readline().strip()
# num_binary = ''

# for now_num in num:
#     now_num = int(now_num)
#     num_binary += str(now_num // 4)
#     now_num %= 4
#     num_binary += str(now_num // 2)
#     now_num %= 2
#     num_binary += str(now_num // 1)

# if num_binary[0] == '0':
#     print(num_binary[1::1])
# else:
#     print(num_binary[::1])

print(bin(int(sys.stdin.readline().strip(), 8))[2:])
