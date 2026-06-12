from datetime import datetime, timedelta

Book_store = {}
borrowed_book_record = {}
user_record = {}

# ---------------- ADMIN FUNCTIONS ---------------- #

def add_book():

    try:
        book_id = int(input("Enter Book ID: "))
    except ValueError:
        print("Invalid Book ID")
        return

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

    collection = input(
        "Collection Name (leave blank if none): "
    ).strip()

    volume = input(
        "Volume Number (leave blank if none): "
    ).strip()

    Book_store[book_id] = {
        "title": title,
        "author": author,
        "collection": collection,
        "volume": volume,
        "available": True
    }

    print("Book added successfully")


def remove_book():

    title = input(
        "Enter Book Title to remove: "
    ).lower()

    ids = []
    collection = ""

    for bid, book in Book_store.items():

        if book["title"].lower() == title:

            collection = book["collection"]
            break

    if collection:

        for bid, book in Book_store.items():

            if book["collection"] == collection:

                if not book["available"]:
                    print(
                        "Cannot remove. "
                        "Book is currently issued."
                    )
                    return

                ids.append(bid)

    else:

        for bid, book in Book_store.items():

            if book["title"].lower() == title:

                if not book["available"]:
                    print(
                        "Cannot remove. "
                        "Book is currently issued."
                    )
                    return

                ids.append(bid)

    if not ids:
        print("Book not found")
        return

    for bid in ids:
        del Book_store[bid]

    if collection:
        print("Entire collection removed successfully")
    else:
        print("Book removed successfully")


def clear_entry_book():

    try:
        book_id = int(input("Enter Book ID to clear: "))
    except ValueError:
        print("Invalid Book ID")
        return

    if book_id not in Book_store:
        print("Book not found")
        return

    collection = Book_store[book_id]["collection"]

    ids = []

    if collection:

        for bid, book in Book_store.items():

            if book["collection"] == collection:
                ids.append(bid)

    else:
        ids.append(book_id)

    for bid in ids:

        if not Book_store[bid]["available"]:
            print(
                "Cannot clear entry. "
                "Book is currently issued."
            )
            return

    for bid in ids:
        del Book_store[bid]

    if collection:
        print("Entire collection removed successfully")
    else:
        print("Book removed successfully")


def view_borrowed_books():

    if not borrowed_book_record:
        print("No borrowed books")
        return

    print("\nCURRENT BORROWED BOOKS\n")

    print(
        f"{'Book ID':<10}"
        f"{'Title':<30}"
        f"{'User':<15}"
        f"{'Issue Date':<15}"
        f"{'Due Date':<15}"
    )

    print("-" * 85)

    for book_id, data in borrowed_book_record.items():

        due_date = (
            datetime.strptime(
                data["issue_date"],
                "%d-%m-%Y"
            ) + timedelta(days=14)
        ).strftime("%d-%m-%Y")

        print(
            f"{book_id:<10}"
            f"{data['title']:<30}"
            f"{data['user']:<15}"
            f"{data['issue_date']:<15}"
            f"{due_date:<15}"
        )


# ---------------- USER FUNCTIONS ---------------- #

def show_available_books():

    found = False

    print("\nAVAILABLE BOOKS\n")

    for book_id, book in Book_store.items():

        if book["available"]:

            found = True

            print(
                f"ID:{book_id} | "
                f"Title:{book['title']} | "
                f"Author:{book['author']} | "
                f"Collection:{book['collection']} | "
                f"Volume:{book['volume']}"
            )

    if not found:
        print("No books available")


