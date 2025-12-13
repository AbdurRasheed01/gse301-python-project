from data_manager import student_profiles 
import sys # Used for safe exit

# Data Processing and Logic

def score_to_grade(score):
    """Converts a score (0-100) to a letter grade using IF-ELIF-ELSE."""
    # Demonstration of IF, ELIF, ELSE logic 
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 50 <= score < 60:
        return "E"
    else: # score < 50
        return "F"

def print_feedback(grade):
    """Prints feedback based on the grade using MATCH CASE."""
    # Demonstration of MATCH CASE logic
    match grade:
        case "A":
            print(">>> Excellent work! Keep it up.")
        case "B":
            print(">>> Very good performance.")
        case "C":
            print(">>> Satisfactory. Aim higher next time.")
        case "D" | "E":
            print(">>> Passed, but attention is needed.")
        case "F":
            print(">>> Failed. Immediate action is required.")
        case _:
            print(">>> Invalid grade received.")

def get_validated_input():
    """Asks user for age and CGPA as strings, converts them, and validates."""
    validated_age = None
    validated_cgpa = None

    # Use TRY EXCEPT to handle invalid age input 
    while validated_age is None:
        age_str = input("Enter age (16-40): ") 
        try:
            age_int = int(age_str) 
            if 16 <= age_int <= 40: # Validation
                validated_age = age_int
            else:
                print("Age must be between 16 and 40. Please try again.")
        except ValueError:
            print("Invalid input. Age must be a whole number.")
        except Exception as e:
            # General exception handling for unexpected errors
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

    # Use TRY EXCEPT to handle invalid CGPA input
    while validated_cgpa is None:
        cgpa_str = input("Enter CGPA (0.0-5.0): ") 
        try:
            cgpa_float = float(cgpa_str) 
            if 0.0 <= cgpa_float <= 5.0: # Validation
                validated_cgpa = cgpa_float
            else:
                print("CGPA must be between 0.0 and 5.0. Please try again.")
        except ValueError:
            print("Invalid input. CGPA must be a number (e.g., 3.50).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

    return validated_age, validated_cgpa


# ---  Analysis and Reporting ---

def demonstrate_slicing(scores):
    """Demonstrates list operations and slicing."""
    
    scores.sort(reverse=True)
    
    top_3_scores = scores[:3] 
    
    last_5_scores = scores[-5:] 
    
    every_other_score = scores[::2] 
    
    print("--- List Slicing Demonstration ---")
    print(f"Scores (Sorted): {scores}")
    print(f"Top 3 Scores: {top_3_scores}")
    print(f"Last 5 Scores: {last_5_scores}")
    print(f"Every Other Score: {every_other_score}")
    print("----------------------------------")

def demonstrate_set_operations(set_pass, set_merit):
    """Demonstrates intersection, union, and difference of sets."""
    
    
    intersection_set = set_pass.intersection(set_merit) 

    union_set = set_pass.union(set_merit) 

    difference_set = set_pass.difference(set_merit) 

    print("--- Set Operations Demonstration ---")
    print(f"Passed Python: {set_pass}")
    print(f"Merit (CGPA > 4.0): {set_merit}")
    print(f"Passed and Merit (Intersection): {intersection_set}")
    print(f"All Distinct Students (Union): {union_set}")
    print(f"Passed but No Merit (Difference): {difference_set}")
    print("----------------------------------")


# --- Interactive Menu Logic ---

def check_graduation_eligibility(student_profile, outstanding_courses=0):
    """
    Checks if a student is eligible for graduation using logical operators.
    Criteria: CGPA >= 2.5 AND no outstanding courses AND is_active is True.
    """
    cgpa = student_profile.get("cgpa", 0.0)
    is_active = student_profile.get("is_active", False)

    is_eligible = (cgpa >= 2.5) and (outstanding_courses == 0) and is_active 

    message = f"Matric Number: {student_profile.get('matric', 'N/A')}\n"
    message += f"CGPA: {cgpa}\n"
    message += f"Outstanding Courses: {outstanding_courses}\n"
    message += f"Active Status: {is_active}\n"
    message += "Eligibility Result:"

    if is_eligible:
        message += f"\n{student_profile['name']} is eligible for graduation."
    else:
        message += f"\n{student_profile['name']} is NOT eligible for graduation."

    return is_eligible, message 

def find_top_performer(profiles):
    """Finds the student with the highest CGPA."""
    if not profiles:
        return None
        
    # Find the student dictionary with the maximum CGPA value
    top_student = max(profiles, key=lambda s: s['cgpa'])
    return top_student

# ---  Advanced Challenges - Nested Data Processing ---

# Data structure for this specific challenge
nested_scores_data = {
    "Rasheed Fatia": {
        "Python": 95,
        "Statistics": 92,
        "Algorithms": 88
    },
    "Moses Oyedele": {
        "Python": 75,
        "Statistics": 68,
        "Algorithms": 72
    },
    "Nimah Nina": {
        "Python": 78,
        "Data Science": 81,
        "Networking": 70
    },
    "Timi Abidoye": {
        "Python": 65,
        "Data Science": 75,
        "Networking": 69
    }
}

def calculate_student_averages(data):
    """
    Calculates the average score for each student from a nested dictionary of scores.
    """
    student_averages = {}
    
    for student_name, scores in data.items():
        score_values = scores.values()
        
        total_score = sum(score_values)
        course_count = len(score_values)
        
        if course_count > 0:
            average = total_score / course_count
            student_averages[student_name] = round(average, 2)
        else:
            student_averages[student_name] = 0.0

    return student_averages

def identify_high_performers(data, threshold=70):
    """
    Identifies students who scored above the threshold in ALL registered courses.
    
    """
    high_performers = {}

    for student_name, scores in data.items():
        # The 'all()' function is efficient for checking if every score meets the condition.
        all_scores_high = all(score > threshold for score in scores.values())
        
        if all_scores_high:
            high_performers[student_name] = scores

    return high_performers

# --- Part 5.2: Advanced Challenges - Pattern Matching with MATCH CASE ---

def identify_data_type(data_input):
    """
    Uses MATCH CASE to identify the type of input and return a formatted summary.
    ( Identify int, float, list, dict, str)
    """

    match data_input:
        case int():
        
            return f"Data Type: Integer. Value: {data_input}. It is an exact whole number."
        
        case float():
            
            return f"Data Type: Float. Value: {data_input}. It has a fractional component."
        
        case list(items) if len(items) > 0:
        
            return f"Data Type: List. Contains {len(items)} elements. First element: {items[0]}."
            
        case list():
        
            return "Data Type: List. This is an empty list with no elements."

        case dict(items):
        
            return f"Data Type: Dictionary. Contains {len(items)} key-value pairs."

        case str() if len(data_input) < 20:
        
            return f"Data Type: String. Length is {len(data_input)}. Short string: '{data_input}'"

        case str():
        
            return f"Data Type: String. Length is {len(data_input)}. Long string."
            
        case _:
            
            return f"Data Type: Other. Type is {type(data_input).__name__}."