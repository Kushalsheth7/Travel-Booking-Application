# Travel Booking Application

## Setup Instructions

1. **Clone the repository**
   ```
   git clone <your-repo-url>
   cd <project-folder>
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

4. **Apply migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin)**
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```
   python manage.py runserver
   ```

7. **Access the app**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Features
- User registration, login, logout, and profile update
- Travel options listing, filtering, and booking
- View and cancel bookings
- Responsive UI with Bootstrap

## MySQL Setup (Optional)
- Update `DATABASES` in `travel_lyke/settings.py` for MySQL
- Install MySQL client:
  ```
  pip install mysqlclient
  ```
- Create a MySQL database and user, then update settings

## Testing
- To run tests:
  ```
  python manage.py test
  ```

## Deployment
- See Django docs for deployment to Google Cloud Platform or other services
