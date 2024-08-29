# E-Commerce Django Project

This is a Django-based e-commerce web application that allows users to browse products, add them to a cart, and proceed to checkout. The project is set up to handle media files, manage products through the Django admin interface, and display dynamic content using Django's templating engine.

## Features

- **Product Management**: Add, edit, and delete products from the admin interface.
- **Cart Functionality**: Users can add products to a cart, view the cart, and proceed to checkout.
- **Dynamic Pages**: The website dynamically displays products based on the data in the database.
  <!--- **User Authentication**: Supports user registration, login, and logout. -->

## Project Structure

- `shop`: The main app handling products and cart functionality.
- `blog`: A secondary app, if needed, for additional content or blog posts.
- `templates`: Directory containing all HTML templates.
- `static`: Directory containing static files (CSS, JS, images).
- `media`: Directory for storing media files like product images.

## Requirements

- **Python 3.x**
- **Django >= 3.2, < 4.0**
- **Pillow >= 8.2.0**
- **psycopg2 >= 2.9.1** (for PostgreSQL, optional)
- **django-environ >= 0.4.5**
- **django-humanize >= 0.0.9**
- **django-extensions >= 3.1.0**
- **whitenoise >= 5.3.0**
- **django-debug-toolbar >= 3.2.1** (optional)
- **django-cors-headers >= 3.7.0** (optional)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ecommerce-django.git
cd ecommerce-django
```

## 2. Set Up Virtual Environment

To isolate dependencies, create and activate a virtual environment.

### 2.1. Create Virtual Environment

Run the following command to create a virtual environment:

```bash
python -m venv djangoenv
```

## 2.2. Activate Virtual Environment

Activate the virtual environment using the following command:

- On Windows:

    ```bash
    djangoenv\Scripts\activate
    ```

- On macOS/Linux:

    ```bash
    source djangoenv/bin/activate
    ```

## 3. Install Required Packages

Install the necessary Python packages using `pip`:

```bash
pip install -r requirements.txt
```

This will install all the required packages listed in the requirements.txt file.

## 4. Set Up the Django Project

### 4.1. Start a New Django Project

Create a new Django project:

```bash
django-admin startproject ecommerce
```

### 4.2. Create a New App

Navigate to your project directory and create a new app:

```bash
cd ecommerce
python manage.py startapp shop
```

### 4.3. Add the App to Installed Apps

Open `ecommerce/settings.py` and add your app (`shop`) to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...,
    'shop',
]
```

### 4.4. Run your server

```bash
python manage.py runserver
```

# Contact Me

Feel free to reach out if you have any questions or want to get in touch. You can contact me through the following method:

## Email

- **Email**: [omernasir29@gmail.com](mailto:omernasir29@gmail.com)

