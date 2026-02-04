# exercise:
#    - make a dictionary with keys as (2-3) authors and values as 2-3 books per author.
#    - input asking for an author name. (think about UX here).
#    - print the books as a STRING!!!
#    - error handling for incorrect author names. 
#    - USE only in built methods and things we have already covered.
#    - be prepared to justify your choices. 


library = {
    "Matthew Walker": [
        "Why do we sleep",
        "Welcome Anoard"
    ],
    "James Clear": [
        "Atomic Habits",
        "The 3rd Door"
    ],
    "Tim Marshall": [
        "Prisoners of Geography",
        "The Power of Geography",
        "Divided"
    ]
}

library_lower = {author.lower(): books for author, books in library.items()}

input_author = input("Please enter the author's name (e.g., Matthew Walker): ").strip().lower()

result = library_lower.get(input_author, f"Sorry, we do not have any books by '{input_author.title()}'. Please check the spelling or try another author.")
string_result = ", ".join(result) if isinstance(result, list) else ""
print(f"Here are the books by {input_author.title()}: {string_result}." if string_result else result)