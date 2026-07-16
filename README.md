\# 📚 Library Management System



A full-stack Library Management System built with Python (Django) that goes beyond a simple book catalog — it supports book issue/return tracking, automatic overdue fine calculation, and live search, with a clean Bootstrap UI.



\## 🚀 Features



\- \*\*Book Catalog\*\* — Add, edit, delete, and search books

\- \*\*Issue \& Return System\*\* — Issue books to borrowers with an auto-calculated 14-day due date

\- \*\*Overdue Fine Calculation\*\* — Automatically calculates ₹5/day late fee when a book is returned past its due date

\- \*\*Active Transactions Tracking\*\* — View all currently issued books with Overdue/On Time status

\- \*\*Delete Protection\*\* — Prevents deleting a book that's currently issued to someone

\- \*\*Live Search\*\* — Client-side instant search by title or author

\- \*\*Responsive UI\*\* — Bootstrap 5 card-based design, works on mobile and desktop



\## 🛠️ Tech Stack



\- \*\*Backend:\*\* Python, Django

\- \*\*Frontend:\*\* HTML, Bootstrap 5, Bootstrap Icons, JavaScript

\- \*\*Database:\*\* SQLite (default Django DB)

## 📸 Screenshots

### Book List
![Book List](list.png)

### Add Book
![Add Book](add_books.png)

### Issue Book
![Issue Book](issue_book.png)

### Active Transactions
![Transactions](transaction.png)



\## ⚙️ Installation \& Setup



1\. Clone the repository

```bash

&#x20;  git clone https://github.com/mangalapurivijayalakshmi/library-management-system.git

&#x20;  cd library-management-system

```



2\. Install Django

```bash

&#x20;  pip install django

```



3\. Run migrations

```bash

&#x20;  python manage.py makemigrations

&#x20;  python manage.py migrate

```



4\. Start the server

```bash

&#x20;  python manage.py runserver

```



5\. Open in browser

