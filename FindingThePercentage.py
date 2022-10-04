

student_marks = {}
student_marks["Krishna"] = [67, 68, 69]
student_marks["Arjun"] = [70, 98, 63]
student_marks["Malika"] = [52, 56, 60]


l = student_marks["Arjun"]
f = '{0:.2f}'.format(sum(l)/len(l))
print(f)
