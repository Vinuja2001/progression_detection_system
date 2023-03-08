# CW Part-04 Text file

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 18989164
# Date:17/04/2022

import sys

progress_count, trailer_count, excluded_count, retriever_count = 0, 0, 0, 0     #Create variables

list_of_progress=[]
list_of_trailer=[]
list_of_excluded=[]              #Create lists for progress,retriever,trailer and exclude
list_of_retriever=[]

print('-'*5,' Welcome ','-'*5)

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
                        list_of_progress.append([credit_pass,credit_differ,credit_fail])
                    elif credit_pass == 100:
                        print("Progress (module trailer)")  # check user inputs its
                        trailer_count = trailer_count + 1  # Total incorrect,Progress,module trailer,
                        list_of_trailer.append([credit_pass,credit_differ,credit_fail])
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
                        choice = input("Enter 'y' for yes or 'q' to quit and view results: ")  # get user choice yes or no
                        choice = choice.upper()  # convert user choice answer into simple letters
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
                            print('| Vertical Histogram    ','\n')
                            print(" Progress ", progress_count, "| Trailer ", trailer_count, "| Retriever ",retriever_count, "| Exclude ", excluded_count)
                            # if user input 'q' then programe will end and print Vertical Histogram and total out come
                            total_count = progress_count + trailer_count + retriever_count + excluded_count

                            for i in range(max(progress_count, trailer_count, retriever_count,excluded_count)):
                                print("  {}           {}            {}          {}".format(
                                    '  *' if i < progress_count else '   ',
                                    '  *' if i < trailer_count else '   ',
                                    '  *' if i < retriever_count else '   ',
                                    '  *' if i < excluded_count else '   '))
                            print("-" * 64)
                            print(total_count, "outcome in total", '\n')
                            file = open("outcomes.txt", "w")
                            for progress in (list_of_progress):
                                file.write("Progress - ")
                                file.write(str(progress).strip('[]'))  #remove extra brackets - https://stackoverflow.com/questions/29459008/how-to-remove-brackets-from-python-string
                                file.write('\n')
                            for trailer in (list_of_trailer):
                                file.write("Progress (module trailer) - ")
                                file.write(str(trailer).strip('[]'))
                                file.write('\n')
                            for retriever in (list_of_retriever):
                                file.write("Module retriever - ")
                                file.write(str(retriever).strip('[]'))
                                file.write('\n')
                            for exclude in (list_of_excluded):
                                file.write("Exclude - ")
                                file.write(str(exclude).strip('[]'))
                                file.write('\n')
                            file = open("outcomes.txt", "r")
                            print(str(file.read()).strip('[]'))
                            file.close()
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


