# CW Part-01- Main Version

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 18989164
# Date:17/04/2022

import sys

progress_count, trailer_count, excluded_count, retriever_count = 0, 0, 0, 0                                         #Create variables
print('-'*5,' Welcome ','-'*5)

def main(progress_count, trailer_count, excluded_count, retriever_count):                                           #Create a function called 'main' and passed parameters into function
    try:
        choose = int(input("Enter number '1' For Student login,Enter number '2' For Staff login : "))                #create option to select the staff or student version with integer input
        while True:
            if choose == 1:
                print("Student Version")
                while True:
                    try:
                        credit_pass = int(input("Please enter your credits at pass: "))  # get user input for credit at pass
                        if 0 <= credit_pass <= 120 and credit_pass % 20 == 0:  # check user input for credit at pass is out of range or not
                            credit_differ = int(input("Please enter your credits at differ: "))  # get user input for credit at differ
                            if 0 <= credit_differ <= 120 and credit_differ % 20 == 0:  # check user input for credit at differ is out of range or not
                                credit_fail = int(input("Please enter your credits at fail: "))  # get user input for credit at fail
                                if 0 <= credit_fail <= 120 and credit_fail % 20 == 0:  # check user input for credit at fail is out of range or not
                                    total = credit_pass + credit_differ + credit_fail  # get total value
                                    if total != 120:
                                        print("Total incorrect")  # Check the total correct or not
                                        continue
                                    elif credit_pass == 120:
                                        print("Progress")
                                    elif credit_pass == 100:
                                        print("Progress (module trailer)")  # check user inputs its Total incorrect,Progress,module trailer,module retriever or Exclude
                                    elif 0 <= credit_pass <= 80 and 0 <= credit_differ <= 120 and 0 <= credit_fail <= 60:
                                        print("Do not progress – module retriever")
                                    elif 0 <= credit_pass <= 40 and 0 <= credit_differ <= 40 and 80 <= credit_fail <= 120:
                                        print("Exclude")
                                    sys.exit()
                                else:
                                    print("out of range")
                            else:
                                print("out of range")
                        else:
                            print("Out of range")
                    except ValueError:
                        print("Integer required")
            elif choose == 2:
                print("--Staff Version with Histogram--")
                while True:
                    try:
                        credit_pass = int(input("Enter your total PASS credits : "))
                        if 0 <= credit_pass <= 120 and credit_pass % 20 == 0:
                            credit_differ = int(input("Enter your total DEFER credits : "))
                            if 0 <= credit_differ <= 120 and credit_differ % 20 == 0:
                                credit_fail = int(input("Enter your total FAIL credits : "))
                                if 0 <= credit_fail <= 120 and credit_fail % 20 == 0:
                                    total = credit_pass + credit_differ + credit_fail
                                    if total != 120:
                                        print("Total incorrect")
                                        continue
                                    elif credit_pass == 120:
                                        print("Progress")
                                        progress_count = progress_count + 1
                                    elif credit_pass == 100:
                                        print("Progress (module trailer)")
                                        trailer_count = trailer_count + 1
                                    elif 0 <= credit_pass <= 80 and 0 <= credit_differ <= 120 and 0 <= credit_fail <= 60:
                                        print("Do not progress – module retriever")
                                        retriever_count = retriever_count + 1
                                    elif 0 <= credit_pass <= 40 and 0 <= credit_differ <= 40 and 80 <= credit_fail <= 120:
                                        print("Exclude")
                                        excluded_count = excluded_count + 1
                                    histo(progress_count, trailer_count, excluded_count, retriever_count,choose)  # call histogram function
                                else:
                                    print("out of range")
                            else:
                                print("out of range")
                        else:
                            print("Out of range")
                    except ValueError:
                        print("Integer required")
            else:
                print("Please enter '1' or '2' for version select")
                main(progress_count, trailer_count, excluded_count, retriever_count)           #call main function
    except ValueError:
        print("Integer required")
        main(progress_count, trailer_count, excluded_count, retriever_count)                #call main function

def histo(progress_count, trailer_count, excluded_count, retriever_count,choose):           #Create a function called 'histo' for histogram and passed parameters into function
    while True:
        print("\nWould you like to enter another set of data?")
        choice = input("Enter 'y' for yes or 'q' to quit and view results: ")               #get user choice yes or no
        choice = choice.upper()                                                             #convert user choice answer into capital letters
        if choice == "Y":
            break                                 # if user input 'y' then programe will continue.
        elif choice == "Q":
            print("-"*64)
            print("| Horizontal Histogram   |", '\n')
            print(f"progress  {progress_count} :", progress_count * ' *')
            print(f"trailer   {trailer_count} :", trailer_count * ' *')                      #if user input 'q' then programe will end and print Horizontal Histogram and total out come
            print(f"retriever {retriever_count} :", retriever_count * ' *')
            print(f"excluded  {excluded_count} :", excluded_count * ' *')

            total_count = progress_count + trailer_count + retriever_count + excluded_count
            print("\n")
            print(total_count, 'Outcomes in total.')
            print("-" * 64)
            sys.exit()
        else:
            print("enter a valid value")


main(progress_count, trailer_count, excluded_count, retriever_count)                   #call main function

