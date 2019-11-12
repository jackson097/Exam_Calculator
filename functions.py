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
			 desired_mark - the student's desired mark for the course overall (float)
			 exam_weight  - the weight of the exam
"""
def calculate_mark_needed(current_mark, desired_mark, exam_weight):
	current_mark = (current_mark * (1-exam_weight))
	return (desired_mark - current_mark) / exam_weight