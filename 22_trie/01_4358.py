# 생태학

import sys

trees = {}
sum = 0

# defaultdict(int)

while True:
    now_tree = sys.stdin.readline().rstrip()
    if not now_tree:
        break

    if now_tree in trees:
        trees[now_tree] += 1
    else:
        trees[now_tree] = 1
    sum += 1

    # trees[now_tree] += 1
    # sum += 1

sorted_trees = sorted(trees.items())
for key, value in sorted_trees:
    print('%s %.4f' %(key, (value/sum*100)))

# tree_key = list(trees.keys())
# tree_key.sort()
# for tree in tree_key:
# print('%s %.4f' %(tree, trees[tree]/sum*100))