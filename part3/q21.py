"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．

kanekojunjunoMacBook-Pro:part3 kanekojunki$ python q21.py
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]
"""

import q20

if __name__ == "__main__":
    article_dict = q20.load_json_dict()

    category_row = []
    target_article = article_dict['イギリス']
    for row in target_article.split():
        if 'Category:' in row:
            category_row.append(row)

    for row in category_row:
        print(row)