import sys

if __name__ == "__main__":
    target_doc = sys.argv[1]

    words = target_doc.split(' ')
    words = [word.replace(',', '') for word in words]
    words = [word.replace('.', '') for word in words]

    result = [len(word) for word in words]
    print(result)

