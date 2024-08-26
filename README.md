# BSE 2210  (2300704)
 Assignment 2

## Student Management System

# Overview
This is a simple Python-based Student Management System designed to manage student records in a database. Users can perform tasks like adding students, deleting students, updating their information, and viewing all students. The system has been refactored to follow key software design principles like SOLID, DRY, KISS, and YAGNI.

## Features

- Add new students to the system.
- Delete students based on their ID.
- Update student information (name, age, major).
- View all students currently in the system.
- Verify whether a student exists before making updates or deletions.

## File Structure

- `student_management_system.py`: Main file containing the Student Management System, including the classes `Student`, `StudentUpdater`, `StudentDatabase`, and `StudentManagementSystem`, as well as the menu for user interaction.

## How to Run the System

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Stan4002/BSE-2210---2300704-.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd BSE-2210---2300704-
    ```
3. **Run the system**:
    - Ensure you have Python 3 installed.
    - In the terminal, run:
    ```bash
    python student_management_system.py
    ```

4. **Follow the prompts** in the menu to interact with the system:
    - Option 1: Add a new student.
    - Option 2: Delete an existing student by ID.
    - Option 3: Update a student’s details (with checks to ensure the student exists).
    - Option 4: View all students.
    - Option 5: Exit the system.







