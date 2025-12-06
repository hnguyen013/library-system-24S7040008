library = []
def add_book(title, author):
    library.append({"title": title, "author": author, "is_available": True})
    print(f"Book '{title}' by {author} has been added!")
def main():
    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add book")
        print("2. Show library")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "3":
            print("Goodbye!")
            break
        elif choice =="1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)

if __name__ == "__main__":
    main()
