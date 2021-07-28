"""Write a program that calculates your final percentage in CSSE1001.

Your final percentage is based on your results in MyPyTutor, 
the three assignments and the final exam.

Challenge 1: Output your grade based on your final percentage
Challenge 2: Output your grade based on the course rules
             See: https://course-profiles.uq.edu.au/student_section_loader/section_5/109483
"""


#Challenge 1: Based on final percentage
def challenge1(mpt, a0, a1, a2, a3, exam):
    lst = [mpt, a0, a1, a2, a3, exam]
    final_perc = sum(lst)
    print("Your final grade is:", final_perc)

    if final_perc >= 85:
        print("Your final GPA is 7")
    elif 75 <= final_perc < 85:
        print("Your final GPA is 6")
    elif 65 <= final_perc < 75:
        print("Your final GPA is 5")
    elif 50 <= final_perc < 65:
        print("Your final GPA is 4")
    elif 45 <= final_perc < 50:
        print("Your final GPA is 3")
    elif 20 <= final_perc < 44:
        print("Your final GPA is 2")
    elif 0 <= final_perc < 20:
        print("Your final GPA is 1")
    return

#Challenge 2: Based on ECP
def challenge2(mpt, a0, a1, a2, a3, exam):
    final_perc = a0*0.01+ a1 * 0.1 + a2 * 0.15 + a3 * 0.2 + exam * 0.42 + mpt * 0.12
    print("Your final grade is:", final_perc*100)

    if (final_perc >= 0.85) and (exam >= 0.80) and (a3 >= 0.80) :
        print("Your final GPA is 7")
    elif (final_perc >= 0.75) and (exam >= 0.70):
        print("Your final GPA is 6")
    elif (final_perc >= 0.65) and (exam >= 0.60):
        print("Your final GPA is 5")
    elif (final_perc >= 0.50) and (exam >= 0.45):
        print("Your final GPA is 4")
    elif (final_perc >=0.45) and (exam>=0.40):
        print("Your final GPA is 3")
    elif final_exam >= 0.20:
        print("Your final GPA is 2")
    else:
        print("Your final GPA is 1")
    return


