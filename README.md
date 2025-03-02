# TempleFest

TempleFest is a Django-based web application that allows users to book festival services such as elephants for temples, fireworks, Kathakali performances, Chenda Melam, and more. This platform simplifies the process of arranging traditional festival services in Kerala.

## Features
- Book various festival services like elephants, fireworks, Kathakali, and Chenda Melam.
- User authentication and management.
- Admin dashboard to manage bookings and services.
- Responsive and user-friendly interface.

## Tech Stack
- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (default), can be configured for PostgreSQL/MySQL

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/TempleFest.git
   cd TempleFest
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```



