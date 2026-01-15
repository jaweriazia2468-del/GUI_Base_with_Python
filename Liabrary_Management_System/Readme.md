Library Management System (Python OOP)

A sophisticated desktop application built with Python and Tkinter to manage library operations. This system demonstrates high-level Object-Oriented Programming (OOP), automated file persistence using JSON, and a professional multi-tabbed interface.

🚀 Key Features
Multi-Tab Interface: Organized into three dedicated sections: Books, Members, and Transactions for streamlined workflow.

Inventory Management: Add new books with unique IDs, tracking authors, and maintaining real-time counts of total versus available copies.

Member Registration: Simple interface to enroll members with unique identification numbers.

Transaction Tracking: Advanced logic for borrowing and returning books that automatically updates stock levels and logs the exact date and time of the action.

Persistent Storage: Integrated file handling that automatically saves and loads data from books.json, members.json, and transactions.json, ensuring data is never lost when the app closes.

Real-time Data Tables: Uses ttk.Treeview to display live, sortable lists of all items and activities in the system.

🛠️ Advanced OOP Concepts Applied
This project serves as a masterclass in the Four Pillars of OOP:

Abstraction: The LibraryItem and Transaction classes are defined as Abstract Base Classes (ABC). They provide a blueprint for all items and logs, enforcing a consistent display() method across the application.

Inheritance: * Book inherits from LibraryItem, extending it with author and copy-tracking attributes.

BorrowTransaction and ReturnTransaction inherit from the base Transaction class, specializing in their respective log formats.

Polymorphism: The system handles different types of transactions dynamically. When refreshing the transaction list, it identifies the type (Borrow vs. Return) and displays it accordingly within the same interface.

Encapsulation: The LibrarySystem class encapsulates all the "business logic" and file operations, keeping it separate from the LibraryApp class which handles the visual display.

📂 System Architecture
LibraryItem (ABC): The root abstract class for all physical inventory.

LibrarySystem: The core engine that manages data loading, saving, and the logic for adding items or processing borrows/returns.

LibraryApp: The Tkinter-based GUI that manages the Notebook (tabbed) layout and user interactions.

JSON Persistence: Uses the json module to serialize Python objects into human-readable files.

🚦 How to Run
Prerequisites: Ensure you have Python 3.x installed.

Setup: Save the code as library_system.py.

Execution: Run the script:

Bash

python library_system.py
The system will automatically create the .json database files in your folder upon the first run.
