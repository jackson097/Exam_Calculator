from functions import is_valid, calculate_mark_needed, print_results

# User Inputs
current_mark = raw_input("Enter current mark (%): ")
while is_valid(current_mark) == False:
    current_mark = raw_input("Number not valid.\nEnter current mark (%):")

desired_mark = raw_input("Enter desired mark (%):")
while is_valid(desired_mark) == False:
    desired_mark = raw_input("Number not valid.\nEnter desired mark (%):")

exam_weight = raw_input("Enter exam weight (%):")
while is_valid(exam_weight) == False or exam_weight == '0':
    exam_weight = raw_input("Number not valid.\nEnter exam weight (%):")

# Convert values to floats now that they have been validated
current_mark = float(current_mark)
desired_mark = float(desired_mark)
exam_weight = float(exam_weight)	

# Calculate the mark needed
mark_needed = calculate_mark_needed(current_mark, desired_mark, exam_weight/100)

# Print results
print_results(mark_needed, desired_mark)