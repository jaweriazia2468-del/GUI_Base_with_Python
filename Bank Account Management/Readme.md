Bank Account Management System (Python OOP)
A desktop-based financial management application developed in Python using the Tkinter library. This project serves as a practical implementation of advanced Object-Oriented Programming (OOP) concepts, specifically focusing on building a robust and scalable banking logic.

Key Features
Account Creation: Allows users to create different types of bank accounts (Savings or Checking) tied to a specific owner's name.

Transaction Management: Supports core banking operations including deposits and withdrawals with real-time balance updates.

Balance Inquiry: Provides an instant lookup feature to check the current balance of any registered account.

Error Handling & Validation: Implements comprehensive try-except blocks and messagebox alerts to handle invalid inputs, such as negative amounts or exceeding overdraft limits.

User-Friendly GUI: Organized into logical LabelFrame sections ("Create Account" and "Transactions") for an intuitive user experience.

Advanced OOP Concepts Applied
This project demonstrates the "Four Pillars of OOP" through the following implementations:

Abstraction: Uses the ABC (Abstract Base Class) module to define a template Account class. It enforces that any specific account type must implement its own deposit and withdraw methods.

Inheritance: The SavingsAccount and CheckingAccount classes inherit common attributes like owner and balance from the base Account class, reducing code redundancy.

Polymorphism: Different account types handle the withdraw method differently; for example, the Checking Account allows an overdraft of up to PKR 500, while the Savings Account strictly prevents any withdrawal exceeding the current balance.

Encapsulation: The internal state of the bank (the self.accounts dictionary) and individual account balances are managed through class methods, ensuring data integrity.

Project Structure
Account(ABC): The abstract base class defining the banking blueprint.

SavingsAccount: Concrete implementation with standard withdrawal rules.

CheckingAccount: Concrete implementation featuring a PKR 500 overdraft facility.

BankApp: The main GUI class that manages the Tkinter lifecycle and coordinates between the user interface and the account objects.

How to Run
Install Python: Ensure you have Python 3.x installed on your system.

Save the Script: Save the code as Bank Account.py.

Execute: Run the application via your terminal or IDE:

Bash

python "Bank Account.py"
