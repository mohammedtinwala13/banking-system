# 🏦 Bank Account Management System (Python)
🏦 A Python-based Bank Account Management System featuring account creation, balance inquiry, deposits, withdrawals, fund transfers, account deactivation, JSON data storage, and email OTP verification using Gmail SMTP. Built with a modular structure to demonstrate file handling, authentication, and banking operations.
A simple command-line based Bank Account Management System built using Python. This project demonstrates modular programming, file handling, JSON data storage, OTP verification through email, and basic banking operations such as account creation, deposits, withdrawals, transfers, and account deactivation.

---

## 📌 Features

### Account Management

* Create new bank accounts
* Store customer information securely
* Generate unique account records

### Banking Operations

* Check account balance
* Deposit money
* Withdraw money
* Transfer money between accounts
* Deactivate accounts

### Security

* OTP (One-Time Password) verification through Gmail SMTP
* Email verification during account-related operations

### Data Management

* JSON-based data storage
* Runtime transaction tracking
* Automatic export of account data

---

# 📂 Project Structure

```text
Bank-Account-Management-System/
│
├── main.py
├── acc_creation.py
├── balance.py
├── deposit.py
├── withdrawal.py
├── transfer.py
├── deactivate.py
├── otp.py
├── makefile.py
├── global_var.py
│
├── accounts.json
├── transactions.json
│
└── README.md
```

---

# 📄 File Description

## main.py

Main driver file of the project.

Provides the menu-driven interface and calls all banking modules.

Functions:

* Create Account
* Check Balance
* Deposit Money
* Withdraw Money
* Transfer Funds
* Deactivate Account
* Export Data

---

## acc_creation.py

Handles new account creation.

Responsibilities:

* Collect customer details
* Validate inputs
* Create account records
* Store account information

---

## balance.py

Checks and displays account balance.

Responsibilities:

* Search account
* Retrieve balance
* Display available funds

---

## deposit.py

Handles money deposits.

Responsibilities:

* Validate account
* Update account balance
* Record transaction

---

## withdrawal.py

Handles money withdrawal operations.

Responsibilities:

* Verify sufficient balance
* Deduct amount
* Update records

---

## transfer.py

Transfers money between accounts.

Responsibilities:

* Validate sender account
* Validate receiver account
* Update both balances
* Log transaction

---

## deactivate.py

Deactivates an account.

Responsibilities:

* Verify account ownership
* Disable account operations
* Preserve historical records

---

## otp.py

Handles OTP generation and email delivery.

Responsibilities:

* Generate OTP
* Send OTP via Gmail
* Verify user-entered OTP

⚠️ IMPORTANT:
Before running the project, this file must be configured with your Gmail credentials.

---

## global_var.py

Stores runtime variables and generates final session summaries.

Responsibilities:

* Maintain transaction statistics
* Generate runtime reports
* Display session summary before exit

---

## makefile.py

Exports and saves data into JSON format.

Responsibilities:

* Store account data
* Export transaction records
* Create persistent storage

---

# 💻 Requirements

Install Python 3.8 or later.

Required libraries:

```bash
pip install json5
```

Most modules used in this project are built into Python:

```python
os
json
random
smtplib
email
datetime
```

---

# 🚀 How To Run

Clone the repository:

```bash
git clone https://github.com/yourusername/Bank-Account-Management-System.git
```

Navigate into the project directory:

```bash
cd Bank-Account-Management-System
```

Run:

```bash
python main.py
```

---

# 🔐 Email OTP Configuration

This project uses Gmail SMTP to send OTPs to users.

The following function is used inside `otp.py`:

```python
def send_otp_email(receiver_email, otp):
    sender_email = "YOUR EMAIL ADDRESS@gmail.com"
    app_password = "YOUR APP PASSWORD"

    message = f"Subject: OTP Verification\n\nYour OTP is {otp}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
```

---

# ⚠️ Required Changes Before Running

Open:

```text
otp.py
```

Replace:

```python
sender_email = "YOUR EMAIL ADDRESS@gmail.com"
```

with your Gmail address.

Replace:

```python
app_password = "YOUR APP PASSWORD"
```

with your Gmail App Password.

Example:

```python
sender_email = "example@gmail.com"
app_password = "abcd efgh ijkl mnop"
```

---

# 🔑 How To Generate Gmail App Password

Google no longer allows normal account passwords for SMTP login.

You must create a Gmail App Password.

---

## Step 1: Enable Two-Factor Authentication

Open:

https://myaccount.google.com/security

Under:

```text
How you sign in to Google
```

Enable:

```text
2-Step Verification
```

Complete the setup process.

---

## Step 2: Open App Passwords

Visit:

https://myaccount.google.com/apppasswords

Login if prompted.

---

## Step 3: Create New App Password

1. Click:

   ```text
   Select App
   ```

2. Choose:

   ```text
   Mail
   ```

3. Click:

   ```text
   Select Device
   ```

4. Choose:

   ```text
   Other (Custom Name)
   ```

5. Enter:

   ```text
   Bank Management System
   ```

6. Click:

   ```text
   Generate
   ```

---

## Step 4: Copy Generated Password

Google will generate a 16-character password.

Example:

```text
abcd efgh ijkl mnop
```

Copy it immediately.

---

## Step 5: Paste Into otp.py

```python
app_password = "abcd efgh ijkl mnop"
```

Save the file.

OTP emails will now be sent automatically.

---

# 📊 Sample Workflow

```text
1. Create Account
2. Verify Email using OTP
3. Deposit Funds
4. Check Balance
5. Transfer Money
6. Withdraw Funds
7. Deactivate Account
8. Export JSON Data
9. Exit Program
```

---

# 🛠 Technologies Used

* Python
* JSON
* SMTP
* Gmail App Password Authentication
* Modular Programming
* File Handling

---

# 🎯 Learning Objectives

This project demonstrates:

* Python Functions
* Python Modules
* File Handling
* JSON Storage
* Data Persistence
* Email Automation
* OTP Authentication
* Exception Handling
* Menu-Driven Programs
* Banking Transaction Logic

---

# 📷 Future Improvements

Possible enhancements:

* GUI using Tkinter
* Database Integration (MySQL/PostgreSQL)
* Password Hashing
* User Login System
* Account Statements
* Interest Calculation
* Transaction History
* Multi-user Support
* Flask/Django Web Version
* Mobile App Integration

---

# 📜 License

This project is developed for educational and learning purposes.

Feel free to fork, modify, and improve the project.

---

# 👨‍💻 Author

Developed as a Python Banking Management System project to learn:

* Python Programming
* Banking Logic
* Email Automation
* JSON Data Management
* Modular Software Development

⭐ If you found this project useful, consider giving it a star on GitHub.
