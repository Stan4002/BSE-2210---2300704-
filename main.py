# Student class - responsible for storing student data
class Student:
    def __init__(self, id, name, age, major):
        # Initialize a Student object with an ID, name, age, and major
        self.id = id
        self.name = name
        self.age = age
        self.major = major

    # String representation of the student object for easy printing
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

# StudentUpdater class - responsible for updating student information
class StudentUpdater:
    @staticmethod
    def update_student(student, **kwargs):
        # Dynamically update student attributes based on the provided keyword arguments
        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)

# StudentDatabase class - manages the collection of students
class StudentDatabase:
    def __init__(self):
        # Dictionary to store students with their ID as the key
        self.students = {}

    # Add a new student to the database
    def add_student(self, student):
        self.students[student.id] = student

    # Remove a student from the database by their ID
    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
        else:
            print(f"No student with ID {student_id} found.")

    # Retrieve a student object by ID
    def get_student(self, student_id):
        return self.students.get(student_id, None)

    # Display all students in the database
    def display_all_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students.values():
                print(student)

# StudentManagementSystem class - provides an interface to interact with the student database
class StudentManagementSystem:
    def __init__(self):
        # Initialize the system with an empty student database
        self.database = StudentDatabase()

    # Add a new student using the given details
    def add_new_student(self, id, name, age, major):
        if id in self.database.students:
            print(f"Student with ID {id} already exists.")
        else:
            student = Student(id, name, age, major)
            self.database.add_student(student)
            print(f"Student with ID {id} added successfully.")

    # Delete a student from the system by their ID
    def delete_student(self, student_id):
        self.database.remove_student(student_id)

    # Update an existing student's information
    def update_student_info(self, student_id, **kwargs):
        student = self.database.get_student(student_id)
        if student:
            # Only proceed if the student exists
            StudentUpdater.update_student(student, **kwargs)
            print(f"Student with ID {student_id} updated successfully.")
        else:
            # Inform user that the student does not exist
            print(f"No student with ID {student_id} found. Unable to update.")

    # Display all students in the system
    def show_all_students(self):
        self.database.display_all_students()

# Simple text-based menu system for user interaction
def menu():
    system = StudentManagementSystem()

    while True:
        # Display the menu options
        print("\nStudent Management System Menu")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student Information")
        print("4. View All Students")
        print("5. Exit")

        # Get user input
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            # Add a new student by asking for details
            try:
                id = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ")
                age = int(input("Enter Student Age: "))
                major = input("Enter Student Major: ")
                system.add_new_student(id, name, age, major)
            except ValueError:
                print("Invalid input. Please enter the correct data types.")

        elif choice == "2":
            # Delete a student by ID
            try:
                student_id = int(input("Enter Student ID to delete: "))
                system.delete_student(student_id)
            except ValueError:
                print("Invalid input. Please enter a valid student ID.")

        elif choice == "3":
            # Update an existing student's information
            try:
                student_id = int(input("Enter Student ID to update: "))
                # Check if student exists first before continuing
                if not system.database.get_student(student_id):
                    print(f"No student with ID {student_id} found.")
                else:
                    print("Leave a field empty if no update is needed.")
                    name = input("Enter new name (or press Enter to skip): ")
                    age = input("Enter new age (or press Enter to skip): ")
                    major = input("Enter new major (or press Enter to skip): ")

                    updates = {}
                    if name:
                        updates['name'] = name
                    if age:
                        try:
                            updates['age'] = int(age)
                        except ValueError:
                            print("Invalid input for age.")
                    if major:
                        updates['major'] = major

                    system.update_student_info(student_id, **updates)
            except ValueError:
                print("Invalid input. Please enter the correct data types.")

        elif choice == "4":
            # Show all students in the system
            system.show_all_students()

        elif choice == "5":
            # Exit the system
            print("Exiting the system. Goodbye!")
            break

        else:
            # Handle invalid menu options
            print("Invalid choice. Please select a valid option.")

# Run the menu system
if __name__ == "__main__":
    menu()
