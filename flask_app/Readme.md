# Flask Product Management API

A lightweight **Flask + SQLAlchemy** application built for practicing and demonstrating **integration testing** using **pytest**.  
The project defines REST API endpoints for managing **Products**, includes automated integration tests that verify real API interactions via Flask’s test client.


# Project Structure
flask_app/
│
├── app.py # Main Flask application (API)
├── test_app.py # Integration tests using pytest
├── mydb.db # SQLite database (auto-created)
└── README.md # Project documentation

# Prerequisites
- **Python 3.11+**
- **Flask** — micro web framework  
- **Flask-SQLAlchemy** — ORM for SQLite  
- **SQLite** — lightweight embedded database  
- **Pytest** — integration testing framework 

# Install Dependencies
pip install flask flask_sqlalchemy pytest requests
pip freeze > requirements.txt

# Running the Flask App and all the Tetss
