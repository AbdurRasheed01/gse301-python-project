# 🎓 Student Academic Performance Analysis System

## Project Title
**Student Academic Performance Analysis System (GSE301 Project)**

## Project Overview
This console-based system was developed for the GSE301 Data Science: Python Fundamentals course. Its purpose is to demonstrate proficiency in core Python concepts—including data structures, conditional logic, error handling, and modular programming by managing, processing, and analyzing mock academic data.

The project is split into three highly readable modules:
1.  **`data_manager.py`**: Manages the storage of all student profiles.
2.  **`core_logic.py`**: Houses all the functional logic (grading, validation, analysis).
3.  **`main_system.py`**: The main execution file containing the interactive menu and running all demonstrations.

## 🛠️ How to Run the System

1.  **Save Files:** Ensure you have the three required files (`data_manager.py`, `core_logic.py`, `main_system.py`) in the same directory.
2.  **Execute:** Run the main file from your terminal:
    ```bash
    python main_system.py
    ```
    The system will first run all required demonstrations (Slicing, Set Operations, Grading, and Advanced Challenges) before starting the interactive menu.

## Key Python Concepts Demonstrated

The project successfully implements all required concepts:

| Concept/Task | File | Implementation Details |
| :--- | :--- | :--- |
| **Data Structures** (List, Dict, Set, Tuple) | `data_manager.py` | Storing student profiles (List of Dictionaries), unique courses (Set), and fixed department info (Tuple). |
| **IF/ELIF/ELSE** | `core_logic.py` | Used in the `score_to_grade` function for assigning letter grades based on score range. |
| **MATCH CASE** | `core_logic.py` | Used for printing structured feedback based on the letter grade, and in **Part 5** for advanced structural pattern matching on data types. |
| **Type Casting (`int()`, `float()`)** | `core_logic.py` | Used in `get_validated_input` to convert user-input strings (age, CGPA) into numeric types. |
| **Try/Except** | `core_logic.py` | Used to handle `ValueError` when converting non-numeric user input (Task 2.2). |
| **List Slicing** | `core_logic.py` | Demonstrated extracting the top 3 scores (`[:3]`), the last 5 scores (`[-5:]`), and every other score (`[::2]`). |
| **Set Operations** | `core_logic.py` | Demonstrated `intersection()`, `union()`, and `difference()` to analyze student group memberships. |
| **Logical Operators (`and`, `or`)** | `core_logic.py` | Used in `check_graduation_eligibility` to enforce criteria (`CGPA >= 2.5` **and** `outstanding courses == 0` **and** `is_active`). |

## Advanced Challenges (Part 5)

| Task | File | Implementation Details |
| :--- | :--- | :--- |
| **Nested Data Processing** | `core_logic.py` | Iterating through a dictionary of dictionaries (`nested_scores_data`) to calculate individual student averages and identify high performers. |
| **Structural Pattern Matching** | `core_logic.py` | The `identify_data_type` function uses `MATCH CASE` to match and summarize `int()`, `float()`, `list()`, `dict()`, and `str()` patterns. |

## My Biggest Challenge 

My biggest challenge was implementing the **Type Conversion and Validation** within the interactive menu loop. Specifically, ensuring the `Try/Except` block successfully catches the `ValueError` if a user enters text instead of a number for age or CGPA, and then correctly prompting the user to re-enter the data without crashing the system or exiting the input loop. The solution involved using a `while` loop combined with `try/except` for robust input handling.

---

## Submission Details

* **Student Name:** [Fashola Abdur Rasheed]
* **Matric Number:** [24/56EG152]
* **GitHub Repository:** [https://github.com/AbdurRasheed01]
* **Social Media Post Link:** [https://www.linkedin.com/in/fashola-abdulrasheed]