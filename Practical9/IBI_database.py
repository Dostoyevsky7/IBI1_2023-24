# create a class to store students' information
class students (object):
    """
    Includes students information about name, major, sore for code portfolio, 
    score for group project, and exam score
    """
    #the class includes 5 elements
    def __init__(self, name, major, code_score, group_score, exam_score):
        self.name = name
        self.major = major
        self.code_score = code_score
        self.group_score = group_score
        self.exam_score = exam_score
    #the class includes a function to print out all the elements in one line
    def print_info(self):
        print(f"Name: {self.name}, Major: {self.major}, sore for code portfolio: {self.code_score}, score for group project: {self.group_score}, exam score: {self.exam_score}")
#example: student A majors in BMI and has straight As
student1 = students('A', 'BMI', 100, 100, 100)
student1.print_info() #use the function to print out A's information