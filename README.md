# Longlongdouble
My personal blog to post CS related stuff

### Project Description
This blog is made using the Flask pyhton framework. The application loads all the articles stored in the database and previews them on the index (home) page. Clicking on 'Read More' on an any post preview opens the article for reading. The project uses [Disqus](disqus.com) to host blog comments. The comment section is unique for each indivisual post. It also uses [Bootstrap](getbootstrap.com) CSS libraries for styling.

### Database Schema
The database file longlongdouble.db has the following structure
| Artribute      | Properties | Description |
| -------------- | ---------- | ----------- |
|id| INTEGER PRIMARY KEY AUTOINCREMENT|ID of the article
|date|DTAE|Publish Date|
|title|TEXT|Title of the article|
|content|TEXT|Content of the article|
|tags|TEXT|Article Tags|

**NOTE :** 'content' of an article can be plain text or html fromated text.
**NOTE :** The tags must be seperated by a comma (,) and a space

### Usage
The application automatically reads the articles from the database and generates previews for the blog. All the publisher has to do is to insert the article into the SQLite database.

The previews generated for the index page contain either the first 1000 characters or the first 10 lines (whichever comes first) of your content text or html. Thus the publisher has to make sure to close any open html tags before the 1000th character or the end of the 10th line.

Clicking on 'Read More' opens the entire article for reading with a comment section below.

**NOTE :** If your content is stored as html make sure to double-up single quote or double quote characters.

### Compatibility
- The website runs perfectly on latest versions of all major web browsers.
- The website is not designed for potrait displays but works on mobile devices.
- Javascript is not required to be enabled to run the website.