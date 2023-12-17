# Simple rest api http://localhost:5000/books, http://localhost:5000/first
# Run via Flask executing python

from flask import Flask, json

books = [{"id": 1, "name": "Java in action"}, {"id": 2, "name": "Github in a nutshell"}]

api = Flask(__name__)


@api.route('/books', methods=['GET'])
def get_books():
    return json.dumps(books)


@api.route('/first', methods=['GET'])
def get_first():
    return json.dumps(books[0])


if __name__ == '__main__':
    api.run()
