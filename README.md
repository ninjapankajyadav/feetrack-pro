# FeeTrack Pro

A desktop application for managing tuition students, fee payments, invoices and receipts. Built with Python, CustomTkinter and MySQL.

Replaces paper registers and spreadsheets with a single searchable system: add students, search them instantly, generate numbered receipts and review month-wise fee reports.

## Screenshots

### Student Management
<img width="1366" height="731" alt="Student page" src="https://github.com/user-attachments/assets/ebdaca01-5059-47c2-9ccf-0c374ee6f042" />

### Invoice and Receipts
<img width="1366" height="727" alt="Invoice page" src="https://github.com/user-attachments/assets/43b8ad9b-a0c2-4261-95a6-aafdce03aea1" />

## Features

- **Student management:** add, edit and delete students; table view with search and filter
- **Search:** look up students by ID, name, class or phone
- **Invoices and receipts:** record fee payments and generate sequential receipt numbers (`RCP-00001` format)
- **Dashboard stats:** summary cards on the invoice page
- **Reports:** month-wise fee report
- **Persistent storage:** all data stored in MySQL
- **Sidebar navigation** between Home, Students, Invoice and Reports pages

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| GUI | CustomTkinter, ttk Treeview |
| Database | MySQL (`mysql-connector-python`) |

## Project Structure

| File | Purpose |
|---|---|
| `opening_page.py` | Entry point: main window, sidebar and page switching |
| `student_page.py` | Student list, search and filter, add/edit/delete |
| `invoice_page.py` | Fee invoice, receipt generation, student lookup |
| `Tuitionfee_DB.py` | Database layer (`tuitionDB` class): all SQL queries |

## Design Notes

- All database access goes through a single `tuitionDB` class, so the UI never contains raw SQL.
- Queries are parameterized (`%s`) and search columns are whitelisted through a mapping, which prevents SQL injection.
- Each page is a separate class, switched from the sidebar.

## Setup

**Prerequisites:** Python 3.11+, MySQL Server

1. Clone the repository
   ```bash
   git clone https://github.com/ninjapankajyadav/feetrack-pro.git
   cd feetrack-pro
   ```
2. Install dependencies
   ```bash
   pip install customtkinter mysql-connector-python
   ```
3. Create the database and tables
   ```sql
   CREATE DATABASE tuitionfee;
   ```
   Then run `schema.sql` inside it.
4. Set your MySQL credentials in `Tuitionfee_DB.py`
5. Run the app
   ```bash
   python opening_page.py
   ```

## Roadmap

- [ ] Flask web version with REST API
- [ ] Export receipts as PDF
- [ ] Fee defaulter reminders

## Author

**Pankaj Yadav**
BCA student (IGNOU), aspiring Python / backend developer

[LinkedIn](https://linkedin.com/in/pankaj-yadav-b564141b4) | [GitHub](https://github.com/ninjapankajyadav) | pankajyadav131875@gmail.com
