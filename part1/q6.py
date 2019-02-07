import q5

if __name__ == "__main__":
    s1 = "paraparaparadise"
    s2 = "paragraph"

    s1_bi_gram_char = q5.n_gram_char(s1, 2)
    s2_bi_gram_char = q5.n_gram_char(s2, 2)

    s1_bi_set = set(s1_bi_gram_char)
    s2_bi_set = set(s2_bi_gram_char)

    s1_or_s2 = s1_bi_set | s2_bi_set
    print(s1_or_s2)

    s1_and_s2 = s1_bi_set & s2_bi_set
    print(s1_and_s2)

    s1_minus_s2 = s1_bi_set - s2_bi_set
    print(s1_minus_s2)

    s1_contain_se = "se" in s1_bi_set
    s2_contain_se = "se" in s2_bi_set
    print(s1_contain_se)
    print(s2_contain_se)