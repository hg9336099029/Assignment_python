from datetime import datetime, timedelta

Book_store = {}
borrowed_book_record = {}
user_record = {}

#----------------- ADMIN FUNCTIONS--------------------#

def add_book():
    book_id = int(input("Enter Book ID: "))

    # Sequential numbering validation
    if Book_store:
        mx = max(Book_store.keys())
        if book_id != mx + 1:
            print(f"Book ID must be {mx + 1}")
            return
    elif book_id != 1:
        print("First Book ID must be 1")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")

    collection = input("Collection Name (blank if none): ")
    volume = input("Volume No (blank if none): ")

    Book_store[book_id] = {
        "title": title,
        "author": author,
        "collection": collection,
        "volume": volume,
        "available": True
    }
    print("Book added successfully!")


def remove_book():
    book_id = int(input("Enter Book ID to remove: "))

    if book_id in Book_store:
        del Book_store[book_id]
        print("Book removed successfully!")
    else:
        print("Book not found")


def clear_entry_book():
    title = input("Enter title to clear: ")

    ids = []

    for book_id, data in Book_store.items():
        if data["title"] == title:
            ids.append(book_id)

    for book_id in ids:
        del Book_store[book_id]

    print("Entry cleared successfully")


def view_borrowed_books():

    if not borrowed_book_record:
        print("No borrowed books")
        return

    print("\nBorrowed Books\n")

    for book_id, data in borrowed_book_record.items():

        due_date = (datetime.strptime(data["issue_date"], "%d-%m-%Y")+ timedelta(days=14)).strftime("%d-%m-%Y")

        print(
            f"Book ID: {book_id} | "
            f"Title: {data['title']} | "
            f"User: {data['user']} | "
            f"Issue Date: {data['issue_date']} | "
            f"Due Date: {due_date}"
        )


# ------------------USER FUNCTIONS-----------------#

def receive_book():

    book_id = int(input("Enter Book ID: "))

    if book_id not in Book_store:
        print("Book not found")
        return

    if not Book_store[book_id]["available"]:
        print("Book already issued")
        return

    user = input("Enter User Name: ")

    if user in user_record and user_record[user]["blocked"]:
        print("User is blocked")
        return

    issue_date = datetime.now().strftime("%d-%m-%Y")

    # Collection handling
    collection = Book_store[book_id]["collection"]

    if collection:
        for bid, book in Book_store.items():
            if book["collection"] == collection:
                book["available"] = False
                borrowed_book_record[bid] = {
                    "title": book["title"],
                    "author": book["author"],
                    "user": user,
                    "issue_date": issue_date,
                    "return_date": None
                }
    else:
        Book_store[book_id]["available"] = False
        borrowed_book_record[book_id] = {
            "title": Book_store[book_id]["title"],
            "author": Book_store[book_id]["author"],
            "user": user,
            "issue_date": issue_date,
            "return_date": None
        }

    if user not in user_record:
        user_record[user] = {"blocked": False}
        
    print("Book issued successfully")


def return_book():

    book_id = int(input("Enter Book ID: "))
    if book_id not in borrowed_book_record:
        print("No issue record found")
        return
    user = borrowed_book_record[book_id]["user"]

    issue_date = datetime.strptime(borrowed_book_record[book_id]["issue_date"],"%d-%m-%Y" )
    return_date = datetime.now()
    days = (return_date - issue_date).days

    # Collection handling
    collection = Book_store[book_id]["collection"]
    if collection:
        ids = []
        for bid, book in Book_store.items():
            if book["collection"] == collection:
                book["available"] = True
                ids.append(bid)

        for bid in ids:
            del borrowed_book_record[bid]
    else:
        Book_store[book_id]["available"] = True
        del borrowed_book_record[book_id]
    if days > 14:
        user_record[user]["blocked"] = True
        print(f"User blocked ({days} days late)")
    print("Book returned successfully")


#--------------- SEARCH FUNCTIONS--------------------#

def search_book_by_title():
    text = input("Enter title or substring: ").lower()
    found = False
    for book_id, book in Book_store.items():
        if text in book["title"].lower():
            found = True
            print(
                f"ID: {book_id} | "
                f"Title: {book['title']} | "
                f"Author: {book['author']}"
            )
    if not found:
        print("No matching books found")


def search_book_by_author():
    author = input("Enter author name: ").lower()
    found = False

    for book_id, book in Book_store.items():
        if author in book["author"].lower():
            found = True
            print(f"ID: {book_id} | "f"Title: {book['title']}")
    if not found:
        print("No books found")


#--------------- MENU--------------#


while True:
    print("\n1.Add Book")
    print("2.Remove Book")
    print("3.Clear Entry")
    print("4.Receive Book")
    print("5.Return Book")
    print("6.Search By Title")
    print("7.Search By Author")
    print("8.View Borrowed Books")
    print("9.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        remove_book()

    elif choice == "3":
        clear_entry_book()

    elif choice == "4":
        receive_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        search_book_by_title()

    elif choice == "7":
        search_book_by_author()

    elif choice == "8":
        view_borrowed_books()

    elif choice == "9":
        break

    else:
        print("Invalid Choice")