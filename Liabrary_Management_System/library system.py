import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod
from datetime import datetime
import json
import os

# Base classes
class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title

    @abstractmethod
    def display(self):
        pass

class Book(LibraryItem):
    def __init__(self, item_id, title, author, total_copies):
        super().__init__(item_id, title)
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def display(self):
        return f"{self.item_id} | {self.title} | {self.author} | {self.available_copies}/{self.total_copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def display(self):
        return f"{self.member_id} | {self.name}"

class Transaction(ABC):
    def __init__(self, transaction_id, member_id, book_id, date):
        self.transaction_id = transaction_id
        self.member_id = member_id
        self.book_id = book_id
        self.date = date

    @abstractmethod
    def display(self):
        pass

class BorrowTransaction(Transaction):
    def display(self):
        return f"{self.transaction_id} | Borrow | {self.member_id} | {self.book_id} | {self.date}"

class ReturnTransaction(Transaction):
    def display(self):
        return f"{self.transaction_id} | Return | {self.member_id} | {self.book_id} | {self.date}"

# Library System with file handling
class LibrarySystem:
    def __init__(self, books_file='books.json', members_file='members.json', transactions_file='transactions.json'):
        self.books_file = books_file
        self.members_file = members_file
        self.transactions_file = transactions_file

        self.books = {}
        self.members = {}
        self.transactions = []

        self.load_data()

    def load_data(self):
        # Load books
        if os.path.exists(self.books_file):
            with open(self.books_file, 'r') as f:
                books_data = json.load(f)
                for b in books_data:
                    book = Book(b['item_id'], b['title'], b['author'], b['total_copies'])
                    book.available_copies = b.get('available_copies', book.total_copies)
                    self.books[book.item_id] = book

        # Load members
        if os.path.exists(self.members_file):
            with open(self.members_file, 'r') as f:
                members_data = json.load(f)
                for m in members_data:
                    member = Member(m['member_id'], m['name'])
                    self.members[member.member_id] = member

        # Load transactions
        if os.path.exists(self.transactions_file):
            with open(self.transactions_file, 'r') as f:
                transactions_data = json.load(f)
                for t in transactions_data:
                    if t['type'] == 'borrow':
                        trans = BorrowTransaction(t['transaction_id'], t['member_id'], t['book_id'], t['date'])
                    else:
                        trans = ReturnTransaction(t['transaction_id'], t['member_id'], t['book_id'], t['date'])
                    self.transactions.append(trans)

    def save_data(self):
        # Save books
        books_data = []
        for book in self.books.values():
            books_data.append({
                'item_id': book.item_id,
                'title': book.title,
                'author': book.author,
                'total_copies': book.total_copies,
                'available_copies': book.available_copies
            })
        with open(self.books_file, 'w') as f:
            json.dump(books_data, f, indent=4)

        # Save members
        members_data = []
        for member in self.members.values():
            members_data.append({
                'member_id': member.member_id,
                'name': member.name
            })
        with open(self.members_file, 'w') as f:
            json.dump(members_data, f, indent=4)

        # Save transactions
        transactions_data = []
        for t in self.transactions:
            t_type = 'borrow' if isinstance(t, BorrowTransaction) else 'return'
            transactions_data.append({
                'transaction_id': t.transaction_id,
                'member_id': t.member_id,
                'book_id': t.book_id,
                'date': t.date,
                'type': t_type
            })
        with open(self.transactions_file, 'w') as f:
            json.dump(transactions_data, f, indent=4)

    def add_book(self, item_id, title, author, total_copies):
        if item_id in self.books:
            raise ValueError("Book ID already exists.")
        self.books[item_id] = Book(item_id, title, author, total_copies)
        self.save_data()

    def add_member(self, member_id, name):
        if member_id in self.members:
            raise ValueError("Member ID already exists.")
        self.members[member_id] = Member(member_id, name)
        self.save_data()

    def borrow_book(self, transaction_id, member_id, book_id):
        if member_id not in self.members:
            raise ValueError("Member not found.")
        if book_id not in self.books:
            raise ValueError("Book not found.")
        book = self.books[book_id]
        if book.available_copies <= 0:
            raise ValueError("No copies available to borrow.")
        book.available_copies -= 1
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = BorrowTransaction(transaction_id, member_id, book_id, date)
        self.transactions.append(transaction)
        self.save_data()

    def return_book(self, transaction_id, member_id, book_id):
        if member_id not in self.members:
            raise ValueError("Member not found.")
        if book_id not in self.books:
            raise ValueError("Book not found.")
        book = self.books[book_id]
        book.available_copies += 1
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = ReturnTransaction(transaction_id, member_id, book_id, date)
        self.transactions.append(transaction)
        self.save_data()

