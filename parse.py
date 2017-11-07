import rdflib
from get_author import get_author, get_title, get_language
from pprint import pprint
import json

ressources_txt = open("files.txt").read()

ressources = ressources_txt.split("\n")

selected_authors_txt = open("selected_authors").read()

selected_authors = selected_authors_txt.split("\n")
print(selected_authors)

index = []

j = 0

for r in ressources:
    j += 1

    if j % 1000 == 0:
        print("***********************"+str(j)+"********************")

    file_format = "../epub/{1}/pg{0}.rdf".format(r, r)

    try:
        text = open(file_format, 'r', encoding='utf-8').read()
    except:
        print("file number "+str(r)+" was not found")
        continue

    is_author = False
    txt_exists = False
    author = get_author(text)
    language = get_language(text)
    title = get_title(text)

    if author in selected_authors:
        if language == "en":
            index.append({
                "id": r,
                "author": author,
                "title": title,
                "download": "not yet",
                "decode": "not yet",
                "novel": "not yet",
                "cleaned": "no"
            })

print(index)
f = open("index.json", 'w')
f.write(json.dumps(index))

