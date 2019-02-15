"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．

kanekojunjunoMacBook-Pro:part3 kanekojunki$ python q24.py
BenNevis2005.jpg
London.bankofengland.arp.jpg
Anglospeak.svg
kanekojunjunoMacBook-Pro:part3 kanekojunki$
音声ファイルはなかった
"""

import q20
import re

if __name__ == "__main__":
    article_dict = q20.load_json_dict()

    target_article = article_dict['イギリス']

    file_pattern = re.compile('\[\[.*File:.*\]\]')
    head_pattern = re.compile('\[\[File:')
    tail_pattern = re.compile('\|.*\]\]')
    file_rows = []
    for row in target_article.split():
        re_result = file_pattern.match(row)
        if re_result:
            filename = head_pattern.sub('', re_result.group())
            filename = re.sub('\|.*\]\]', '', filename)
            file_rows.append(filename)

    for row in file_rows:
        print(row)