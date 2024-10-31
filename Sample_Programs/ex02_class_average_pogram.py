# ex03_class_averge_pogram
"""Writing an class average program"""
import random
#Initial Phase
total = 0
grade_counter = 0
mark_sheet=[]
for i in range(0,11):
   i=random.randint(78,101)
   mark_sheet.append(i)
print(mark_sheet)

for grade in mark_sheet:
    total += grade
    grade_counter += 1

average = total / grade_counter
print(f"The Class average is {int(average)}")