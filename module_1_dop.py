grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Variant 1
dict_ = {}
for grade in grades:
    dict_.update({sorted(students)[grades.index(grade)]: sum(grade)/len(grade)})
print(dict_)

# Variant 2
average_grades = {}
for grade, name in zip(grades, sorted(students)):
    average_grades.update({str(name): sum(grade)/len(grade)})
print(average_grades)
