"""
kanekojunjunoMacBook-Pro:part2 kanekojunki$ python q16.py 3
kanekojunjunoMacBook-Pro:part2 kanekojunki$ cd q16
kanekojunjunoMacBook-Pro:q16 kanekojunki$ ls -l | grep row | wc -l
       8
kanekojunjunoMacBook-Pro:q16 kanekojunki$ split -l 3 ../hightemp.txt
kanekojunjunoMacBook-Pro:q16 kanekojunki$ ls -l | grep x | wc -l
       8
kanekojunjunoMacBook-Pro:q16 kanekojunki$
"""

import sys

if __name__ == '__main__':
    n = int(sys.argv[1])
    # target_file = sys.argv[2] # 毎回入力するのは面倒なので
    target_file = './hightemp.txt'

    with open(target_file) as f:
        lines = f.readlines()

    for i in range(0, len(lines), n):
        with open('./q16/row%dto%d' % (i, i+n), 'w') as f:
            f.writelines(lines[i:i+n])