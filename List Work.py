print("This Program will take a list of strings from the user and find a specific keyword in it")

user_in = input("Enter your doc list with commas: ")
doc_list = [i.strip() for i in user_in.split(',')]
keyword = input("Enter keyword(s) to find: ")
doc_keyword = [k.strip() for k in keyword.split(',')]
def find_keyword_in_list(doc_list, keywords):
    indices = []
    for i, item in enumerate(doc_list):
        if item in keywords:
            indices.append(i)
    return indices
def find_keyword_in_sentences(doc_list, keyword):
    indices = []
    for i, sent in enumerate(doc_list):
        if keyword.lower() in sent.lower():
            indices.append(i)
    return indices
indec = find_keyword_in_list(doc_list, doc_keyword)
print("Found exact keywords at index positions:", indec)
single_keyword = input("Enter one word to search inside sentences: ")
sentence_indec = find_keyword_in_sentences(doc_list, single_keyword)
print("Keyword found inside sentences at positions:", sentence_indec)
