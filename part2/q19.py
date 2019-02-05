"""
kanekojunjunoMacBook-Pro:part2 kanekojunki$ python q19.py
3 群馬県
3 山梨県
3 山形県
3 埼玉県
2 静岡県
2 愛知県
2 岐阜県
2 千葉県
1 高知県
1 愛媛県
1 大阪府
1 和歌山県
kanekojunjunoMacBook-Pro:part2 kanekojunki$ cut -f 1 hightemp.txt | sort | uniq -c | sort -gr
   3 群馬県
   3 山梨県
   3 山形県
   3 埼玉県
   2 静岡県
   2 愛知県
   2 岐阜県
   2 千葉県
   1 和歌山県
   1 高知県
   1 愛媛県
   1 大阪府
kanekojunjunoMacBook-Pro:part2 kanekojunki$
"""


if __name__ == '__main__':
    target_file = './hightemp.txt'

    with open(target_file) as f:
        lines = f.readlines()
    lines = [line.split() for line in lines]

    col1_list = [line[0] for line in lines]
    col1_list = sorted(col1_list, reverse=True)

    freq_map = {word: 0 for word in col1_list}
    for word in col1_list:
        freq_map[word] += 1

    freq_map = sorted(freq_map.items(), key=lambda freq_map: -freq_map[1])

    for fmap in freq_map:
        print(fmap[1], fmap[0])