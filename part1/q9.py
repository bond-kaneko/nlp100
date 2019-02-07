import random

if __name__ == "__main__":
    doc = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    word_list = doc.split(' ')

    fixed_i = [0, len(word_list) - 1] # 並び替えない単語の番号
    for i, word in enumerate(word_list):
        if len(word) < 5:
            fixed_i.append(i)

    # ここは醜い
    shuffle_i = list( set(range(len(word_list))) - set(fixed_i) )

    result_list = []
    for i in range(0, len(word_list)):
        if i in fixed_i:
            result_list.append(word_list[i])
        else:
            random.shuffle(shuffle_i)
            picked_i = shuffle_i.pop()
            result_list.append(word_list[picked_i])
    
    result_doc = ' '.join(result_list)

    print(result_doc)