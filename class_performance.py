def average(marks):
    return sum(marks) / len(marks)
def performance(students):
    averages = {}
    for name, marks in students.items():
        averages[name] = round(average(marks), 2)
    top = max(averages, key=averages.get)
    return averages, top

students = {}
n = int(input("Enter number of students: "))
for i in range(1,n+1):
    name = input(f"\nEnter name of student {i}: ")
    m = int(input(f"Enter number of subjects for {name}: "))
    marks = []
    for j in range(1,m+1):
        mark = float(input(f"Enter mark {j} for {name}: "))
        marks.append(mark)
    students[name] = marks
averages, top = performance(students)
print("\nAverage Marks:", averages)
print("Top Performer:", top)