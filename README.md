## Digital Library Management System (DLMS)
The Digital Library Management System is a file-based automation tool developed in Python. It is designed to streamline day-to-day library operations, including book cataloging, member registration, and the tracking of borrow/return transactions with automated fine calculation.
Libraries often struggle to manage large volumes of books and member data using manual records, leading to lost borrow records and incorrect fine calculations. This project addresses these challenges by providing a centralized, automated solution that is easy for beginners to understand and extend.
As of now, this project is a prototype developed to demonstrate the use of core Python programming concepts in a practical, real-world application. The goal is to provide a lightweight and user-friendly interface that automates routine library tasks while ensuring persistent data management.

To preview the code: Download and run `DLMS.py`
To see the Process Flow: Refer to the Process Flow Diagram.
To see the Entities and Relationships: Refer to the E-R Diagram.


Key Features
Dual-Portal System: Includes dedicated interfaces for Admins and Members to manage tasks separately.
Book Management: Full capabilities to add, display, search, update, and delete books in the library catalog.
Automated Transactions: Manages the borrowing and returning of books while automatically updating available copy counts.
Dynamic Fine Calculation: Automatically calculates late fees at a rate of Rs.5 per day beyond the due date.
Persistent Storage: Uses a lightweight database of plain text files (`books.txt`, `members.txt`, and `borrow.txt`) to ensure data is saved between sessions.
