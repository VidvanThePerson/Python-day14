def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(words) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List of words with first and last letter same \n",lst)
    return ctr
count =match_words(["abc","cfc","fjs","ksk","kok","joj","1122211"])
print("Amount of words with first and last letter same:",count)
