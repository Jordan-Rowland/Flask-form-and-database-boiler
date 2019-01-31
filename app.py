from flask import redirect, render_template, url_for
from project import app, db
from project.forms import BookForm, RemoveBook
from project.models import Book


@app.route('/addbook', methods=['GET', 'POST'])
def addbook():

    form = BookForm()

    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            genre=form.genre.data)

        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RemoveBook()
    books = Book.query.all()

    if form.validate_on_submit():
        book = Book.query.filter_by(id=form.id.data).first()
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('index.html', books=books, form=form)

if __name__ == '__main__':
    app.run(debug=True)
