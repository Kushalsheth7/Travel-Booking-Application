
# Travel Booking Application

## Setup Instructions

1. **Clone the repository**
   ```
   git clone https://github.com/Kushalsheth7/Travel-Booking-Application.git
   cd Travel-Booking-Application
   ```

2. **Create and activate a virtual environment**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Install MySQL and create database**
   - Download and install MySQL Community Server and MySQL Workbench.
   - Start MySQL server and connect using MySQL Workbench.
   - Run:
     ```sql
     CREATE DATABASE travel_lyke_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
     ```

5. **Configure database settings**
   - Edit `travel_lyke/settings.py` and set your MySQL username and password in the `DATABASES` section.

6. **Apply migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser (admin)**
   ```
   python manage.py createsuperuser
   ```

8. **Add mock travel options data**
   ```
   python manage.py create_mock_data
   ```

9. **Run the development server**
   ```
   python manage.py runserver
   ```

10. **Access the app**
    - Main site: http://127.0.0.1:8000/
    - Admin panel: http://127.0.0.1:8000/admin/

## Features
- User registration, login, logout, and profile update
- Travel options listing, filtering, and booking
- View and cancel bookings (with seat restoration)
- Responsive UI with Bootstrap
- Admin dashboard for managing travel options and bookings
- Mock data for testing
- MySQL database support

## Testing
- To run tests:
  ```
  python manage.py test
  ```

## Deployment
- See Django docs for deployment to Google Cloud Platform or other services


mysql -u KushalSheth -p -h KushalSheth.mysql.pythonanywhere-services.com
SHOW DATABASES;
USE your_db_name;
SHOW TABLES;
KushalSheth$Travel
SELECT * FROM auth_user LIMIT 5;
