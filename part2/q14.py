"""
kanekojunjunoMacBook-Pro:part2 kanekojunki$ python q14.py 3
高知県	江川崎	41	2013-08-12
埼玉県	熊谷	40.9	2007-08-16
岐阜県	多治見	40.9	2007-08-16
kanekojunjunoMacBook-Pro:part2 kanekojunki$ diff <(head -n 3 hightemp.txt) <(python q14.py 3)
kanekojunjunoMacBook-Pro:part2 kanekojunki$
"""

import sys

if __name__ == "__main__":
    n = int(sys.argv[1])
    # target_file = sys.argv[2] # 毎回入力するのは面倒なので
    target_file = './hightemp.txt'

    with open(target_file) as f:
        lines = f.readlines()

    # 一応lengthチェック
    if (n > len(lines)):
        n = len(lines)

    for i in range(n):
        print(lines[i], end='') # 二重改行防止