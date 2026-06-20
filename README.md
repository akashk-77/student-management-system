# Student Management System

A web app for managing student records — create, update, delete, and search. Built with a FastAPI backend and a React frontend, backed by a MySQL database.

## Tech stack

- **Frontend:** React
- **Backend:** Python, FastAPI
- **Database:** MySQL, accessed via SQLAlchemy
- **API style:** REST (JSON over HTTP)

## Prerequisites

- [Node.js](https://nodejs.org) (includes npm)
- [Python 3.10+](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/) running locally or accessible remotely

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/akashk-77/student-management-system.git
cd student-management-system
```

### 2. Set up the database
Create a MySQL database for the project, e.g.:
```sql
CREATE DATABASE student_management;
```

### 3. Backend setup
```bash
cd backend/app
python -m venv venv
```

Activate the virtual environment:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy pymysql
```

Update your database connection details (host, username, password, database name) in the relevant config/settings file before running the server.

Run the backend:
```bash
uvicorn main:app --reload
```
> Replace `main:app` with the actual entry point filename if different (e.g. `app.main:app`).

The API will be available at `http://localhost:8000`. FastAPI also provides interactive docs at `http://localhost:8000/docs`.

### 4. Frontend setup
In a new terminal:
```bash
cd frontend
npm install
npm start
```

The app will open at `http://localhost:3000`.

## Features

- Create new student records
- View / search existing records
- Update student details
- Delete records

