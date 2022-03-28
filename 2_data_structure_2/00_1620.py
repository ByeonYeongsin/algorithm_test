# 나는야 포켓몬 마스터 이다솜

import sys

N, M = map(int, sys.stdin.readline().split())
pokemon_dict = {}

for i in range(N):
    now_pokemon = sys.stdin.readline().strip()
    pokemon_dict[i+1] = now_pokemon
    pokemon_dict[now_pokemon] = i+1

for j in range(M):
    now_ques = sys.stdin.readline().strip()
    if now_ques.isalpha(): # 오로지 알파벳, 한글만 있어야 True, 빈 칸도 안됨
    # .isdigit() => 숫자인지 판단
        print(pokemon_dict[now_ques])
    else:
        print(pokemon_dict[int(now_ques)])
