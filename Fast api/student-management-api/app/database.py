from typing import List, Dict, Any

# A simple list serving as our fake database
students_db: List[Dict[str, Any]] = [
    {
        "id": 1,
        "name": "Alice Smith",
        "age": 22,
        "course": "Mathematics"
    },
    {
        "id": 2,
        "name": "Bob Johnson",
        "age": 24,
        "course": "Physics"
    }
]

# Function to figure out the next available ID
def get_next_id() -> int:
    if not students_db:
        return 1
    return max(student["id"] for student in students_db) + 1
