import os
import json

os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("================================")


student_record = {}

while True:
    print("SELECT FROM THE FOLLOWING OPTIONS")
    print("A - ADD STUDENT RECORD")
    print("B - PRINT ALL STUDENT RECORD")
    print("C - SEARCH STUDENT RECORD")
    print("D - DELETE STUDENT RECORD")
    print("E - EDIT STUDENT RECORD")
    print("F - EXPORT STUDENT RECORD")
    print("G - IMPORT STUDENT RECORD")
    print("X - EXIT SYSTEM")

    choice = input("SELECT FROM THE OPTIONS ABOVE --->").lower()

    if choice == 'a':
        os.system('cls')
        print("\nADD STUDENT RECORD ")
        
        id_no = input("Please input Student ID number ---> ")

        first_name = input("Please input Student First Name ---> ")
        second_name = input("Please input Student Second Name ---> ")
        age = eval(input("Please input Student age ---> "))
        course = input("Please input Student Course ---> ")
        section = input("Please input Student Section ---> ")

        student_record[id_no] = [ first_name, second_name, age, course, section]
        print("DATA SAVED SUCCESSFULLY")


        continue
    elif choice == 'b':
        os.system('cls')
        print("PRINTING STUDENT RECORD")
        #print(student_record) simple approach

        for i, j in student_record.items(): #key _ values
            print(f"STUDENT ID - {i}, INFORMATION - {j}")

        else:
            print("NO RECORD FOUND")
            break
        continue
    elif choice == 'c':
        os.system('cls')

        print("SEARCH STUDENT RECORD")

        search_id = input("input student ID for search ---> ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print(" ===========================")
                print(f"\n\nRECORD FOUND FOR ID {search_id}")
                #to print the record for the searched ID
                for i in student_record[search_id]:
                    print(f" --- {i}")
                print(" ========================")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'd':
        os.system('cls')

        print("SEARCH STUDENT RECORD")

        search_id = input("input student ID for search ---> ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print(" ===========================")
                print(f"\n\nRECORD FOUND FOR ID {search_id}")
                #to print the record for the searched ID
                for i in student_record[search_id]:
                    print(f" --- {i}")
                print(" ========================")

                student_record.pop(search_id)
                print("\nRECORD DELETED")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'e':
        os.system('cls')

        print("EDIT/MODIFY STUDENT RECORD")

        search_id = input("input student ID for search ---> ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print(" ===========================")
                print(f"\n\nRECORD FOUND FOR ID {search_id}")
                #to print the record for the searched ID
                for i in student_record[search_id]:
                    print(f" --- {i}")
                print(" ========================")
                #new sets of value for the searched ID
                first_name = input("Please input Student First Name ---> ").upper()
                second_name = input("Please input Student Second Name ---> ").upper()
                age = eval(input("Please input Student age ---> "))
                course = input("Please input Student Course ---> ").upper()
                section = input("Please input Student Section ---> ").upper()

                student_record[search_id][0] = first_name
                student_record[search_id][1] = second_name
                student_record[search_id][2] = age
                student_record[search_id][3] = course
                student_record[search_id][4] = section

                print("DATA UPDATED")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'f':
        os.system('cls')
        print("EXPORT STUDENT DATA")
        #Json JavaScript Object Notation

        with open('student_record.json', 'w') as new_file:
            json.dump(student_record,new_file, indent=4 )
        continue
    elif choice == 'g':
        os.system('cls')
        print("IMPORT STUDENT DATA")
        #Json JavaScript Object Notation

        with open('student_record.json', 'r') as new_file:
           imported_student = json.load(new_file)

        student_record = imported_student
        print("\n\nDATA IMPORTED TO JSON")
        continue
    elif choice == 'x':
        print("SYSTEM EXIT")
        break
    else:
        print("INVALID CHOICE, REENTER YOUR CHOICE")
        continue
