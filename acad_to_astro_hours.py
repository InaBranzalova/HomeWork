# Task:
# Write a Python program that calculates the total duration (in astronomical hours) of a Python course consisting of 64 academical hours, including the respective breaks.

# Given:

# 1 astronomical hour = 60 minutes
# 1 academical hour = 40 minutes
# The course is structured in sessions, where:
# Each session consists of 4 academical hours
# Each session includes a 20-minute break


astro_hour_dur = 60
acad_hour_dur = 40
python_course_acad_hours = 64
break_dur = 20
time_of_break = (python_course_acad_hours/4)*break_dur
astro_hour_of_course = ((python_course_acad_hours*acad_hour_dur)+ time_of_break)/astro_hour_dur
print(astro_hour_of_course)