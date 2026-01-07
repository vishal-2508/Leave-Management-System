# Leave Management System

A Django-based Leave Management System that allows employees to apply for leave and managers to manage leave requests effectively.

## Overview

This project provides a simple and intuitive interface for:

- Employees to **apply for leaves**
- Managers to **approve or reject leave requests**
- Viewing leave records
- Managing user accounts (employees and Managers)


## Features

✔ Apply for leave with start/end dates  
✔ View leave status (approved / pending / rejected)  
✔ Manager dashboard for managing requests  
✔ User authentication and role-based access  
✔ Easy to run locally with SQLite

## Project Rules

- The leave end date cannot precede the start date.
- New leave requests must default to a "Pending" status.
- Employees cannot approve their own leave requests.
- Only users with the Manager role can modify leave statuses.

## Tech Stack

The project is built using:

- **Python**  
- **Django Framework**  
- **SQLite** (default database)  
- **HTML/CSS** for basic UI
- **JavaScript**
 
## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/vishal-2508/Leave-Management-System.git
   cd Leave-Management-System

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Apply migrations**
   ```bash
   python manage.py migrate

5. **Run the development server**
   ```bash
   python manage.py runserver

6. **Open in browser**
   ```bash
   http://127.0.0.1:8000/

## Project Structure

  ```bash
  Leave-Management-System/
  │
  ├── accounts/                     # Django app for authentication & profiles
  │   ├── migrations/
  │   ├── admin.py
  │   ├── apps.py
  │   ├── models.py
  │   ├── views.py
  │   ├── urls.py
  │   └── templates/accounts/
  │
  ├── leave/                        # Django app for leave management
  │   ├── migrations/
  │   ├── admin.py
  │   ├── apps.py
  │   ├── models.py
  │   ├── views.py
  │   ├── urls.py
  │   └── templates/leave/
  │
  ├── leave_management_system/      # Core Django project settings
  │   ├── __init__.py
  │   ├── asgi.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  │
  ├── db.sqlite3                    # Local SQLite database
  ├── manage.py                     # Django CLI script
  ├── requirements.txt              # Python dependencies
  └── README.md                    # Project documentation
  ```


## Visual ER Diagram

   ```bash

                                 +-----------------+          +---------------------+
                                 |      User       | 1      ∞ |    LeaveRequest     |
                                 |-----------------|----------|---------------------|
                                 | id (PK)         |          | id (PK)             |
                                 | username        |          | user_id (FK)        |
                                 | email           |          | leave_type          |
                                 | password        |          | leave_reason        |
                                 | first_name      |          | leave_start_date    |
                                 | last_name       |          | leave_end_date      |
                                 | user_type       |          | leave_status        |
                                 |                 |          | leave_remark        |
                                 +-----------------+          +---------------------+

   ```

## Postman Documentation

#### You can also import the Postman collection:
1. Open Postman
2. Go to Import
3. Paste this URL:
   ```bash
   https://documenter.getpostman.com/view/47277153/2sBXVeDrmn
   ```
4. Postman will load the collection with all documented endpoints.
#### You can then test all API endpoints directly from Postman.



