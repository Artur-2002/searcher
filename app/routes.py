from app import app, db
from .models import Document
from .forms import PostForm
from flask import render_template, request, redirect

@app.route('/', methods=['GET', 'POST'])
def index():
	form = PostForm()
	documents = []
	if request.method == 'POST':
		text = form.text.data

		for document in Document.query.all():
			if len(documents) == 20:
				break

			if text.lower() in document.text.lower():
				documents.append(document)

		documents = sorted(documents, key = lambda x: x.get_created_date())
		
	return render_template('index.html', form=form, documents=documents)


@app.route('/text/<int:id>/')
def get_text(id):
	try:
		document = Document.query.get(id)
	except:
		return "Нет документа с таким id"

	return document.text


@app.route('/delete/<int:id>/')
def delete(id):
	try:
		document = Document.query.get(id)
	except:
		return "Нет документа с таким id"

	db.session.delete(document)
	db.session.commit()
	return redirect('/')

