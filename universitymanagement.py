import pickle

class UniversityManagementSystem:
    def __init__(self):
        self.students = []
        self.faculty = []
        self.courses = []
        self.filename = "university_data.pkl"

    def load_data(self):
        
        try:
            with open(self.filename, "rb") as file:
                data = pickle.load(file)
                self.students = data.get("students", [])
                self.faculty = data.get("faculty", [])
                self.courses = data.get("courses", [])
            print("Data loaded successfully!")
        except FileNotFoundError:
            print("No data file found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_data(self):
        
        data = {
            "students": self.students,
            "faculty": self.faculty,
            "courses": self.courses
        }
        try:
            with open(self.filename, "wb") as file:
                pickle.dump(data, file)
            print("Data saved successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_student(self, name, student_id, department):
        
        student = {
            "name": name,
            "id": student_id,
            "department": department
        }
        self.students.append(student)
        self.save_data()  
        print(f"Student '{name}' added successfully!")

    def view_students(self):
        
        if not self.students:
            print("No students found.")
            return
        print("\n------- STUDENTS LIST -------")
        for student in self.students:
            print(f"Name: {student['name']}, ID: {student['id']}, Department: {student['department']}")

    def delete_student(self, student_id):
        
        for student in self.students:
            if student["id"] == student_id:
                self.students.remove(student)
                self.save_data()  
                print(f"Student with ID '{student_id}' deleted successfully!")
                return
        print(f"Student with ID '{student_id}' not found.")



def menu():
    ums = UniversityManagementSystem()
    ums.load_data() 

    while True:
        print("\n------- UNIVERSITY MANAGEMENT SYSTEM -------")
        print("1. add student")
        print("2. view students")
        print("3. delete student")
        print("4. Exit")
        choice = input("enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            department = input("Enter department: ")
            ums.add_student(name, student_id, department)
        elif choice == "2":
            ums.view_students()
        elif choice == "3":
            student_id = input("Enter the student ID to delete: ")
            ums.delete_student(student_id)
        elif choice == "4":
            print("Exiting the System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
