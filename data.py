students = [
    {"name": "Kashif", "Roll.no.": 101},
    {"name": "Sami", "Roll.no.": 102},
    {"name": "Irfan", "Roll.no.": 103},
    {"name": "Shahbaz", "Roll.no.": 104},
    {"name": "Rayan", "Roll.no.": 105}]
    return False


# MAIN LOOP (SYSTEM NEVER STOPS)
while True:

    valid_data = check_student()

    if valid_data == True:

        add_nums = []
        subjects = int(input("How many subject marks you want to add: "))

        for i in range(subjects):
            numbers = int(input("Enter your marks: "))
            add_nums.append(numbers)

        obtained_marks = sum(add_nums)
        print("Total Obtained Marks =", obtained_marks)

        print("\nDo you want Percentage or Grade? (yes/no)")
        ans = input("Enter your choice: ")

        if ans == "yes":
            total_marks = int(input("Enter total marks: "))
            percentage = (obtained_marks / total_marks) * 100
            print("Percentage:", percentage)

            if percentage >= 90:
                print("Grade: A+")
            elif percentage >= 80:
                print("Grade: A")
            elif percentage >= 70:
                print("Grade: B")
            elif percentage >= 60:
                print("Grade: C")
            elif percentage >= 50:
                print("Grade: D")
            else:
                print("Failed")

        elif ans == "no":
            print("OK 👍 Skipping result")

    # CONTINUE SYSTEM
    again = input("\nDo you want to check another student? (yes/no): ")

    if again != "yes":
        print("System closed ")
        break




    
          
   





    
          
   




