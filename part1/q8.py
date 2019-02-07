def cipher(doc):
    ci_doc = ''
    for c in doc:
        if c.islower():
            ci_doc += chr(219 - ord(c))
        else:
            ci_doc += c

    return ci_doc

if __name__ == '__main__':
    doc = 'HOGEhoge'

    ci_doc = cipher(doc)
    print(ci_doc)