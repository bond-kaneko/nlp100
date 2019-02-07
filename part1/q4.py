import sys

if __name__ == "__main__":
    target_doc = sys.argv[1]

    words_tmp = target_doc.split(' ')
    words_tmp = [word.replace(',', '') for word in words_tmp]
    words = [word.replace('.', '') for word in words_tmp]

    pick_first_at = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    pick_firsts = []
    pick_seconds = []

    results = {}
    for i in range(len(words)):
        if (i in pick_first_at):
            results[words[i][:1]] = i
        else:
            results[words[i][:2]] = i

    print(results)

