
import os.path
Directory = 'Users/diego/'
#display menu with options available
def main():
    display_menu()
    choice = getChoice('What would you like to do today? ')

    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    elif choice == 3:
        choice3()
    elif choice == 4:
        choice4()
    elif choice == 5:
        choice5()

   
#error prevention
def getChoice(outputstring):
    x = input(outputstring)
    if not x.isnumeric():
        print('Invalid Selection.')
        return -1
    else:
        return int(x)    

#showing menu and asking which option they would like to proceed
def display_menu():
    print('----- BUDGET BREAKDOWN CALCULATOR ----- ')
    print('1) Create User')
    print('2) Add User’s Expenses')
    print('3) Generate Report')
    print('4) Print Terms of Use')
    print('5) End Program')
    print()
    


#creating user if they do not already exist on 'userinfo.txt'
def choice1():
    first_name =input('Please enter your first name: ')
    last_name = input('Please enter your last name: ')
    r_num =input("Please enter your R#: ")
    total_yearly_revenue =input('Please enter your total yearly revenue: ')
    with open("userinfo.txt","a") as f:
        f.write(first_name +","+ last_name +","+ r_num +","+total_yearly_revenue + "\n")
    
    display_menu()

#adds the users list of expenses
def choice2():
   r_num = input("Please enter your R#: ")
   num_of_expenses = int(input('Enter the number of expenses you will be adding:' ))
   for i in range(num_of_expenses):
       r_num = input('Input your R number once again: ')
       expense = input('Enter the expense name: ')
       cost = float(input('Enter the cost for the previously typed expense: '))
       type = input('Enter the classification of the expense: ')

       with open("userinfo.txt", "a") as expenses:
       	expenses.write(r_num + "                " + expense + "                " + str(cost) + "                " + type)
       	expenses.write("\n")
       	print('Data inserted successfully.')
           

#generates a report of the users details

#function to add the user's expenses
def choice3():
    r_num = input("Please enter your R#")
    reportForm = input('Enter "1" to display report on console, enter "2" to write report to file.')
    print(r_num)
    print(nameVariable)
    print(revenue)
    revenue = total_yearly_revenue =input('Please enter your total yearly revenue: ')
    print(expenses)
    expenses = num_of_expenses = int(input('Enter the number of expenses you will be adding:' ))    
    print(preferred_expenses)
    preferred_expenses = expenses * ('{:.2f}'.format(.5))
    print("Statement here")

    if reportForm == 1:
        choice3()
    #elif reportForm == 2

                    
    
              
# Prompt the user to enter any additional monthly expenses


#print the Print Terms of Use
def choice4():
    DIRECTORY = '/Users/diego/'

    with open(DIRECTORY + 'COD.txt', 'r') as f:
        for lines in f:
            linesplit = lines.rstrip().split('.')
            print(linesplit)
 
    terms = input()
    if terms == ('Y'):
        print('******************************')
        print('Thank you for your soul!')
        print('******************************')
        display_menu()
    else:
        print('Goodbye!')
#ends the program    
def choice5():
    print('Goodbye! :)')
    
def is_valid_file(f):
    if os.path.exists(Directory + f):
        return True
    return False

#running the choice selected

main()

    
