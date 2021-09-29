# author : LM (AMDG) 09/29/2021
number_points = int(input("Please enter the number of points. "))
if number_points >= 15:
    print("They have one a gold medal!!!")
else:
    if number_points >= 12:
        print( "They won a silver medal")
    else: 
        if number_points < 9:
            print("No medals won.")
        else:
            print("They won a bronze medal.")