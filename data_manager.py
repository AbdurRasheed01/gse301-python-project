
#  Data Collection and Storage

# List of dictionaries for each student's full profile
# This is the primary data storage for the system
student_profiles = [
    {
        "name": "Rasheed Fatia",
        "matric": "23/60AC389",
        "age": 20,
        "cgpa": 4.81,
        "is_active": True,
        "courses": ["ELE567", "Data Science", "Statistics"],
        "grades": {"ELE567": "A", "Data Science": "A", "Statistics": "A"}
    },
    {
        "name": "Yusuf Adeoye",
        "matric": "23/70JC093",
        "age": 21,
        "cgpa": 3.45,
        "is_active": True,
        "courses": ["Python", "Networking", "Database"],
        "grades": {"Python": "B", "Networking": "C", "Database": "B"}
    },
    {
        "name": "Moses Oyedele",
        "matric": "23/50AB123",
        "age": 22,
        "cgpa": 3.10,
        "is_active": True,
        "courses": ["Algorithms", "Security"],
        "grades": {"Algorithms": "C", "Security": "C"}
    },
    {
        "name": "Timi Abidoye",
        "matric": "23/90ZD456",
        "age": 19,
        "cgpa": 4.05,
        "is_active": True,
        "courses": ["Data Science", "Statistics"],
        "grades": {"Data Science": "A", "Statistics": "B"}
    },
    {
        "name": "Nimah Nina",
        "matric": "23/80XC111",
        "age": 19,
        "cgpa": 2.20,
        "is_active": False,
        "courses": ["Algorithms", "Security"],
        "grades": {"Algorithms": "D", "Security": "F"}
    }
]

# Set to store unique courses offered (it automatically handle duplicates)
unique_courses = {"Python", "Data Science", "Statistics", "Algorithms", "Networking", "Database", "Security"}

# Tuple for fixed department information
department_info = ("Computer Science Department", "Faculty of Technology", 2025)

def add_new_student(student_data):
    """Appends a new student dictionary to the global student_profiles list."""
    student_profiles.append(student_data)
    print("Student record added successfully.")

def get_all_students():
    """Returns the list of all student profiles."""
    return student_profiles

def find_student_by_name(name):
    """Searches for a student profile based on name."""
    for student in student_profiles:
        if student["name"].lower() == name.lower():
            return student
    return None