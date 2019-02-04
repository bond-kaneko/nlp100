"""
kanekojunjunoMacBook-Pro:part2 kanekojunki$ python q12.py
kanekojunjunoMacBook-Pro:part2 kanekojunki$ diff <(cat q12/col1.txt) <(cut -f 1 hightemp.txt)
kanekojunjunoMacBook-Pro:part2 kanekojunki$ diff <(cat q12/col2.txt) <(cut -f 2 hightemp.txt)
kanekojunjunoMacBook-Pro:part2 kanekojunki$
"""

if __name__ == "__main__":
    with open('./hightemp.txt') as f:
        lines = f.readlines()

    parsed_lines = [line.split('\t') for line in lines]

    col1_list = [line[0] for line in parsed_lines]
    col2_list = [line[1] for line in parsed_lines]

    col1_str = '\n'.join(col1_list) + '\n'
    col2_str = '\n'.join(col2_list) + '\n'

    with open('./q12/col1.txt', 'w') as f:
        f.write(col1_str)

    with open('./q12/col2.txt', 'w') as f:
        f.write(col2_str)