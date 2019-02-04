"""
kanekojunjunoMacBook-Pro:part2 kanekojunki$ python q13.py
kanekojunjunoMacBook-Pro:part2 kanekojunki$ diff <(cat q13/col1_col2.txt) <(paste q12/col1.txt q12/col2.txt)
kanekojunjunoMacBook-Pro:part2 kanekojunki$
"""

if __name__ == "__main__":
    with open('./q12/col1.txt') as f:
        col1 = [line.replace('\n', '') for line in f.readlines()]
    with open('./q12/col2.txt') as f:
        col2 = [line.replace('\n', '') for line in f.readlines()]

    with open('./q13/col1_col2.txt', 'w') as f:
        for c1, c2 in zip(col1, col2):
            f.write(c1 + '\t' + c2 + '\n')
