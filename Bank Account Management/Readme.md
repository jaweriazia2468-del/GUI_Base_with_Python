# 🏦 Bank Account Management System (Python Tkinter)

## 📌 Project Overview

The Bank Account Management System is a desktop GUI application developed using **Python** and **Tkinter**. It demonstrates Object-Oriented Programming (OOP) concepts including **Abstraction, Inheritance, and Polymorphism** while providing a simple banking environment where users can create accounts, deposit money, withdraw money, and check balances.

The application supports two account types:

- Savings Account
- Checking Account

---

## ✨ Features

- Create Savings Account
- Create Checking Account
- Deposit Money
- Withdraw Money
- Check Account Balance
- Input Validation
- Error Handling
- Graphical User Interface (GUI)

---

## 🛠 Technologies Used

- Python 3
- Tkinter
- Object-Oriented Programming (OOP)

---

## 📚 OOP Concepts Implemented

### Abstraction

The abstract class `Account` defines common methods:

- deposit()
- withdraw()

These methods are implemented by child classes.

---

### Inheritance

The following classes inherit from `Account`:

- SavingsAccount
- CheckingAccount

---

### Polymorphism

Both account types implement their own version of:

- deposit()
- withdraw()

The GUI interacts with accounts without knowing which specific account type is being used.

---

## 📂 Project Structure

```
BankAccountManagement/
│
├── bank.py
└── README.md
```

---

## 🚀 How to Run

### Step 1

Install Python 3.

### Step 2

Clone the repository.

```bash
git clone https://github.com/javeru=iazia26/BankAccountManagement.git
```

### Step 3

Navigate to the project.

```bash
cd BankAccountManagement
```

### Step 4

Run the application.

```bash
python bank.py
```

---

## 💻 GUI Sections

### Create Account

- Owner Name
- Savings Account
- Checking Account
- Create Account Button

---

### Transactions

- Owner Name
- Amount
- Deposit
- Withdraw
- Check Balance

---

## ⚙ Business Rules

### Savings Account

- Deposit amount must be positive.
- Withdrawal amount must be positive.
- Cannot withdraw more than available balance.

---

### Checking Account

- Deposit amount must be positive.
- Withdrawal amount must be positive.
- Allows overdraft up to PKR 500.

---

## ✔ Validation

The system validates:

- Empty owner name
- Duplicate account
- Invalid amount
- Negative amount
- Insufficient balance
- Overdraft limit
- Account existence

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python GUI Programming
- Object-Oriented Programming
- Abstract Classes
- Polymorphism
- Exception Handling
- Event-Driven Programming

---

## 📸 Application Workflow

1. Create an account.
2. Select account type.
3. Deposit money.
4. Withdraw money.
5. Check balance.

---

## Future Improvements

- Login System
- PIN Authentication
- Transaction History
- SQLite Database
- Account Number Generation
- Interest Calculation
- Money Transfer
