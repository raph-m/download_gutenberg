import json
import numpy as np

f_index = open("index_after_cleaning.json", "r")

index_text = f_index.read()
index = json.loads(index_text)

selected_authors_txt = open("selected_authors").read()

selected_authors = selected_authors_txt.split("\n")

book_count = np.zeros(len(selected_authors))
lines_count = np.zeros(len(selected_authors))


def get_number_of_author(author):

    for i in range(len(selected_authors)):
        if selected_authors[i] == author:
            return i
    else:
        print("weird stuff")
        print(author)
        return 0


for d in index:
    author = d["author"]
    id = d["id"]

    if d["cleaned"] == "success":
        with open("truncated_books/" + str(id) + ".txt", 'r') as fin:
            data = fin.read().splitlines(True)
            lines_count[get_number_of_author(author)] += len(data)
            book_count[get_number_of_author(author)] += 1


for i in range(len(selected_authors)):
    if book_count[i] > 0.5:
        print(selected_authors[i])
        print(book_count[i])
        print(lines_count[i])
