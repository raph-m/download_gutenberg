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