# GUI Application
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.library = LibrarySystem()

        self.create_widgets()

    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)

        # Tabs
        self.tab_books = ttk.Frame(tab_control)
        self.tab_members = ttk.Frame(tab_control)
        self.tab_transactions = ttk.Frame(tab_control)

        tab_control.add(self.tab_books, text='Books')
        tab_control.add(self.tab_members, text='Members')
        tab_control.add(self.tab_transactions, text='Transactions')

        tab_control.pack(expand=1, fill='both')

        self.create_books_tab()
        self.create_members_tab()
        self.create_transactions_tab()

    # Books tab
    def create_books_tab(self):
        frame = self.tab_books

        # Add book section
        add_frame = ttk.LabelFrame(frame, text="Add Book")
        add_frame.pack(fill='x', padx=10, pady=10)

        ttk.Label(add_frame, text="Book ID:").grid(row=0, column=0, sticky='w')
        self.book_id_entry = ttk.Entry(add_frame)
        self.book_id_entry.grid(row=0, column=1, sticky='w')

        ttk.Label(add_frame, text="Title:").grid(row=1, column=0, sticky='w')
        self.book_title_entry = ttk.Entry(add_frame)
        self.book_title_entry.grid(row=1, column=1, sticky='w')

        ttk.Label(add_frame, text="Author:").grid(row=2, column=0, sticky='w')
        self.book_author_entry = ttk.Entry(add_frame)
        self.book_author_entry.grid(row=2, column=1, sticky='w')

        ttk.Label(add_frame, text="Total Copies:").grid(row=3, column=0, sticky='w')
        self.book_copies_entry = ttk.Entry(add_frame)
        self.book_copies_entry.grid(row=3, column=1, sticky='w')

        ttk.Button(add_frame, text="Add Book", command=self.add_book).grid(row=4, column=0, columnspan=2, pady=5)

        # Book list
        list_frame = ttk.LabelFrame(frame, text="Books List")
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)

        columns = ('ID', 'Title', 'Author', 'Available/Total')
        self.books_tree = ttk.Treeview(list_frame, columns=columns, show='headings')
        for col in columns:
            self.books_tree.heading(col, text=col)
            self.books_tree.column(col, anchor='center')
        self.books_tree.pack(fill='both', expand=True)

        self.refresh_books_list()

    def add_book(self):
        item_id = self.book_id_entry.get().strip()
        title = self.book_title_entry.get().strip()
        author = self.book_author_entry.get().strip()
        copies = self.book_copies_entry.get().strip()

        if not item_id or not title or not author or not copies:
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            copies = int(copies)
            if copies <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Total copies must be a positive integer.")
            return

        try:
            self.library.add_book(item_id, title, author, copies)
            messagebox.showinfo("Success", "Book added successfully.")
            self.book_id_entry.delete(0, tk.END)
            self.book_title_entry.delete(0, tk.END)
            self.book_author_entry.delete(0, tk.END)
            self.book_copies_entry.delete(0, tk.END)
            self.refresh_books_list()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def refresh_books_list(self):
        for i in self.books_tree.get_children():
            self.books_tree.delete(i)
        for book in self.library.books.values():
            self.books_tree.insert('', tk.END, values=(book.item_id, book.title, book.author, f"{book.available_copies}/{book.total_copies}"))

    # Members tab
    def create_members_tab(self):
        frame = self.tab_members

        add_frame = ttk.LabelFrame(frame, text="Add Member")
        add_frame.pack(fill='x', padx=10, pady=10)

        ttk.Label(add_frame, text="Member ID:").grid(row=0, column=0, sticky='w')
        self.member_id_entry = ttk.Entry(add_frame)
        self.member_id_entry.grid(row=0, column=1, sticky='w')

        ttk.Label(add_frame, text="Name:").grid(row=1, column=0, sticky='w')
        self.member_name_entry = ttk.Entry(add_frame)
        self.member_name_entry.grid(row=1, column=1, sticky='w')

        ttk.Button(add_frame, text="Add Member", command=self.add_member).grid(row=2, column=0, columnspan=2, pady=5)

        list_frame = ttk.LabelFrame(frame, text="Members List")
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)

        columns = ('ID', 'Name')
        self.members_tree = ttk.Treeview(list_frame, columns=columns, show='headings')
        for col in columns:
            self.members_tree.heading(col, text=col)
            self.members_tree.column(col, anchor='center')
        self.members_tree.pack(fill='both', expand=True)

        self.refresh_members_list()

    def add_member(self):
        member_id = self.member_id_entry.get().strip()
        name = self.member_name_entry.get().strip()

        if not member_id or not name:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            self.library.add_member(member_id, name)
            messagebox.showinfo("Success", "Member added successfully.")
            self.member_id_entry.delete(0, tk.END)
            self.member_name_entry.delete(0, tk.END)
            self.refresh_members_list()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def refresh_members_list(self):
        for i in self.members_tree.get_children():
            self.members_tree.delete(i)
        for member in self.library.members.values():
            self.members_tree.insert('', tk.END, values=(member.member_id, member.name))

    # Transactions tab
    def create_transactions_tab(self):
        frame = self.tab_transactions

        trans_frame = ttk.LabelFrame(frame, text="Borrow / Return Book")
        trans_frame.pack(fill='x', padx=10, pady=10)

        ttk.Label(trans_frame, text="Transaction ID:").grid(row=0, column=0, sticky='w')
        self.trans_id_entry = ttk.Entry(trans_frame)
        self.trans_id_entry.grid(row=0, column=1, sticky='w')

        ttk.Label(trans_frame, text="Member ID:").grid(row=1, column=0, sticky='w')
        self.trans_member_entry = ttk.Entry(trans_frame)
        self.trans_member_entry.grid(row=1, column=1, sticky='w')

        ttk.Label(trans_frame, text="Book ID:").grid(row=2, column=0, sticky='w')
        self.trans_book_entry = ttk.Entry(trans_frame)
        self.trans_book_entry.grid(row=2, column=1, sticky='w')

        ttk.Button(trans_frame, text="Borrow Book", command=self.borrow_book).grid(row=3, column=0, pady=5)
        ttk.Button(trans_frame, text="Return Book", command=self.return_book).grid(row=3, column=1, pady=5)

        list_frame = ttk.LabelFrame(frame, text="Transactions List")
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)

        columns = ('Transaction ID', 'Type', 'Member ID', 'Book ID', 'Date')
        self.trans_tree = ttk.Treeview(list_frame, columns=columns, show='headings')
        for col in columns:
            self.trans_tree.heading(col, text=col)
            self.trans_tree.column(col, anchor='center')
        self.trans_tree.pack(fill='both', expand=True)

        self.refresh_transactions_list()

    def borrow_book(self):
        trans_id = self.trans_id_entry.get().strip()
        member_id = self.trans_member_entry.get().strip()
        book_id = self.trans_book_entry.get().strip()

        if not trans_id or not member_id or not book_id:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            self.library.borrow_book(trans_id, member_id, book_id)
            messagebox.showinfo("Success", "Book borrowed successfully.")
            self.trans_id_entry.delete(0, tk.END)
            self.trans_member_entry.delete(0, tk.END)
            self.trans_book_entry.delete(0, tk.END)
            self.refresh_books_list()
            self.refresh_transactions_list()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def return_book(self):
        trans_id = self.trans_id_entry.get().strip()
        member_id = self.trans_member_entry.get().strip()
        book_id = self.trans_book_entry.get().strip()

        if not trans_id or not member_id or not book_id:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            self.library.return_book(trans_id, member_id, book_id)
            messagebox.showinfo("Success", "Book returned successfully.")
            self.trans_id_entry.delete(0, tk.END)
            self.trans_member_entry.delete(0, tk.END)
            self.trans_book_entry.delete(0, tk.END)
            self.refresh_books_list()
            self.refresh_transactions_list()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def refresh_transactions_list(self):
        for i in self.trans_tree.get_children():
            self.trans_tree.delete(i)
        for t in self.library.transactions:
            t_type = 'Borrow' if isinstance(t, BorrowTransaction) else 'Return'
            self.trans_tree.insert('', tk.END, values=(t.transaction_id, t_type, t.member_id, t.book_id, t.date))

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
