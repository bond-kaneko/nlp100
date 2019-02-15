"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

kanekojunjunoMacBook-Pro:part4 kanekojunki$ python q30.py
{'surface': '一', 'base': '一', 'pos': '名詞', 'pos1': '*'}
{'surface': '\u3000', 'base': '\u3000', 'pos': '記号', 'pos1': '*'}
{'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '一般'}
{'surface': 'は', 'base': 'は', 'pos': '助詞', 'pos1': '*'}
{'surface': '猫', 'base': '猫', 'pos': '名詞', 'pos1': '*'}
{'surface': 'で', 'base': 'だ', 'pos': '助動詞', 'pos1': '*'}
{'surface': 'ある', 'base': 'ある', 'pos': '助動詞', 'pos1': '*'}
{'surface': '。', 'base': '。', 'pos': '記号', 'pos1': '*'}
{'surface': '名前', 'base': '名前', 'pos': '名詞', 'pos1': '*'}
{'surface': 'は', 'base': 'は', 'pos': '助詞', 'pos1': '*'}
kanekojunjunoMacBook-Pro:part4 kanekojunki$
"""

import re

def parse_neko():
    with open('./neko.txt.mecab', 'r') as f:
        raw_list = f.readlines()

    rows_elements = []
    for row in raw_list:
        sp_row = re.split('\t|,|\n', row)
        rows_elements.append(sp_row)


    morpheme_list = []
    for elems in rows_elements:
        if elems[0] == 'EOS':
            continue

        morpheme_dict = {'surface': elems[0], 'base': elems[7], 'pos': elems[1], 'pos1': elems[3]}
        morpheme_list.append(morpheme_dict)

    return morpheme_list

if __name__ == "__main__":
    neko_list = parse_neko()
    # 長いので一部だけ表示
    for mopheme in neko_list[:10]:
        print(mopheme)