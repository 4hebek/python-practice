library = {
    1: {
        "title": "Why We Sleep: The New Science of Sleep and Dreams",
        "author": "Matthew Walker",
        "type": "Non-fiction",
        "genre": "Science",
        "year": 2017,
        "publisher": "Scribner",
        "ISBN-13": "978-0735211292"
    },
    2: {
        "title": "Atomic Habits: An Easy & Proven Way to Build Good Habits",
        "author": "James Clear",
        "type": "Non-fiction",
        "genre": "Personal Development",
        "year": 2018,
        "publisher": "Avery",
        "ISBN-13": "978-0735211292"
    },
    3: {
        "title": "Prisoners of Geography: Ten Maps That Tell You Everything You Need to Know About Global Politics",
        "author": "Tim Marshall",
        "type": "Non-fiction",
        "genre": "Politics",
        "year": 2015,
        "publisher": "Elliott & Thompson",
        "ISBN-13": "978-1783962433"
    },
    4: {
        "title": "Divided: Why We’re Living in an Age of Walls",
        "author": "Tim Marshall",
        "type": "Non-fiction",
        "genre": "Politics",
        "year": 2018,
        "publisher": "Penguin Books",
        "ISBN-13": "978-1783963973"
    },
    5: {
        "title": "Macbeth",
        "author": "William Shakespeare",
        "type": "Fiction",
        "genre": "Tragedy",
        "year": 1606,
        "publisher": "Penguin Classics",
        "ISBN-13": "978-0141396507"       
    }
}


# Print every title in the library (one per line) - Reddy
# Count total number of books - Jess
# List all books by a given author - Ayaan
# Find a book by title (case insensitive) - Darren
# Filter by year: all books published before 1970 - Darren
# Count books by genre and display all - Karolina


# Print every title in the library (one per line)
for i in library:
    print(library[i]["title"])


# Find a book by title (case insensitive)
while True:
    search_title = input("Enter book title: ").lower()

    for book_id, book in library.items():
        if book["title"].lower() == search_title:
            print(f"""Book found:Title: {book['title']}Author: {book['author']}Year: {book['year']}Type: {book['type']}Genre: {book['genre']}Publisher: {book['publisher']}ISBN-13: {book['ISBN-13']}""")
            break
    else:
        print("Book not found. Try again.\n")
    break

print("\nBooks published before 1970:")


# Filter by year: all books published before 1970
for book_id, book in library.items():
    if book["year"] < 1970:
        print(book["title"], "-", book["year"])


# Count books by genre and display all
search_genre = input("Enter genre: ").strip().lower()

count = 0
titles = []

for book in library.values():
    genre = book.get("genre", "").strip().lower()
    
    if genre == search_genre:
        count += 1
        titles.append(book.get("title"))

if count > 0:
        print(f"Total books in genre '{search_genre}': {count}")
        for title in titles:
            print(f"{title}")
else:
        print("No books found for this genre.")
