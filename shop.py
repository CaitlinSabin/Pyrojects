print("Letter Grade Converter")
print("-----------------------------")
while True:
    grade = int(input("Enter your grade (0-100): "))
    
    if grade >= 88:
        letterGrade = "A"
    elif grade >= 80:
        letterGrade = "B"
    elif grade >= 67:
        letterGrade = "C"
    elif grade >= 60:
        letterGrade = "D"
    else:
        letterGrade = "F"
    
    print("Your letter grade is" ,letterGrade+".")
    
    continueInput = input("Do you want to continue (y/n)? ")
    if continueInput.lower() != "y":
        print("GET OUT!!!!!!")
        break
