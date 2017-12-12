# download_gutenberg

A Python script to download specific authors using the Gutenberg project.
The goal of this repostory is to create the database for the author_classification project.

Next to this repository you should have the epub folder wich contains references of all books in the Gutenberg database.
The epub folder contains folders with the format of the folders /46 and /41970. You can find the epub folder on the project Gutenberg website.

The get_author file enables you to look at the infos you want on the epub files. (author, title, language)
I did not find a way to extract the type of book (novel, poems, etc), it appears that it is not stored on the epub files.

The parse file parses the epub folder and find the references of books you are interested in. (for example you might be interested by specific authors). There are put in a json so you can access easely this data.

The download file downloads files found in the index.json.

files.txt is the full list of authors for each rdf file found in the epub folder.

selected_authors is the list of authors we wanted to have for our database. This list comes from https://www.theguardian.com/books/2015/aug/17/the-100-best-novels-written-in-english-the-full-list, a list of english novelist given by the Guardian. The most recent authors (after Fitzgerald) are not present in the database.

clean.py is a script to truncate the files (so you can get rid of the License at the beginning and at the end). It also
allows you to delete the files that are considered too small.

the stats.py file helps you to explore the results (count of book for each author, count of lines)

In the file notes you can find my personal notes. At the end you can see the result of the stats.py script/

