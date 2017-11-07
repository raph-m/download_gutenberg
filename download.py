import urllib.request
import json

f_index = open("index.json", "r")

index_text = f_index.read()
index = json.loads(index_text)

url_format_1 = "http://www.gutenberg.org/cache/epub/{1}/pg{0}.txt"
url_format_2 = "http://www.gutenberg.org/cache/epub/{1}/{0}.txt"
url_format_3 = "http://www.gutenberg.org/cache/epub/{1}/{0}-0.txt"
url_format_4 = "http://www.gutenberg.org/cache/epub/{1}/pg{0}-0.txt"

url_formats = [url_format_1, url_format_2, url_format_3, url_format_4]

compteur = 0
total = len(index)
print("total to download: "+str(total))
success_count = 0

for d in index:
    compteur += 1
    if compteur % 30 == 0:
        print(str(compteur)+" files parsed")
        print(str(compteur*100.0/total)+"% effectués")
        print("number of success: "+str(success_count))
        print("************************************")

    id = d["id"]

    success = False

    for url_format in url_formats:

        url = url_format.format(id, id)
        try:
            response = urllib.request.urlopen(url)
            d.update({"download": "success"})
        except:
            print("file "+str(id)+" didnt download")
            d.update({"download": "failed"})
            print("download failed")
            continue

        data = response.read()  # a `bytes` object
        try:
            text = data.decode('utf-8')  # a `str`; this step can't be used if data is binary
            success = True
        except:
            d.update({"decode": "failed"})
            print("decode failed for file number "+str(id))
            continue

        if success:
            break

    if success:
        f = open("downloaded/"+str(id)+".txt", 'w')
        f.write(text)
        f.close()
        d.update({"decode": "success"})
        success_count += 1


f = open("index_after_download.json", 'w')
f.write(json.dumps(index))
