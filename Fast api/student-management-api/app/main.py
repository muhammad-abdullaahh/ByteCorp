from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import router as student_router

# Create the FastAPI app
app = FastAPI(
    title="Student Management API",
    description="A simple API for managing students using FastAPI.",
    version="1.0.0"
)

# Connect the student routes (endpoints) to our app
app.include_router(student_router)

# Serve the static files (like CSS and Javascript) from the app/static folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# When someone visits the main page (/), show them the index.html file
@app.get("/")
def read_root():
    return FileResponse("app/static/index.html")
