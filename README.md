#  Event Booking System (Django + Docker)

A full-featured **Event Booking System** built with **Django** — allowing users to browse events, book tickets, and receive confirmation emails.  
The admin can manage events, bookings, and users efficiently through the Django admin panel.

----

##  Features

###  User Side

- User registration and login
- Browse available events
- View event details
- Book tickets for events
- Email notifications for successful bookings
- View all booked events in the user dashboard

###  Admin Side
- Add, edit, and delete events
- Manage bookings and users
- Send email updates to users
- Automatic signals for booking creation and notifications

----

## Tech Stack

- **Backend:** Django 5.2  
- **Frontend:** HTML, CSS (Bootstrap)
- **Database:** SQLite3 (default)
- **Containerization:** Docker
- **Email Notification:** Django Email Backend
- **Environment Management:** Poetry

---

##  Local Development Setup

### 1️ Clone the repository

```bash
git clone https://github.com/Sawan127/Event_management_system.git
cd event-booking-system

```

### 2️ Create and activate a virtual environment

```bash
poetry shell
poetry install
```
### 3️ Apply migrations

```bash
python manage.py migrate
```
### 4️ Create a superuser (for admin panel)

```bash
python manage.py createsuperuser
```
### 5️ Run the server

```bash
python manage.py runserver
```

----

## Docker Setup

### 1️ Build the Docker image

```bash
docker build -t event-booking-system .
```
### 2️ Run using Docker Compose

```bash
docker-compose up
```
### 3 Access the app

```bash
Visit 👉 http://localhost:8000
```
