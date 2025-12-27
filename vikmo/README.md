# Vikmo – Sales Order & Inventory Management System

## Project Overview
This project is a backend Sales Order & Inventory Management System built using Django and Django REST Framework.
It simulates a simplified version of Vikmo’s B2B auto-parts platform where dealers place orders and inventory is
automatically managed based on order confirmations.

The system focuses on backend logic, database design, and RESTful APIs.

---

## Features Implemented
- Product management with unique SKU
- Inventory tracking per product
- Dealer management
- Order creation with multiple order items
- Order lifecycle: Draft → Confirmed → Delivered
- Stock validation before order confirmation
- Atomic inventory deduction to prevent race conditions
- Auto-generated order numbers
- Auto-calculation of line totals and order totals
- Django Admin panel for management

---

## Tech Stack
- Python 3.11
- Django 5.x
- Django REST Framework
- SQLite (default database)
- Postman / curl for API testing

---

## Project Structure
vikmo-sales-order/
├── manage.py
├── README.md
├── db.sqlite3
├── vikmo/
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── products/
├── dealers/
├── inventory/
└── orders/
---
## Setup Instructions

### 1. Clone / Extract Project
git clone <repository-url>
cd vikmo-sales-order
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install django djangorestframework
4. Apply Migrations
python manage.py makemigrations
python manage.py migrate
5. Create Superuser (Admin)
python manage.py createsuperuser
6. Run Server
python manage.py runserver

Admin Access
arduino
http://127.0.0.1:8000/admin/

Use superuser credentials to manage:
Products
Inventory
Dealers
Orders

# API Endpoints
Products
Method	Endpoint	Description
GET	/api/products/	List products
POST	/api/products/	Create product
GET	/api/products/{id}/	Product detail
PUT	/api/products/{id}/	Update product
DELETE	/api/products/{id}/	Delete product

Dealers
Method	Endpoint	Description
GET	/api/dealers/	List dealers
POST	/api/dealers/	Create dealer
GET	/api/dealers/{id}/	Dealer details

Orders
Method	Endpoint	Description
POST	/api/orders/	Create draft order
PUT	/api/orders/{id}/	Update draft order
POST	/api/orders/{id}/confirm/	Confirm order
POST	/api/orders/{id}/deliver/	Mark delivered

Inventory
Method	Endpoint	Description
GET	/api/inventory/	View inventory
PUT	/api/inventory/{product_id}/	Manual stock update

# Assumptions
1. Each product has exactly one inventory record
2. Inventory is deducted only when order is confirmed
3. Confirmed or delivered orders cannot be edited
4. Backend-only system (no frontend)

# Notes
1. Homepage / returns 404 by design (API-only project)
2. SQLite used for simplicity