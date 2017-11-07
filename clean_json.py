import json

f_index = open("index_after_cleaning.json", "r")

index_text = f_index.read()
index = json.loads(index_text)

new_index = []

for d in index:
    author = d["author"]
    id = d["id"]

    if d["cleaned"] == "success":

        with open("truncated_books/" + str(id) + ".txt", 'r') as fin:
            data = fin.read().splitlines(True)
            lines = len(data)

        new_index.append({
            "author": d["author"],
            "title": d["title"],
            "number_of_lines": lines
        })

f = open("final_index.json", 'w')
f.write(json.dumps(new_index))
