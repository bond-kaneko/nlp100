"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

(root) kanekojunjunoMacBook-Pro:part3 kanekojunki$ python q22.py
イギリス
英連邦王国
G8加盟国
欧州連合加盟国
海洋国家
君主国
島国
1801年に設立された州・地域
(root) kanekojunjunoMacBook-Pro:part3 kanekojunki$
"""

import q20
import re

if __name__ == "__main__":
    article_dict = q20.load_json_dict()

    category_pattern = re.compile('.*Category:.*')
    category_row = []
    target_article = article_dict['イギリス']
    for row in target_article.split():
        result = category_pattern.match(row)
        if result:
            # もっといい方法があるはず
            category_name = re.sub('^\[\[Category:', '', result.group())
            category_name = re.sub('\]\]', '', category_name)
            category_name = re.sub('\|.*', '', category_name)
            category_row.append(category_name)

    for row in category_row:
        print(row)