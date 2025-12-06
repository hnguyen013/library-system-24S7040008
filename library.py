library = []

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
        else:
            print("This feature is not implemented yet.")

if __name__ == "__main__":
    main()
