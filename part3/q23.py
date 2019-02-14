"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

(root) kanekojunjunoMacBook-Pro:part3 kanekojunki$ python q23.py
Section name: 国名
Section level 1

Section name: 歴史
Section level 1

Section name: 地理
Section level 1

Section name: 気候
Section level 2

Section name: 政治
Section level 1

... 長いので省略

Section name: 関連項目
Section level 1

Section name: 外部リンク
Section level 1

(root) kanekojunjunoMacBook-Pro:part3 kanekojunki$
"""

import q20
import re

if __name__ == "__main__":
    article_dict = q20.load_json_dict()

    section_pattern = re.compile('^===?.*===?$')
    sections = []
    target_article = article_dict['イギリス']
    for row in target_article.split():
        section = section_pattern.match(row)
        if section:
            section_name = re.sub('=', '', section.group())
            section_level = int((section.group().count('=') / 2) - 1)
            sections.append({'name': section_name, 'level': section_level})

    for row in sections:
        print('Section name:', row['name'])
        print('Section level', row['level'])
        print()