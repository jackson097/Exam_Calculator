"""
 Determines if the number provided is a valid float
 Parameters: number - the value entered by the user
"""
def is_valid(number):
	# Check if the number is a digit
	if number.isdigit() == False:
		return False
	if float(number) > 100 or float(number) < 0:
		return False
	return True

	
"""
 Calculate the mark needed on final exam
 Parameters: current_mark - the student's current mark (float)
			 desired_mark - the overall course mark desired by the student (float)
			 exam_weight  - the weight of the exam
"""
def calculate_mark_needed(current_mark, desired_mark, exam_weight):
	current_mark = (current_mark * (1-exam_weight))
	return (desired_mark - current_mark) / exam_weight
	
	
"""
  Print human readable results from the calculation
  Parameters: mark_needed  - the mark needed on exam to achieve desired mark
			  desired_mark - the overall course mark desired by the student
"""
def print_results(mark_needed, desired_mark):
	print_statement = "\nYou will need a {:.1f}% on the final exam to achieve a final mark of {:.1f}%. ".format(float(mark_needed), float(desired_mark))

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
