from pydantic import BaseModel, Field
from typing import Optional

# The base blueprint for a student with required fields
class StudentBase(BaseModel):
    name: str = Field(..., description="Full name of the student", example="John Doe")
    age: int = Field(..., gt=0, description="Age of the student (must be positive)", example=20)
    course: str = Field(..., description="Course the student is enrolled in", example="Computer Science")

# Used when creating a new student
class StudentCreate(StudentBase):
    pass

# Used when updating a student (all fields are optional)
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None

# Used when sending student data back to the user (includes the ID)
class Student(StudentBase):
    id: int
