# This is a Python Dictionary that contains all of the students in Kenny's class as well as their grades.
student_grades = {"Jeremy" : 87, "Kyla" : 82, "Ayesha" : 90, "Aleida" : 94, "Todd" : 79, "Maxwell" : 98, "Yolonda" : 81, "Kiyoko" : 71, "Dagmar" : 73, "Laura" : 91, "Shimeah" : 81, "Songqiao" : 92, "Frankie" : 87, "Natalia" : 95, "Gonzalo" : 82, "Pavel" : 78}

# This is a function that determines the student with the highest grade given a dictionary
def highest_grade(grades):
	top_of_class = list(grades.keys())[0]
	for student_a in grades:
		for student_b in grades:
			if (grades[student_a] > grades[student_b]) and (grades[student_a] > grades[top_of_class]):
				top_of_class = student_a
			elif (grades[student_b] > grades[student_a]) and (grades[student_b] > grades[top_of_class]):
				top_of_class = student_b
	return top_of_class

# This is a function that determines the student with the lowest grade given a dictionary
def lowest_grade(grades):
	bottom_of_class = list(grades.keys())[0]
	for student_a in grades:
		for student_b in grades:
			if (grades[student_a] < grades[student_b]) and (grades[student_a] < grades[bottom_of_class]):
				bottom_of_class = student_a
			elif (grades[student_b] < grades[student_a]) and (grades[student_b] < grades[bottom_of_class]):
				bottom_of_class = student_b
	return bottom_of_class

# This is Kenny's Algorithm! It sorts the students into pairs based on their grades.
def kennys_algorithm(grade_dict):
	student_pairs = []
	while len(grade_dict) > 0:
		student_pairs.append([highest_grade(grade_dict), lowest_grade(grade_dict)])
		grade_dict.pop(highest_grade(grade_dict))
		grade_dict.pop(lowest_grade(grade_dict))
	print(student_pairs)
  
# Paste the code below!
kennys_algorithm(student_grades)
