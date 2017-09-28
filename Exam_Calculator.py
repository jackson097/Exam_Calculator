# Inputs
current_mark = float(input("Enter current mark (%):"))
while current_mark < 0:
    print("Error. Please enter a positive number.")
    current_mark = float(input("Enter current mark (%):"))

desired_mark = float(input("Enter desired mark (%):"))
while desired_mark < 0:
    print("Error. Please enter a positive number.")
    desired_mark = float(input("Enter desired mark (%):"))

exam_weight = float(input("Enter exam weight (%):"))
while exam_weight < 0:
    print("Error. Please enter a positive number.")
    exam_weight = float(input("Enter exam weight (%):"))

# Valid number check
if current_mark < 0 or current_mark > 100:
    print("Error. Not a valid value.")
elif exam_weight < 0 or exam_weight > 100:
    print("Error. Not a valid value.")
elif desired_mark < 0 or desired_mark > 100:
    print("Error. Not a valid value.")

# Calculations
exam_weight = exam_weight / 100
course_work_weight = 1 - exam_weight
current_mark = (current_mark * course_work_weight)
mark_needed = desired_mark - current_mark
mark_needed = mark_needed / exam_weight

# Print Statements
if mark_needed > 100:
    print("You will need a {:.1f}% on the final exam for a final mark of {:.1f}%. You're screwed.".format(
        mark_needed, desired_mark))
elif mark_needed >= 90 and mark_needed < 100:
    print("You will need a {:.1f}% on the final exam for a final mark of {:.1f}%. Anything's possible.".format(
        mark_needed, desired_mark))
elif mark_needed >= 80 and mark_needed < 90:
    print("You will need a {:.1f}% on the final exam for a final mark of {:.1f}%. You can do it!".format(
        mark_needed, desired_mark))
elif mark_needed >= 70 and mark_needed < 80:
    print("You will need a {:.1f}% on the final exam for a final mark of {:.1f}%. Not too bad.".format(
        mark_needed, desired_mark))
elif mark_needed >= 60 and mark_needed < 70:
    print("You will need a {:.1f}% on the final exam for a final mark of {:.1f}%. Shouldn't be too hard.".format(
        mark_needed, desired_mark))
elif mark_needed >= 50 and mark_needed < 60:
    print("You will need a {:.1f}% on the final exam for a final mark of {:.1f}%. Should be a breeze.".format(
        mark_needed, desired_mark))
elif mark_needed < 50:
    print("You will need a {:.1f}% on the final exam for a final mark of {:.1f}%. Just show up and you're good.".format(
        mark_needed, desired_mark))
else:
    print("Error.")
