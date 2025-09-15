# Django Blog

A simple Django blog application.

## Features
- List blog posts
- Admin interface
- SQLite database

## Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/aryalbirat/django-blog.git
   cd django-blog
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # Or
   source venv/bin/activate      # On Linux/Mac
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
- Visit `http://localhost:8000/` to view the blog.
- Visit `http://localhost:8000/admin/` for the admin interface.

## License
MIT
