# ============================================================
# DIGITAL LIBRARY MANAGEMENT SYSTEM (DLMS)
# ============================================================

import random
from datetime import datetime

# ─────────────────────────────────────────────
# FILE INITIALISATION  (creates files if missing)
# ─────────────────────────────────────────────
def init_files():
    for fname in ['books.txt', 'members.txt', 'borrow.txt']:
        open(fname, 'a').close()

init_files()


# ══════════════════════════════════════════════
#  HELPER — print a divider line
# ══════════════════════════════════════════════
def divider():
    print("-" * 60)


# ══════════════════════════════════════════════
#  SECTION 1 – BOOKS
# ══════════════════════════════════════════════

def display_books():
    print("\n📚  BOOKS IN LIBRARY")
    divider()
    found = False
    with open('books.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                found = True
                b = line.split(',')
                status = "✅ Available" if int(b[4]) > 0 else "❌ Not Available"
                print(f"  ID: {b[0]}  |  {b[1]}  by {b[2]}  |  Genre: {b[3]}  |  Copies: {b[4]}  |  {status}")
    if not found:
        print("  No books found.")
    divider()
    print()


def add_book():
    display_books()
    print("➕  ADD NEW BOOK")
    divider()
    book_id   = input("  Enter Book ID       : ")
    title     = input("  Enter Title         : ")
    author    = input("  Enter Author        : ")
    genre     = input("  Enter Genre         : ")
    copies    = int(input("  Enter No. of Copies : "))
    with open('books.txt', 'a') as f:
        f.write(f"{book_id},{title},{author},{genre},{copies}\n")
    print(f"\n  ✅  '{title}' added successfully!\n")
    display_books()


def search_book():
    display_books()
    keyword = input("🔍  Enter title or author to search: ").lower()
    print("\n  SEARCH RESULTS")
    divider()
    found = False
    with open('books.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                b = line.split(',')
                if keyword in b[1].lower() or keyword in b[2].lower():
                    found = True
                    status = "✅ Available" if int(b[4]) > 0 else "❌ Not Available"
                    print(f"  ID: {b[0]}  |  {b[1]}  by {b[2]}  |  Genre: {b[3]}  |  Copies: {b[4]}  |  {status}")
    if not found:
        print("  No matching books found.")
    divider()
    print()


def update_book():
    display_books()
    print("✏️   UPDATE BOOK")
    divider()
    book_id = input("  Enter Book ID to update: ")
    found = False
    with open('books.txt', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for i, line in enumerate(lines):
            if line.startswith(book_id + ','):
                found = True
                b = line.strip().split(',')
                print(f"\n  Updating: '{b[1]}' by {b[2]}")
                print("  (Press Enter to keep current value)\n")
                new_title  = input(f"  New title  [{b[1]}]: ") or b[1]
                new_author = input(f"  New author [{b[2]}]: ") or b[2]
                new_genre  = input(f"  New genre  [{b[3]}]: ") or b[3]
                new_copies = input(f"  New copies [{b[4]}]: ") or b[4]
                lines[i] = f"{book_id},{new_title},{new_author},{new_genre},{new_copies}\n"
                break
        if not found:
            print("  ❌  Book not found!")
            return
        f.writelines(lines)
        f.truncate()
    print("  ✅  Book updated successfully!\n")
    display_books()


def delete_book():
    display_books()
    print("🗑️   DELETE BOOK")
    divider()
    book_id = input("  Enter Book ID to delete: ")
    found = False
    with open('books.txt', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line.startswith(book_id + ','):
                found = True
            else:
                f.write(line)
        f.truncate()
    if found:
        print("  ✅  Book deleted successfully!\n")
        display_books()
    else:
        print("  ❌  Book not found!\n")


# ══════════════════════════════════════════════
#  SECTION 2 – MEMBERS
# ══════════════════════════════════════════════

def display_members():
    print("\n👥  REGISTERED MEMBERS")
    divider()
    found = False
    with open('members.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                found = True
                m = line.split(',')
                print(f"  ID: {m[0]}  |  {m[1]}  |  Phone: {m[2]}  |  Email: {m[3]}  |  Type: {m[4]}")
    if not found:
        print("  No members registered.")
    divider()
    print()


def add_member():
    display_members()
    print("➕  ADD NEW MEMBER")
    divider()
    member_id   = "M" + str(random.randint(1000, 9999))
    name        = input("  Enter Member Name                    : ")
    phone       = input("  Enter Phone Number                   : ")
    email       = input("  Enter Email                          : ")
    member_type = input("  Member Type (Student/Faculty/Public) : ")
    with open('members.txt', 'a') as f:
        f.write(f"{member_id},{name},{phone},{email},{member_type}\n")
    print(f"\n  ✅  Member added! Member ID is: {member_id}\n")
    display_members()


def update_member():
    display_members()
    print("✏️   UPDATE MEMBER")
    divider()
    member_id = input("  Enter Member ID to update: ")
    found = False
    with open('members.txt', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for i, line in enumerate(lines):
            if line.startswith(member_id + ','):
                found = True
                m = line.strip().split(',')
                print(f"\n  Updating: {m[1]}")
                print("  (Press Enter to keep current value)\n")
                new_phone = input(f"  New phone [{m[2]}]: ") or m[2]
                new_email = input(f"  New email [{m[3]}]: ") or m[3]
                lines[i] = f"{member_id},{m[1]},{new_phone},{new_email},{m[4]}\n"
                break
        if not found:
            print("  ❌  Member not found!")
            return
        f.writelines(lines)
        f.truncate()
    print("  ✅  Member updated successfully!\n")
    display_members()


# ══════════════════════════════════════════════
#  SECTION 3 – BORROW & RETURN
# ══════════════════════════════════════════════

def display_borrows():
    print("\n📋  BORROW RECORDS")
    divider()
    found = False
    with open('borrow.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                found = True
                r = line.split(',')
                icon = "🟡" if r[5] == "BORROWED" else "🟢"
                print(f"  {icon} BorrowID: {r[0]}  |  MemberID: {r[1]}  |  BookID: {r[2]}  |  Borrowed: {r[3]}  |  Due: {r[4]}  |  {r[5]}")
    if not found:
        print("  No borrow records found.")
    divider()
    print()


def borrow_book():
    display_books()
    display_members()
    print("📤  BORROW A BOOK")
    divider()
    member_id = input("  Enter Member ID  : ")

    member_found = False
    with open('members.txt', 'r') as f:
        for line in f:
            if line.startswith(member_id + ','):
                member_found = True
                m = line.strip().split(',')
                print(f"  Member: {m[1]} ({m[4]})")
                break
    if not member_found:
        print("  ❌  Member not found!\n")
        return

    book_id = input("  Enter Book ID    : ")

    book_found  = False
    book_copies = 0
    with open('books.txt', 'r') as f:
        for line in f:
            if line.startswith(book_id + ','):
                book_found  = True
                b = line.strip().split(',')
                book_copies = int(b[4])
                print(f"  Book  : {b[1]} by {b[2]}")
                break
    if not book_found:
        print("  ❌  Book not found!\n")
        return
    if book_copies < 1:
        print("  ❌  No copies available right now.\n")
        return

    borrow_id   = "BR" + str(random.randint(1000, 9999))
    borrow_date = datetime.today().strftime('%d/%m/%Y')
    due_date    = input("  Enter due date (DD/MM/YYYY): ")

    with open('borrow.txt', 'a') as f:
        f.write(f"{borrow_id},{member_id},{book_id},{borrow_date},{due_date},BORROWED\n")

    with open('books.txt', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for i, line in enumerate(lines):
            if line.startswith(book_id + ','):
                b = line.strip().split(',')
                b[4] = str(int(b[4]) - 1)
                lines[i] = ','.join(b) + '\n'
                break
        f.writelines(lines)
        f.truncate()

    print(f"\n  ✅  Book borrowed! Borrow ID: {borrow_id}  |  Due: {due_date}\n")
    display_borrows()


def return_book():
    display_borrows()
    print("📥  RETURN A BOOK")
    divider()
    borrow_id = input("  Enter Borrow ID from the list above: ")
    found = False

    borrow_data = []
    with open('borrow.txt', 'r') as f:
        borrow_data = f.readlines()

    book_id = None
    for i, line in enumerate(borrow_data):
        if line.startswith(borrow_id + ','):
            found = True
            record = line.strip().split(',')
            if record[5] == "RETURNED":
                print("  ⚠️   This book has already been returned!\n")
                return
            book_id        = record[2]
            due_date_str   = record[4]
            return_date    = datetime.today().strftime('%d/%m/%Y')
            borrow_data[i] = ','.join(record[:5]) + ',RETURNED\n'
            break

    if not found:
        print("  ❌  Borrow record not found!\n")
        return

    due_dt  = datetime.strptime(due_date_str, '%d/%m/%Y')
    today   = datetime.today()
    overdue = (today - due_dt).days
    fine    = max(0, overdue * 5)

    with open('borrow.txt', 'w') as f:
        f.writelines(borrow_data)

    with open('books.txt', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for i, line in enumerate(lines):
            if line.startswith(book_id + ','):
                b = line.strip().split(',')
                b[4] = str(int(b[4]) + 1)
                lines[i] = ','.join(b) + '\n'
                break
        f.writelines(lines)
        f.truncate()

    print(f"\n  ✅  Book returned on {return_date}")
    if fine > 0:
        print(f"  ⚠️   Overdue by {overdue} day(s).  Fine: ₹{fine}")
    else:
        print("  🎉  No fine! Returned on time.")
    print()
    display_borrows()


# ══════════════════════════════════════════════
#  SECTION 4 – FINE CALCULATOR
# ══════════════════════════════════════════════

def calculate_fine():
    display_borrows()
    print("💰  FINE CALCULATOR")
    divider()
    due_str = input("  Enter due date (DD/MM/YYYY): ")
    try:
        due_dt  = datetime.strptime(due_str, '%d/%m/%Y')
        today   = datetime.today()
        overdue = (today - due_dt).days
        if overdue > 0:
            fine = overdue * 5
            print(f"  ⚠️   Overdue by {overdue} day(s).  Fine: ₹{fine}\n")
        else:
            print("  ✅  No fine – not overdue yet.\n")
    except ValueError:
        print("  ❌  Invalid date format. Use DD/MM/YYYY\n")


# ══════════════════════════════════════════════
#  SECTION 5 – DISPLAY ALL
# ══════════════════════════════════════════════

def display_all():
    display_books()
    display_members()
    display_borrows()


# ══════════════════════════════════════════════
#  SECTION 6 – MEMBER MENU
# ══════════════════════════════════════════════

def member_menu():
    print("\n📖  MEMBER PORTAL – Digital Library Management System\n")
    display_members()
    member_id = input("Enter your Member ID: ")
    print()

    with open('members.txt', 'r') as f:
        found = False
        for line in f:
            if line.startswith(member_id + ','):
                found = True
                m = line.strip().split(',')
                print(f"  Hello {m[1]}! Welcome back 😊  ({m[4]} Member)\n")
                break

    if not found:
        print("  ❌  Member not found!\n")
        return

    go_on = "yes"
    while go_on == "yes":
        print("\nWhat would you like to do?")
        divider()
        print("  1. View all books")
        print("  2. Search for a book")
        print("  3. Borrow a book")
        print("  4. Return a book")
        print("  5. Calculate fine")
        print("  0. Exit Member Portal")
        divider()
        choice = input("Enter your choice: ")
        print()
        if choice == '1':
            display_books()
        elif choice == '2':
            search_book()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            calculate_fine()
        elif choice == '0':
            print("  👋  Goodbye!\n")
            go_on = "no"
        else:
            print("  ❌  Invalid choice! Enter a number from the menu above.\n")


# ══════════════════════════════════════════════
#  SECTION 7 – ADMIN MENU
# ══════════════════════════════════════════════

ADMIN_PASSWORD = "admin123"

def admin_menu():
    print("\n🔐  ADMIN LOGIN")
    divider()
    pwd = input("  Enter Admin Password: ")
    if pwd != ADMIN_PASSWORD:
        print("  ❌  Incorrect password!\n")
        return

    go_on = "yes"
    while go_on == "yes":
        print("\n🛠️   ADMIN PANEL – Digital Library Management System")
        divider()
        print("  BOOKS  :  1-Add    2-Display  3-Search  4-Update  5-Delete")
        print("  MEMBERS:  6-Add    7-Display  8-Update")
        print("  BORROW :  9-Borrow 10-Return  11-All Borrow Records")
        print("  OTHER  :  12-Fine Calculator  13-Display All Data")
        print("            0-Logout")
        divider()
        choice = input("  Enter your choice: ")
        print()
        if   choice == '1':  add_book()
        elif choice == '2':  display_books()
        elif choice == '3':  search_book()
        elif choice == '4':  update_book()
        elif choice == '5':  delete_book()
        elif choice == '6':  add_member()
        elif choice == '7':  display_members()
        elif choice == '8':  update_member()
        elif choice == '9':  borrow_book()
        elif choice == '10': return_book()
        elif choice == '11': display_borrows()
        elif choice == '12': calculate_fine()
        elif choice == '13': display_all()
        elif choice == '0':
            print("  👋  Logged out of Admin Panel.\n")
            go_on = "no"
        else:
            print("  ❌  Invalid choice! Enter a number from the menu above.\n")


# ══════════════════════════════════════════════
#  SECTION 8 – MASTER MENU
# ══════════════════════════════════════════════

def run_library():
    while True:
        print("\n" + "=" * 60)
        print("       📚  DIGITAL LIBRARY MANAGEMENT SYSTEM  📚")
        print("=" * 60)
        print("  1. Admin Portal")
        print("  2. Member Portal")
        print("  0. Exit")
        divider()
        choice = input("  Enter your choice: ")
        if choice == '1':
            admin_menu()
        elif choice == '2':
            member_menu()
        elif choice == '0':
            print("\n  👋  Thank you for using DLMS. Goodbye!\n")
            break
        else:
            print("  ❌  Invalid choice!\n")


# ──────────────────────────────────────────────
run_library()
