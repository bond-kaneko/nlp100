"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ

長いので解答例省略
"""



import json

def load_json_dict(filename = 'jawiki-country.json'):
    with open(filename) as f:
        articles_str = f.readlines()

        article_dict = {}
        for article in articles_str:
            article_json = json.loads(article)
            article_dict.update({article_json['title']: article_json['text']})

    return article_dict

if __name__ == "__main__":
    article_dict = load_json_dict('jawiki-country.json')
    print(article_dict['イギリス'])