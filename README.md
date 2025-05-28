# 🛒 eCommerce API with JWT & Discounts
A Django-React based eCommerce platform with JWT authentication, supporting user-specific cart, order checkout, and conditional discount codes. Includes admin analytics and unit tests for a robust backend system.

---

## 🚀 Features

- User authentication via JWT
- Add to cart, view cart, checkout
- Automatic discount code generation for every nth order
- Admin-only endpoints for (RBAC)
- Role-based permissions (`is_customer`, `is_admin_user`)
- Unit tests included

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/abhaybraja/ecommerce.git
cd ecommerce

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Create tow users with role is_customer and is_admin_user
```

## 🔐 Authentication
Obtain token:
```bash

POST /api/token/
{
  "username": "user1",
  "password": "Abc@1234"
}


```

## 🧪 Running Tests

```bash
python manage.py test

```


## 📬 API Endpoints

| Method | Endpoint                              | Description               |
| ------ | ------------------------------------- | ------------------------- |
| POST   | `/api/token/`                         | Login and get JWT token   |
| POST   | `/api/token/refresh/`                 | Refresh access token      |
| GET    | `/api/inventory/products/`            | List products             |
| POST   | `/api/store/cart/add/`                | Add item to cart          |
| GET    | `/api/store/cart/view/`               | View cart                 |
| POST   | `/api/store/checkout/`                | Checkout and place order  |
| POST   | `/api/store/admin/generate-discount/` | Generate discount (admin) |
| GET    | `/api/store/admin/analytics/`         | View analytics (admin)    |


Note: Assignment Completed