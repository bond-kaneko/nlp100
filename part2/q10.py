"""
(root) kanekojunjunoMacBook-Pro:part2 kanekojunki$ python q10.py
24
(root) kanekojunjunoMacBook-Pro:part2 kanekojunki$ wc hightemp.txt
      24      98     813 hightemp.txt
(root) kanekojunjunoMacBook-Pro:part2 kanekojunki$
"""

if __name__ == "__main__":
    row_count = 0
    with open('./hightemp.txt') as f:
        lines = f.readlines()

    print(len(lines))