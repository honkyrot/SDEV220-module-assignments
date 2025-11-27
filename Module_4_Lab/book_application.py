from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# flask app and database setup
app = Flask(__name__)
# ensure the SQLite file is created inside the Module_4_Lab folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "books.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# database model
class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	book_name = db.Column(db.String(120), nullable=False)
	author = db.Column(db.String(120), nullable=False)
	publisher = db.Column(db.String(120), nullable=False)

	def to_dict(self):
		return {
			"id": self.id,
			"book_name": self.book_name,
			"author": self.author,
			"publisher": self.publisher,
		}


@app.route("/")
def index():
	return jsonify({"message": "Book API is running"})


# create
@app.route("/books", methods=["POST"])
def create_book():
	data = request.get_json(silent=True) or {}
	required = ["book_name", "author", "publisher"]
	missing = [k for k in required if not data.get(k)]
	if missing:
		return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

	book = Book(
		book_name=data["book_name"],
		author=data["author"],
		publisher=data["publisher"],
	)
	db.session.add(book)
	db.session.commit()
	return jsonify(book.to_dict()), 201


# read all
@app.route("/books", methods=["GET"])
def get_books():
	books = Book.query.all()
	return jsonify({"books": [b.to_dict() for b in books]})


# read one
@app.route("/books/<int:id>", methods=["GET"])
def get_book(id: int):
	book = Book.query.get_or_404(id)
	return jsonify(book.to_dict())


# update
@app.route("/books/<int:id>", methods=["PUT", "PATCH"])
def update_book(id: int):
	book = Book.query.get_or_404(id)
	data = request.get_json(silent=True) or {}

	# Only update provided fields
	for field in ["book_name", "author", "publisher"]:
		if field in data and data[field]:
			setattr(book, field, data[field])

	db.session.commit()
	return jsonify(book.to_dict())


# delete
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id: int):
	book = Book.query.get(id)
	if book is None:
		return jsonify({"error": "Book not found"}), 404
	db.session.delete(book)
	db.session.commit()
	return jsonify({"message": "Book deleted"})


# convenience CLI to create tables when run directly
if __name__ == "__main__":
	with app.app_context():
		db.create_all()
	app.run(host="127.0.0.1", port=5001, debug=True)

