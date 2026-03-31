# Part 1: Python Basics & Control Flow
# Grade Tracker Application

print("--- Task 1: Data Parsing & Profile Cleaning ---")

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

final_data = []

for s in raw_students:
    # fix the name
    n = s["name"].strip().title()
    
    # fix roll to int
    r = int(s["roll"])
    
    # turn marks string into a list of ints , because it is necessary for calculations and conversions
    m_list = []
    for mark in s["marks_str"].split(", "):
        m_list.append(int(mark))
        
    test_name = n.replace(" ", "")
    if test_name.isalpha():
        print("✓ Valid name:", n)
    else:
        print("✗ Invalid name:", n)
        
    final_data.append({"name": n, "roll": r, "marks": m_list})
    
    # print the profile card
    print("================================")
    print(f"Student : {n}")
    print(f"Roll No : {r}")
    print(f"Marks   : {m_list}")
    print("================================")
    print()

print("Finding roll 103:")
for data in final_data:
    if data["roll"] == 103:
        print(data["name"].upper())
        print(data["name"].lower())


print("\n--- Task 2: Marks Analysis Using Loops & Conditionals ---")

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("Grades for", student_name)
for i in range(len(subjects)):
    cur_mark = marks[i]
    grade = ""
    if cur_mark >= 90:
        grade = "A+"
    elif cur_mark >= 80:
        grade = "A"
    elif cur_mark >= 70:
        grade = "B"
    elif cur_mark >= 60:
        grade = "C"
    else:
        grade = "F"
        
    print(f"- {subjects[i]}: {cur_mark} ({grade})")

t_marks = sum(marks)
avg_m = t_marks / len(marks)
highest = max(marks)
lowest = min(marks)

idx_high = marks.index(highest)
idx_low = marks.index(lowest)

print()
print("Total marks:", t_marks)
print("Average marks:", round(avg_m, 2))
print(f"Highest scoring subject: {subjects[idx_high]} ({highest})")
print(f"Lowest scoring subject: {subjects[idx_low]} ({lowest})")
print()

print("--- Enter new subjects ---")
added_count = 0

while True:
    sub = input("Enter subject name (or type 'done' to stop): ").strip()
    if sub.lower() == 'done':
        break
        
    try:
        val = int(input(f"Enter marks for {sub} (0-100): ").strip())
        if 0 <= val <= 100:
            subjects.append(sub)
            marks.append(val)
            added_count += 1
            print("Added", sub)
        else:
            print("Invalid range. Skipping.")
    except:
        print("Not a number. Skipping.")

print("\nSummary:")
print("New subjects added:", added_count)
if len(marks) > 0:
    print("Updated average across all subjects:", round(sum(marks)/len(marks), 2))
else:
    print("Updated average across all subjects: 0")


print("\n--- Task 3: Class Performance Summary ---")

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name              | Average | Status")
print("----------------------------------------")

p_count = 0
f_count = 0
total_class_sum = 0
top_avg = 0
top_name = ""

for student_tuple in class_data:
    nm = student_tuple[0]
    grades = student_tuple[1]
    
    curr_avg = sum(grades) / len(grades)
    total_class_sum += curr_avg
    
    if curr_avg >= 60:
        status = "Pass"
        p_count += 1
    else:
        status = "Fail"
        f_count += 1
        
    if curr_avg > top_avg:
        top_avg = curr_avg
        top_name = nm
        
    # simple formatting manually instead of fancy left/right aligners
    nm_padded = nm + " " * (18 - len(nm))
    avg_str = f"{curr_avg:.2f}"
    avg_padded = avg_str + " " * (7 - len(avg_str))
    
    print(f"{nm_padded}| {avg_padded} | {status}")

class_avg_total = total_class_sum / len(class_data)
print()
print("Passed:", p_count)
print("Failed:", f_count)
print(f"Class Topper: {top_name} ({top_avg:.2f})")
print(f"Class Average: {class_avg_total:.2f}")


print("\n--- Task 4: String Manipulation Utility ---")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# step 1
clean_essay = essay.strip()
print("1)", clean_essay)

# step 2
print("2)", clean_essay.title())

# step 3
c = clean_essay.count("python")
print("3)", c)

# step 4
rep_essay = clean_essay.replace("python", "Python 🐍")
print("4)", rep_essay)

# step 5
pieces = clean_essay.split(". ")
print("5)", pieces)

# step 6
print("6)")
for idx in range(len(pieces)):
    snt = pieces[idx]
    if not snt.endswith("."):
        snt += "."
    print(f"{idx+1}. {snt}")
