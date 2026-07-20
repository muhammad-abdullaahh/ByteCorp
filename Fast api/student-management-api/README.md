# Student Management API

This project is my internship task aimed at learning and implementing a basic CRUD application using **FastAPI**.

## Project Features
*   **FastAPI Backend**: A lightweight, fast backend using Python.
*   **Pydantic Models**: Automatic data validation and serialization.
*   **Vanilla JS/HTML/CSS Frontend**: A clean, minimalistic web interface that interacts dynamically with the API.
*   **In-Memory Database**: A temporary list-based database for learning CRUD operations (Create, Read, Update, Delete).

## How to Run

1.  Make sure you have your dependencies installed:
    ```bash
    pip install -r requirements.txt
    ```
2.  Navigate to the `student-management-api` root directory.
3.  Start the server using Uvicorn:
    ```bash
    uvicorn app.main:app --reload
    ```
4.  Open your browser and visit `http://127.0.0.1:8000/` to use the Graphical User Interface.
5.  Alternatively, visit `http://127.0.0.1:8000/docs` to see the automatic, interactive API documentation provided by FastAPI.
