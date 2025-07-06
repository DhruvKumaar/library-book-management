from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = {}
        self.issued = {}

    def add_book(self, book_id, title):
        if book_id in self.books:
            print("Book ID already exists.")
        else:
            self.books[book_id] = title
            print(f"Book '{title}' added successfully.")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book removed successfully.")
        else:
            print("Book ID not found.")

    def issue_book(self, student_name, book_id):
        if book_id not in self.books:
            print("Book ID not available.")
            return
        if student_name in self.issued:
            print("Student already has a book issued.")
            return

        issue_date = datetime.now()
        due_date = issue_date + timedelta(days=7)
        self.issued[student_name] = {
            'book_id': book_id,
            'issue_date': issue_date,
            'due_date': due_date
        }
        print(f"Book issued to {student_name} until {due_date.strftime('%d-%m-%Y')}.")

    def return_book(self, student_name):
        if student_name not in self.issued:
            print("No book issued to this student.")
            return

        record = self.issued[student_name]
        return_date = datetime.now()
        due_date = record['due_date']

        if return_date > due_date:
            days_late = (return_date - due_date).days
            fine = days_late * 5
            print(f"Book returned late. Fine: ₹{fine}")
        else:
            print("Book returned on time. No fine.")

        del self.issued[student_name]

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Available Books:")
            for book_id, title in self.books.items():
                print(f"{book_id}: {title}")

    def display_issued(self):
        if not self.issued:
            print("No books currently issued.")
        else:
            print("Issued Books:")
            for student, record in self.issued.items():
                print(f"{student} => {record['book_id']} due on {record['due_date'].strftime('%d-%m-%Y')}")

lib = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Show All Books")
    print("6. Show Issued Books")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        lib.add_book(book_id, title)
    elif choice == '2':
        book_id = input("Enter Book ID to remove: ")
        lib.remove_book(book_id)
    elif choice == '3':
        student = input("Enter Student Name: ")
        book_id = input("Enter Book ID to issue: ")
        lib.issue_book(student, book_id)
    elif choice == '4':
        student = input("Enter Student Name to return book: ")
        lib.return_book(student)
    elif choice == '5':
        lib.display_books()
    elif choice == '6':
        lib.display_issued()
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again.")