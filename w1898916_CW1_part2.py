# CW Part-02 Vertical Histogram

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 18989164
# Date:17/04/2022

''''In part 2 we need to create vertical histogram with the multiple outcomes,then student inputs are no need for that part.'''
import sys
progress_count, trailer_count, excluded_count, retriever_count = 0, 0, 0, 0     #Create variables

print('-'*5,' Welcome ','-'*5)
print('-'*5," Staff Version with Histogram",'-'*5)

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
                        progress_count = progress_count + 1  # get count
                    elif credit_pass == 100:
                        print("Progress (module trailer)")
                        trailer_count = trailer_count + 1  # check user inputs its Total incorrect,Progress,module trailer,module retriever or Exclude
                    elif 0 <= credit_pass <= 80 and 0 <= credit_differ <= 120 and 0 <= credit_fail <= 60:  # and count inputs
                        print("Do not progress – module retriever")
                        retriever_count = retriever_count + 1
                    elif 0 <= credit_pass <= 40 and 0 <= credit_differ <= 40 and 80 <= credit_fail <= 120:
                        print("Exclude")
                        excluded_count = excluded_count + 1
                    while True:
                        print("\nWould you like to enter another set of data?")
                        choice = input("Enter 'y' for yes or 'q' to quit and view results: ")  # get user choice yes or no
                        choice = choice.upper()  # convert user choice answer into capital letters
                        if choice == "Y":
                            break  # if user input 'y' then programe will continue.
                        elif choice == "Q":
                            print("-" * 64)
                            print('| Vertical Histogram |', '\n')
                            print(" Progress ", progress_count, "| Trailer ", trailer_count, "| Retriever ",retriever_count, "| Exclude ", excluded_count)# if user input 'q' then programe will end and print Vertical Histogram and total out come
                            total_count = progress_count + trailer_count + retriever_count + excluded_count

                            for i in range(max(progress_count, trailer_count, retriever_count, excluded_count)):
                                print("  {}           {}            {}          {}".format(
                                    '  *' if i < progress_count else '   ',
                                    '  *' if i < trailer_count else '   ',
                                    '  *' if i < retriever_count else '   ',
                                    '  *' if i < excluded_count else '   '))  # vertical histogram - #https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
                            print(total_count, "outcome in total")
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