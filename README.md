# Part 1: Python Basics & Control Flow

## Assignment Overview
A command-line **Student Grade Tracker** that manages student data, computes results, and provides a summary report — built using core Python concepts including string manipulation, loops, conditionals, and formatted output.

## Concepts Covered
1. **Data Parsing & Cleaning** — Stripping whitespace, type conversion, title casing, name validation
2. **Loops & Conditionals** — Grade assignment with `for` loops, marks-entry system with `while` loop
3. **Class Performance Summary** — Computing averages, pass/fail status, class topper and class average
4. **String Manipulation** — Strip, title case, count, replace, split, and sentence formatting

## File Structure
```
├── part1_grade_tracker.py   # Main Python script with all 4 tasks
└── README.md                # This file
```

## How to Run
```bash
python part1_grade_tracker.py
```

## Requirements
- Python 3.6+
- No external libraries needed

## Execution Output

```
--- Task 1: Data Parsing & Profile Cleaning ---
✓ Valid name: Ayesha Sharma
================================
Student : Ayesha Sharma
Roll No : 101
Marks   : [88, 72, 95, 60, 78]
================================
✓ Valid name: Rohit Verma
================================
Student : Rohit Verma
Roll No : 102
Marks   : [55, 68, 49, 72, 61]
================================
✓ Valid name: Priya Nair
================================
Student : Priya Nair
Roll No : 103
Marks   : [91, 85, 88, 94, 79]
================================
✓ Valid name: Karan Mehta
================================
Student : Karan Mehta
Roll No : 104
Marks   : [40, 55, 38, 62, 50]
================================
✓ Valid name: Sneha Pillai
================================
Student : Sneha Pillai
Roll No : 105
Marks   : [75, 80, 70, 68, 85]
================================
Finding roll 103:
PRIYA NAIR
priya nair

--- Task 2: Marks Analysis Using Loops & Conditionals ---
Grades for Ayesha Sharma
- Math: 88 (A)
- Physics: 72 (B)
- CS: 95 (A+)
- English: 60 (C)
- Chemistry: 78 (B)

Total marks: 393
Average marks: 78.6
Highest scoring subject: CS (95)
Lowest scoring subject: English (60)

--- Enter new subjects ---
Enter subject name (or type 'done' to stop): Math
Enter marks for Math (0-100): 45
Added Math
Enter subject name (or type 'done' to stop): done

Summary:
New subjects added: 1
Updated average across all subjects: 73.0

--- Task 3: Class Performance Summary ---
Name              | Average | Status
----------------------------------------
Ayesha Sharma     | 78.60   | Pass
Rohit Verma       | 61.00   | Pass
Priya Nair        | 87.40   | Pass
Karan Mehta       | 49.00   | Fail
Sneha Pillai      | 75.60   | Pass

Passed: 4
Failed: 1
Class Topper: Priya Nair (87.40)
Class Average: 70.32

--- Task 4: String Manipulation Utility ---
1) python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.
2) Python Is A Versatile Language. It Supports Object Oriented, Functional, And Procedural Programming. Python Is Widely Used In Data Science And Machine Learning.
3) 2
4) Python 🐍 is a versatile language. it supports object oriented, functional, and procedural programming. Python 🐍 is widely used in data science and machine learning.
5) ['python is a versatile language', 'it supports object oriented, functional, and procedural programming', 'python is widely used in data science and machine learning.']
6)
1. python is a versatile language.
2. it supports object oriented, functional, and procedural programming.
3. python is widely used in data science and machine learning.
```