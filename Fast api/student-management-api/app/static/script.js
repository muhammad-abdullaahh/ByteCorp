// The base URL for our API endpoints
const API_URL = '/students';

// Run this code when the web page finishes loading
document.addEventListener('DOMContentLoaded', () => {
    // Load the initial list of students
    fetchStudents();
    
    // Listen for the form submission to add a new student
    document.getElementById('addStudentForm').addEventListener('submit', async (e) => {
        e.preventDefault(); // Stop the page from reloading
        
        // Get the values from the form inputs
        const name = document.getElementById('name').value;
        const age = document.getElementById('age').value;
        const course = document.getElementById('course').value;
        
        // Send the new student to the backend
        await addStudent({ name, age: parseInt(age), course });
        
        // Clear the form
        e.target.reset();
    });
});

// Fetch all students from the backend and show them on the screen
async function fetchStudents() {
    try {
        const response = await fetch(API_URL);
        const students = await response.json();
        renderStudents(students);
    } catch (error) {
        console.error('Error fetching students:', error);
        alert('Failed to load students.');
    }
}

// Draw the students in the HTML table
function renderStudents(students) {
    const tbody = document.getElementById('studentTableBody');
    tbody.innerHTML = ''; // Clear the table first
    
    // Show a message if there are no students
    if (students.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: var(--text-muted);">No students found. Add one above!</td></tr>';
        return;
    }
    
    // Create a new row for each student
    students.forEach(student => {
        const tr = document.createElement('tr');
        
        tr.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>
            <td>${student.course}</td>
            <td>
                <button class="delete-btn" onclick="deleteStudent(${student.id})">Delete</button>
            </td>
        `;
        
        tbody.appendChild(tr);
    });
}

// Send a POST request to create a new student
async function addStudent(studentData) {
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(studentData) // Convert Javascript object to JSON string
        });
        
        if (!response.ok) {
            throw new Error('Failed to add student');
        }
        
        // Refresh the list after adding
        await fetchStudents();
    } catch (error) {
        console.error('Error adding student:', error);
        alert('Failed to add student.');
    }
}

// Send a DELETE request to remove a student
async function deleteStudent(id) {
    if (!confirm('Are you sure you want to delete this student?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) {
            throw new Error('Failed to delete student');
        }
        
        // Refresh the list after deleting
        await fetchStudents();
    } catch (error) {
        console.error('Error deleting student:', error);
        alert('Failed to delete student.');
    }
}
