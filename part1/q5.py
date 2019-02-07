import sys

def n_gram_char(doc, n):
    words_tmp = doc.split(' ')
    words_tmp = [word.replace(',', '') for word in words_tmp]
    word_list = [word.replace('.', '') for word in words_tmp]

    target_str = ''.join(word_list)

    ngram = []
    for i in range(len(target_str)):
        if (i + n > len(target_str)):
            break
        ngram.append(target_str[i:i+n])

    return ngram

# charの方と共通化できそう
def n_gram_word(doc, n):
    words_tmp = doc.split(' ')
    words_tmp = [word.replace(',', '') for word in words_tmp]
    word_list = [word.replace('.', '') for word in words_tmp]

    ngram = []
    for i in range(len(word_list)):
        if (i + n > len(word_list)):
            break
        ngram.append(word_list[i:i+n])
    return ngram



if __name__ == "__main__":
    target_doc = sys.argv[1]

    bi_gram_char = n_gram_char(target_doc, 2)
    bi_gram_word = n_gram_word(target_doc, 2)

    print(bi_gram_char)
    print(bi_gram_word)