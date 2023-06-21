import typing as t
from flask import Flask, jsonify, request, abort, make_response
from flask.json.provider import DefaultJSONProvider


class Book:
    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return self.title + ' by ' + self.author + ' @ ' + str(self.price)

    def to_json(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'price': self.price
        }

class BookJSONProvider(DefaultJSONProvider):

    def dumps(self, obj: t.Any, **kwargs: t.Any):
        if isinstance(obj, Book):
            return {'book': obj.to_json()}
        elif isinstance(obj, list):
            return {'books': list(map(lambda b: b.to_json(), obj))}
        return super().dumps(obj, **kwargs)


class Bookshop:
    def __init__(self, books):
        self.books = books

    def get(self, isbn):
        if int(isbn) > len(self.books):
            abort(404)
        return list(filter(lambda b: b.isbn == isbn, self.books))[0]

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, isbn):
        self.books = list(filter(lambda b: b.isbn != isbn, self.books))


bookshop = Bookshop([Book(1, 'XML', 'Gryff Smith', 10.99),
                     Book(2, 'Java', 'Phoebe Cooke', 12.99),
                     Book(3, 'Scala', 'Adam Davies', 11.99),
                     Book(4, 'Python', 'Natalia Nadal', 15.99)])

def create_bookshop_service():
    app = Flask(__name__)
    app.json=BookJSONProvider(app)

    @app.route('/book/list', methods=['GET'])
    def get_books():
        response= jsonify(bookshop.books)
        return response


    @app.route('/book/<int:isbn>', methods=['GET'])
    def get_book(isbn):
        book = bookshop.get(isbn)
        return jsonify(book)


    @app.route('/book', methods=['POST'])
    def create_book():
        print('create book')
        if not request.json or not 'isbn' in request.json:
            abort(400)
        book = Book(request.json['isbn'],
                    request.json['title'],
                    request.json.get('author', ""),
                    float(request.json['price']))
        bookshop.add_book(book)
        return jsonify(book), 201


    @app.route('/book', methods=['PUT'])
    def update_book():
        if not request.json or not 'isbn' in request.json:
            abort(400)
        isbn = request.json['isbn']
        book = bookshop.get(isbn)
        book.title = request.json['title']
        book.author = request.json['author']
        book.price = request.json['price']
        return jsonify(book), 201


    @app.route('/book/<int:isbn>', methods=['DELETE'])
    def delete_book(isbn):
        bookshop.delete_book(isbn)
        return jsonify({'result': True})


    @app.errorhandler(400)
    def not_found(error):
        return make_response(jsonify({'Error': 'Book Not Found'}), 400)

    return app

if __name__ == '__main__':
    app = create_bookshop_service()
    app.run(debug=True)
