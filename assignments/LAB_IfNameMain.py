# Author: mdavis2@scu.edu
# Date: 2020-04-20
# Context: SCU OMIS 30 Spring 2020 - LAB-IfNameMain
# Collaborators: None

# Weights of each of the individual grades
participation_weight = 0.10
challenge_activities_weight = 0.10
zylabs_weight = 0.15
homeworks_weight = 0.10
pre_read_quizzes_weight = 0.05
midterm_weight = 0.20
final_project_weight = 0.30


# Create the grade dictionary to pass to the other program
my_grade_dict = dict()

my_grade_dict['student'] = 'mdavis2@scu.edu'

my_grade_dict['grade_components'] = dict()
my_grade_dict['grade_components']['participation'] = 80
my_grade_dict['grade_components']['challenge_activities'] = 85
my_grade_dict['grade_components']['zylabs'] = 90
my_grade_dict['grade_components']['homeworks'] = 95
my_grade_dict['grade_components']['pre_read_quizzes'] = 75
my_grade_dict['grade_components']['midterm'] = 97
my_grade_dict['grade_components']['final_project'] = 100

my_grade_dict['calculated_course_grade'] = ( (my_grade_dict['grade_components']['participation'] * participation_weight) + (my_grade_dict['grade_components']['challenge_activities'] * challenge_activities_weight) + (my_grade_dict['grade_components']['zylabs'] * zylabs_weight) + (my_grade_dict['grade_components']['homeworks'] * homeworks_weight) + (my_grade_dict['grade_components']['pre_read_quizzes'] * pre_read_quizzes_weight) + (my_grade_dict['grade_components']['midterm'] * midterm_weight) + (my_grade_dict['grade_components']['final_project'] * final_project_weight) )

'''
This is an example of the docstring-style multi-line comment.
'''

'''
Before adding any code - run this file, see what happens.  What do you think should happen?
Then, create a new python file in the same folder.  Call it "LAB_IfNameMain_Testing.py".
In that new file: paste this code: 
    
from LAB_IfNameMain import my_grade_dict as student_1_grade_dict
print(student_1_grade_dict)

Then change the grades, and re-run your new file "LAB-IfNameMain_Testing.py".  See that your final grade changes.
Now, delete the "print(student_1_grade_dict)" line.  See that nothing prints now!

This is how someone who would be importing your code would work.
For example: I'm going to download all 30 submissions.  I'm going to run

from student1 import my_grade_dict as student_1_grade_dict
from student2 import my_grade_dict as student_2_grade_dict
...

Then, in order to calculate the class average, I'll run: (student_1_grade_dict['calculated_course_grade'] + student_2_grade_dict['calculated_course_grade'] + ... ) / 30

'''

# Below, add your code for the lab.