"""
kanekojunjunoMacBook-Pro:part2 kanekojunki$ python q17.py | sort
千葉県
埼玉県
大阪府
山形県
山梨県
岐阜県
愛媛県
愛知県
群馬県
静岡県
高知県
和歌山県
kanekojunjunoMacBook-Pro:part2 kanekojunki$ cut -f 1 hightemp.txt | sort | uniq | sort
千葉県
埼玉県
大阪府
山形県
山梨県
岐阜県
愛媛県
愛知県
群馬県
静岡県
高知県
和歌山県
kanekojunjunoMacBook-Pro:part2 kanekojunki$ diff <(python q17.py | sort) <(cut -f 1 hightemp.txt | sort | uniq | sort)
kanekojunjunoMacBook-Pro:part2 kanekojunki$
"""

if __name__ == '__main__':
    target_file = './hightemp.txt'
    n = 0

    with open(target_file) as f:
        lines = f.readlines()

    lines = [line.split() for line in lines]
    col_n_list = [line[n] for line in lines]
    col_n_set = set(col_n_list)
    for word in col_n_set:
        print(word)