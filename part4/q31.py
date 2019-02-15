"""
31. 動詞
動詞の表層形をすべて抽出せよ．

kanekojunjunoMacBook-Pro:part4 kanekojunki$ python q31.py
{'surface': '生れ', 'base': '生れる', 'pos': '動詞', 'pos1': '*'}
{'surface': 'つか', 'base': 'つく', 'pos': '動詞', 'pos1': '*'}
{'surface': 'し', 'base': 'する', 'pos': '動詞', 'pos1': '*'}
{'surface': '泣い', 'base': '泣く', 'pos': '動詞', 'pos1': '*'}
{'surface': 'し', 'base': 'する', 'pos': '動詞', 'pos1': '*'}
{'surface': 'いる', 'base': 'いる', 'pos': '動詞', 'pos1': '*'}
{'surface': '始め', 'base': '始める', 'pos': '動詞', 'pos1': '*'}
{'surface': '見', 'base': '見る', 'pos': '動詞', 'pos1': '*'}
{'surface': '聞く', 'base': '聞く', 'pos': '動詞', 'pos1': '*'}
{'surface': '捕え', 'base': '捕える', 'pos': '動詞', 'pos1': '*'}
kanekojunjunoMacBook-Pro:part4 kanekojunki$
"""

import q30

if __name__ == "__main__":
    neko_list = q30.parse_neko()

    verbs = []
    for row in neko_list:
        if (row['pos'] == '動詞'):
            verbs.append(row)

    for v in verbs[:10]:
        print(v)