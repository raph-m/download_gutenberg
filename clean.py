import json
import os

f_index = open("index_after_download.json", "r")

index_text = f_index.read()
index = json.loads(index_text)


def truncate():
    answer = input("are you sure you want to truncate all the files in the 'downloaded' folder and "
                   "put them in the 'truncated' folder ? y/n")
    if answer == "y":
        for d in index:

            if d["decode"] == "success":
                id = d["id"]
                print("truncating file " + str(id))

                with open("downloaded/" + str(id) + ".txt", 'r') as fin:
                    data = fin.read().splitlines(True)
                with open("truncated_books/" + str(id) + ".txt", 'w') as fout:
                    fout.writelines(data[350:len(data)-500])
    else:
        print("truncation aborted")


def delete_too_small_files():
    answer = input("are you sure you want to delete the files that are smaller than 2000 lines ?? y/n")
    if answer == "y":
        delete_count = 0
        for d in index:

            if d["decode"] == "success":
                id = d["id"]
                must_delete = False
                with open("truncated_books/" + str(id) + ".txt", 'r') as fin:
                    data = fin.read().splitlines(True)
                    if len(data) < 2000:
                        must_delete = True
                if must_delete:
                    print("deleting file number "+str(id))
                    os.remove("truncated_books/" + str(id) + ".txt")
                    delete_count += 1
                    d.update({"cleaned": "failed"})
                else:
                    d.update({"cleaned": "success"})
        print("number of files: "+str(len(index)))
        print("number of files deleted: "+str(delete_count))
        f = open("index_after_cleaning.json", 'w')
        f.write(json.dumps(index))
    else:
        print("deletion aborted")


delete_too_small_files()
