library = []
def add_book(title, author):
    library.append({"title": title, "author": author, "is_available": True})
    print(f"Book '{title}' by {author} has been added!")

def view_books():
    if not library:
        print("Library is empty.")
        return
    print("\n===== ALL BOOKS =====")
    for index, book in enumerate(library, start=1):
        title = book.get("title", "Unknown Title")
        author = book.get("author", "Unknown Author")
        available = "Yes" if book.get("is_available", True) else "No"
        print(f"{index}. {title} — {author} (Available: {available})")

def search_book(query):        
    keyword = query.lower()
    results = []
    for book in library:
        if keyword in book["title"].lower():
            results.append(book)
    if not results:
        print(f"No books found with keyword: {query}")
    else:
        print(f"\n===== SEARCH RESULTS for '{query}' =====")
        for index, book in enumerate(results, start=1):
            title = book["title"]
            author = book["author"]
            available = "Yes" if book["is_available"] else "No"
            print(f"{index}. {title} — {author} (Available: {available})")

def main():
    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "4":
            print("Goodbye!")
            break
        elif choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
        elif choice == "2":
            view_books()
        elif choice == "3":
            query = input("Enter a keyword to search: ").strip()
            search_book(query)

if __name__ == "__main__":
    main()
