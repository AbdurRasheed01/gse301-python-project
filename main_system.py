from data_manager import get_all_students, find_student_by_name, add_new_student, student_profiles
from core_logic import get_validated_input, check_graduation_eligibility, find_top_performer, demonstrate_slicing, demonstrate_set_operations, score_to_grade, print_feedback, calculate_student_averages, identify_high_performers, identify_data_type, nested_scores_data

def display_menu():
    """Prints the main menu options."""
    print("\n" + "="*45)
    print("Student Academic Performance Analysis System")
    print("="*45)
    print("Menu Options ")
    print("1. View all students")
    print("2. Add new student")
    print("3. Check eligibility for graduation")
    print("4. Find top performer")
    print("5. Exit")
    print("-"*45)

def run_demonstrations():
    """Runs the demonstrations for slicing, set operations, and advanced challenges."""
        
    print("\n" + "="*45)
    print("ADVANCED CHALLENGES DEMONSTRATION ")
    print("="*45)
    
    # -- Nested Data Processing Demo ---
    print("\n---  Nested Data Processing ---")
    
    averages = calculate_student_averages(nested_scores_data)
    print("1. Average Scores:")
    for name, avg in averages.items():
        print(f"   {name}: {avg}")
    

    top_students = identify_high_performers(nested_scores_data, threshold=70)
    print("\n2. Students with ALL Scores Above 70:")
    if top_students:
        print(f"   {list(top_students.keys())}")
    else:
        print("   None found.")

    
    print("\n--- MATCH CASE Type Identification ---")
    print(f"Input (Integer): {identify_data_type(15)}")
    print(f"Input (Float): {identify_data_type(3.14)}")
    print(f"Input (List): {identify_data_type(['A', 'B'])}")
    print(f"Input (String): {identify_data_type('short text')}")
    print("----------------------------------")
def main_menu_system():
    """The core interactive menu system, using MATCH CASE."""
    
    run_demonstrations() # Run the non-interactive analysis parts first
    
    profiles = get_all_students()
    print("\nLoading student records... ")
    print(f"{len(profiles)} student profiles loaded successfully. ")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        
        match choice:
            case '1':
                print("\nList of Students: ")
                for i, student in enumerate(profiles):
                    print(f"{i+1}. {student['name']} ")
                print("-"*45)

            case '2':
                print("\nAdd New Student ")
                new_name = input("Enter name: ")
                new_matric = input("Enter matric number: ")
                
            
                new_age, new_cgpa = get_validated_input() 

                is_active_str = input("Is the student active (yes/no):").lower()
                new_is_active = is_active_str == 'yes'

                courses_str = input("Enter courses (comma separated):")
                new_courses = [c.strip() for c in courses_str.split(',')]

                new_student = {
                    "name": new_name,
                    "matric": new_matric,
                    "age": new_age,
                    "cgpa": new_cgpa,
                    "is_active": new_is_active,
                    "courses": new_courses,
                    "grades": {} 
                }
                
                add_new_student(new_student)
                print("-"*45)


            case '3':
                name_to_check = input("Enter student name: ")
                found_student = find_student_by_name(name_to_check) 

                if found_student:
                    
                    _, message = check_graduation_eligibility(found_student, outstanding_courses=0)
                    print(message)
                else:
                    print("Student not found.")
                print("-"*45)


            case '4': 
                top_student = find_top_performer(profiles)
                
                if top_student:
                    print("\nTop Performer: ")
                    print(f"Name: {top_student['name']} ")
                    print(f"Matric: {top_student['matric']} ")
                    print(f"CGPA: {top_student['cgpa']} ")
                    print(f"Courses: {top_student['courses']} ")
                else:
                    print("No students available.")
                print("-"*45)

            case '5':
                print("Exiting the system... ")
                print("Goodbye! ")
                break 

            case _:
                print("Invalid choice. Please select an option between 1 and 5.")

if __name__ == "__main__":
    main_menu_system()