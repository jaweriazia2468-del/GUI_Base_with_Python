# 📚 Library Management System (Python Tkinter)

## 📌 Project Overview

The Library Management System is a desktop application built using **Python**, **Tkinter**, and **JSON file handling**. It provides a user-friendly interface for managing books, members, and borrowing transactions while demonstrating Object-Oriented Programming concepts.

The system stores data permanently using JSON files.

---

## ✨ Features

- Add Books
- Add Members
- Borrow Books
- Return Books
- View Books List
- View Members List
- View Transaction History
- Automatic Data Saving
- Data Persistence using JSON

---

## 🛠 Technologies Used

- Python 3
- Tkinter
- ttk
- JSON
- Object-Oriented Programming

---

## 📚 OOP Concepts Used

### Abstraction

Abstract Classes

- LibraryItem
- Transaction

---

### Inheritance

Book inherits from LibraryItem.

BorrowTransaction and ReturnTransaction inherit from Transaction.

---

### Polymorphism

Each transaction class has its own implementation of:

```
display()
```

---

## 📂 Project Structure

```
LibraryManagement/
│
├── library.py
├── books.json
├── members.json
├── transactions.json
└── README.md
```

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/javeriazia26/LibraryManagement.git
```

### Navigate

```bash
cd LibraryManagement
```

### Run

```bash
python library.py
```

---

## 💻 GUI Tabs

### Books

- Add Book
- View Books

---

### Members

- Add Member
- View Members

---

### Transactions

- Borrow Book
- Return Book
- Transaction History

---

## 💾 Data Storage

Data is stored in three JSON files.

### books.json

Stores:

- Book ID
- Title
- Author
- Total Copies
- Available Copies

---

### members.json

Stores:

- Member ID
- Member Name

---

### transactions.json

Stores:

- Transaction ID
- Member ID
- Book ID
- Date
- Transaction Type

---

## ⚙ Functionalities

### Add Book

Creates a new book record.

---

### Add Member

Registers a new library member.

---

### Borrow Book

- Checks member exists
- Checks book exists
- Checks availability
- Reduces available copies
- Saves transaction

---

### Return Book

- Increases available copies
- Saves return transaction

---

## ✔ Input Validation

The application validates:

- Empty fields
- Duplicate IDs
- Invalid copies
- Book availability
- Member existence
- Book existence

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python GUI Development
- File Handling
- JSON Storage
- OOP Concepts
- Data Persistence
- Exception Handling

---

## 📸 Application Workflow

1. Add books.
2. Register members.
3. Borrow books.
4. Return books.
5. View transaction history.

---

## Future Improvements

- Due Date Management
- Late Fine Calculation
- Search Books
- Delete Books
- Edit Books
- Login System
- SQLite Database
- Barcode Scanner
