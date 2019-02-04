"""
kanekojunjunoMacBook-Pro:part2 kanekojunki$ python q11.py
kanekojunjunoMacBook-Pro:part2 kanekojunki$ expand -t 1 hightemp.txt > q11-ans.txt
kanekojunjunoMacBook-Pro:part2 kanekojunki$ diff q11.txt q11-ans.txt
kanekojunjunoMacBook-Pro:part2 kanekojunki$
"""

if __name__ == "__main__":
    with open('./hightemp.txt') as f:
        lines = f.readlines()

    writeLines = [line.replace('\t', ' ') for line in lines]

    with open('./q11/q11.txt', 'w') as f:
        f.writelines(writeLines)