def receive_book():

    show_available_books()

    try:
        book_id = int(input("\nEnter Book ID: "))
    except ValueError:
        print("Invalid Book ID")
        return

    if book_id not in Book_store:
        print("Book not found")
        return

    if not Book_store[book_id]["available"]:
        print("Book already issued")
        return

    user = input("Enter User Name: ")

    if (
        user in user_record
        and user_record[user]["blocked"]
    ):
        print("User is blocked")
        return

    issue_date = datetime.now().strftime("%d-%m-%Y")

    collection = Book_store[book_id]["collection"]

    if collection:

        for bid, book in Book_store.items():

            if book["collection"] == collection:

                book["available"] = False

                borrowed_book_record[bid] = {
                    "title": book["title"],
                    "author": book["author"],
                    "user": user,
                    "issue_date": issue_date
                }

        print("Entire collection issued successfully")

    else:

        Book_store[book_id]["available"] = False

        borrowed_book_record[book_id] = {
            "title": Book_store[book_id]["title"],
            "author": Book_store[book_id]["author"],
            "user": user,
            "issue_date": issue_date
        }

        print("Book issued successfully")

    if user not in user_record:
        user_record[user] = {"blocked": False}


def return_book():

    try:
        book_id = int(input("Enter Book ID: "))
    except ValueError:
        print("Invalid Book ID")
        return

    if book_id not in borrowed_book_record:
        print("No issue record found")
        return

    user = borrowed_book_record[book_id]["user"]

    issue_date = datetime.strptime(
        borrowed_book_record[book_id]["issue_date"],
        "%d-%m-%Y"
    )

    return_date = datetime.now()

    days = (return_date - issue_date).days

    collection = Book_store[book_id]["collection"]

    if collection:

        ids = []

        for bid, book in Book_store.items():

            if book["collection"] == collection:

                book["available"] = True
                ids.append(bid)

        for bid in ids:
            del borrowed_book_record[bid]

        print("Entire collection returned successfully")

    else:

        Book_store[book_id]["available"] = True

        del borrowed_book_record[book_id]

        print("Book returned successfully")

    if days > 14:

        user_record[user]["blocked"] = True

        print(
            f"User '{user}' blocked "
            f"for late return ({days} days)"
        )


# ---------------- SEARCH FUNCTIONS ---------------- #

def search_book_by_title():

    text = input(
        "Enter Title or Substring: "
    ).lower()

    found = False

    for book_id, book in Book_store.items():

        if text in book["title"].lower():

            found = True

            print(
                f"ID:{book_id} | "
                f"Title:{book['title']} | "
                f"Author:{book['author']} | "
                f"Collection:{book['collection']} | "
                f"Volume:{book['volume']}"
            )

    if not found:
        print("No matching books found")


def search_book_by_author():

    author = input(
        "Enter Author Name: "
    ).lower()

    found = False

    for book_id, book in Book_store.items():

        if author in book["author"].lower():

            found = True

            print(
                f"ID:{book_id} | "
                f"Title:{book['title']} | "
                f"Collection:{book['collection']} | "
                f"Volume:{book['volume']}"
            )

    if not found:
        print("No books found")


# ---------------- MENUS ---------------- #

def admin_menu():

    while True:

        print("\n----- ADMIN MENU -----")
        print("1. Add Book")
        print("2. Remove Book By Name")
        print("3. Clear Entry By Book ID")
        print("4. View Borrowed Books")
        print("5. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            remove_book()

        elif choice == "3":
            clear_entry_book()

        elif choice == "4":
            view_borrowed_books()

        elif choice == "5":
            break

        else:
            print("Invalid Choice")


def user_menu():

    while True:

        print("\n----- USER MENU -----")
        print("1. Receive Book")
        print("2. Return Book")
        print("3. Search By Title")
        print("4. Search By Author")
        print("5. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            receive_book()

        elif choice == "2":
            return_book()

        elif choice == "3":
            search_book_by_title()

        elif choice == "4":
            search_book_by_author()

        elif choice == "5":
            break

        else:
            print("Invalid Choice")


# ---------------- MAIN ---------------- #

def main():

    while True:

        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Admin")
        print("2. User")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            admin_menu()

        elif choice == "2":
            user_menu()

        elif choice == "3":
            print("Thank You")
            break

        else:
            print("Invalid Choice")


main()
