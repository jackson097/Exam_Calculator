from functions import is_valid, calculate_mark_needed

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

	
# Calculate the mark needed
mark_needed = calculate_mark_needed(float(current_mark), float(desired_mark), float(exam_weight)/100)


# Print results
print_statement = "You will need a {:.1f}% on the final exam for a final mark of {:.1f}%. ".format(float(mark_needed), float(desired_mark))

if mark_needed > 100:
    print(print_statement + "You're screwed.")
	
elif mark_needed >= 90 and mark_needed <= 100:
    print(print_statement + "Anything's possible.")
	
elif mark_needed >= 80 and mark_needed < 90:
    print(print_statement + "You can do it!")
	
elif mark_needed >= 70 and mark_needed < 80:
    print(print_statement + "Not too bad.")
	
elif mark_needed >= 60 and mark_needed < 70:
    print(print_statement + "Shouldn't be too hard.")
	
elif mark_needed >= 50 and mark_needed < 60:
    print(print_statement + "Should be a breeze.")
	
elif mark_needed < 50 and mark_needed > 0:
    print(print_statement + "Just show up and you're good.")
	
elif mark_needed <= 0:
	print(print_statement + "Don't even bother...")
	
else:
    print("Error.")
