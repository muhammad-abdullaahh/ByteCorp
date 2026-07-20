from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import Student, StudentCreate, StudentUpdate
from app.database import students_db, get_next_id

# Group all these routes under the /students URL path
router = APIRouter(prefix="/students", tags=["Students"])

# Get a list of all students
@router.get("/", response_model=List[Student])
def get_all_students():
    return students_db

# Get a single student by their ID
@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students_db:
        if student["id"] == student_id:
            return student
            
    # Return a 404 error if the student isn't found
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

# Add a new student
@router.post("/", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    # Convert data to a dictionary and assign an ID
    new_student = student.model_dump() 
    new_student["id"] = get_next_id()
    
    # Save it to our database list
    students_db.append(new_student)
    return new_student

# Update an existing student
@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student_update: StudentUpdate):
    for index, student in enumerate(students_db):
        if student["id"] == student_id:
            # Only update the fields the user provided
            update_data = student_update.model_dump(exclude_unset=True)
            students_db[index].update(update_data)
            return students_db[index]
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

# Delete a student
@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    for index, student in enumerate(students_db):
        if student["id"] == student_id:
            del students_db[index]
            return 
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
