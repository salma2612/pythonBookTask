import string
books = {"Margaret Atwood":["The Handmaid's Tale", "The Blind Assassin"], "J.R.R. Tolkien":["The Hobbit", "The Lord Of The Rings", "The Silmarillion"], "Roald Dahl":["Charlie And The Chocolate Factory", "Matilda"]}


book = string.capwords( input('pick a book'))

def check(book):
    for author in books:
        if book in books[author]:
            return f"{author} wrote {book}"
        return "Book not found"

print (check(book))
