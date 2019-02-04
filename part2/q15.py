"""
kanekojunjunoMacBook-Pro:part2 kanekojunki$ python q15.py 3
山梨県	大月	39.9	1990-07-19
山形県	鶴岡	39.9	1978-08-03
愛知県	名古屋	39.9	1942-08-02
kanekojunjunoMacBook-Pro:part2 kanekojunki$ tail -n 3 hightemp.txt
山梨県	大月	39.9	1990-07-19
山形県	鶴岡	39.9	1978-08-03
愛知県	名古屋	39.9	1942-08-02
kanekojunjunoMacBook-Pro:part2 kanekojunki$ diff <(python q15.py 3) <(tail -n 3 hightemp.txt)
kanekojunjunoMacBook-Pro:part2 kanekojunki$
"""

import sys

if __name__ == '__main__':
    n = int(sys.argv[1])
    # target_file = sys.argv[2] # 毎回入力するのは面倒なので
    target_file = './hightemp.txt'

    with open(target_file) as f:
        lines = f.readlines()

    # 一応lengthチェック
    lines_len = len(lines)
    if (n > lines_len):
        n = lines_len

    for i in range(lines_len - n, lines_len):
        print(lines[i], end='') # 二重改行防止