# CW Part-03 Lists

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 18989164
# Date:17/04/2022

import sys

progress_count, trailer_count, excluded_count, retriever_count = 0, 0, 0, 0                              #Create variables

list_of_progress=[]
list_of_trailer=[]                     #Create lists for progress,retriever,trailer and exclude
list_of_excluded=[]
list_of_retriever=[]

print('-'*5,' Staff Version with Histogram ','-'*5)

while True:
    try:
        credit_pass = int(input("please enter your credits at pass: "))  # get user input for credit at pass
        if 0 <= credit_pass <= 120 and credit_pass % 20 == 0:  # check user input for credit at pass is out of range or not
            credit_differ = int(input("please enter your credits at differ: "))  # get user input for credit at differ
            if 0 <= credit_differ <= 120 and credit_differ % 20 == 0:  # check user input for credit at differ is out of range or not
                credit_fail = int(input("please enter your credits at fail: "))  # get user input for credit at fail
                if 0 <= credit_fail <= 120 and credit_fail % 20 == 0:  # check user input for credit at fail is out of range or not
                    total = credit_pass + credit_differ + credit_fail  # get total value
                    if total != 120:
                        print("Total incorrect")
                        continue
                    elif credit_pass == 120:
                        print("Progress")
                        progress_count = progress_count + 1
                        list_of_progress.append([credit_pass,credit_differ,credit_fail])# check user inputs its Total incorrect,Progress,module trailer ,module retriever or Exclude and count inputs
                    elif credit_pass == 100:
                        print("Progress (module trailer)")
                        trailer_count = trailer_count + 1
                        list_of_trailer.append([credit_pass,credit_differ,credit_fail])  #append user inputs for the created lists
                    elif 0 <= credit_pass <= 80 and 0 <= credit_differ <= 120 and 0 <= credit_fail <= 60:
                        print("Do not progress – module retriever")
                        retriever_count = retriever_count + 1
                        list_of_retriever.append([credit_pass,credit_differ,credit_fail])
                    elif 0 <= credit_pass <= 40 and 0 <= credit_differ <= 40 and 80 <= credit_fail <= 120:
                        print("Exclude")
                        excluded_count = excluded_count + 1
                        list_of_excluded.append([credit_pass,credit_differ,credit_fail])
                    while True:
                        print("\nWould you like to enter another set of data?")
                        choice = input(
                            "Enter 'y' for yes or 'q' to quit and view results: ")  # get user choice yes or no
                        choice = choice.upper()  # convert user choice answer into capital letters
                        if choice == "Y":
                            break  # if user input 'y' then programe will continue.
                        elif choice == "Q":
                            print("-" * 64)
                            print("| Horizontal Histogram   |", '\n')
                            print(f"progress  {progress_count} :", progress_count * ' *')
                            print(f"trailer   {trailer_count} :",trailer_count * ' *')  # if user input 'q' then programe will end and print Horizontal Histogram and total out come
                            print(f"retriever {retriever_count} :", retriever_count * ' *')
                            print(f"excluded  {excluded_count} :", excluded_count * ' *')
                            print("-" * 64)
                            print('| Vertical Histogram   |\n')
                            print(" Progress ", progress_count, "| Trailer ", trailer_count, "| Retriever ", retriever_count , "| Exclude ", excluded_count) # if user input 'q' then programe will end and print Vertical Histogram and total out come
                            total_count = progress_count + trailer_count + retriever_count + excluded_count

                            for i in range(max(progress_count, trailer_count, retriever_count, excluded_count)):
                                print("  {}           {}            {}          {}".format(
                                    '  *' if i < progress_count else '   ',
                                    '  *' if i < trailer_count else '   ',
                                    '  *' if i < retriever_count else '   ',
                                    '  *' if i < excluded_count else '   '))

                            print('\n',total_count, "outcome in total")
                            print("-" * 64)
                            for progress in (list_of_progress):
                                print("Progress  - ", end='')
                                print(str(progress).strip('[]'))
                            for trailer in (list_of_trailer):
                                print("Progress (module trailer) - ", end='')
                                print(str(trailer).strip('[]'))
                            for retriever in (list_of_retriever):
                                print("Module retriever - ", end='')  # get data from those lists and print here .
                                print(str(retriever).strip('[]')) #.strip used for remove '[]' from the list
                            for exclude in (list_of_excluded):
                                print("Exclude   - ", end='')  # https://www.kite.com/python/answers/how-to-print-a-list-without-brackets-in-python#:~:text=Use%20*%20to%20print%20a%20list,set%20sep%20to%20%22%2C%20%22%20.
                                print(str(exclude).strip('[]'))
                            print('-' * 64)
                            sys.exit()
                        else:
                            print("enter a valid value")
                else:
                    print("out of range")
            else:
                print("out of range")
        else:
            print("Out of range")
    except ValueError:
        print("Integer required")