from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)
app.jinja_env.globals.update(reversed=reversed)
app.jinja_env.globals.update(len=len)

def tenlines(string):
	linelist = string.splitlines(True)
	lines = ""
	if len(linelist) > 10:
		for i in range(10):
			lines += linelist[i]
	else:
		for line in linelist:
			lines += line
	return lines

app.jinja_env.globals.update(tenlines=tenlines)

class article:
	def __init__(self, ID, date, title, content, tags):
		self.ID = ID
		self.date = date
		self.title = title
		self.content = content
		self.tags = tags


articles = []

@app.route("/", methods=["GET", "POST"])
def index():

	if request.method == "GET":

		db = SQL("sqlite:///longlongdouble.db")

		articles.clear()
		rows = db.execute("SELECT * FROM articles")

		for row in rows:
			articles.append(article(
				row["id"],
				row["date"],
				row["title"],
				row["content"],
				row["tags"].split(", ")
			))
			
		return render_template("index.html", articles=articles)

	else:

		keywords = request.form.get("search")

		if not keywords:
			ID = int(request.form.get("id"))

			for entry in articles:
				if entry.ID == ID:
					selected_article = entry

			return render_template("article.html", article=selected_article)

		else:

			for entry in articles:
				if not (keywords in entry.title or keywords in entry.tags):
					articles.remove(entry)

			return render_template("index.html", articles=articles)