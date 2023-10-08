# 1. Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    print(f"Hello_{user_name}!")

user_name = input('What is your name?')

hello_name(user_name)



# 2. Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds(odd):
    while odd != 101:
        print(int(f"{odd}"))
        odd += 2
    else:
        return('nothing')

odd = 1
    
first_odds(odd)



# 3. Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list): 
    print(len(a_list))

a_list =[10, 21, 32, 43, 54]
max_num_in_list(a_list)



# 4. Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):


def is_leap_year(a_year):
    if a_year % 400 == 0:
        print('True')
    elif a_year % 100 == 0:
        print('False')
    elif a_year % 4 ==0:
        print('True')
    else:
        print('False')


a_year = int(input("Is it a leap year?"))

is_leap_year(a_year)



# 5. Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):


# 1st draft
# def is_consecutive(a_list):
#     a_list.append(int(input('Enter numbers and I will tell you if they are consecutive.  Hit enter after every number.  For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.  ')))
#     print(a_list)
#     a_list.append(int(input('I need at least one more number, please... ')))
#     print(a_list)
#     more_nums(more)
    
           
# def more_nums(more):
#     inc = int(0)
    
#     if more == 'y':
#         a_list.append(int(input('What is your number? ')))
#         print(a_list)
#         more_nums(more)
#     if more == 'n':       
#         while a_list[inc + 1] != a_list[inc] + 1:
#             print('False')
#         while a_list[inc + 1] == a_list[inc] + 1:
#             inc += 1
#             more_nums(more)
#     else:
#         print('y or n')
#         more_nums(more)


# a_list = []
# more = input('Do you have another number? ')

# is_consecutive(a_list)
# more_nums(more)



#have input for numbers
#have break
#have computer check if 1st number + 1 = 2nd number
#must repeat until all list numbers are looked at
#display list
#print true or false




# 2nd draft

def is_consecutive(a_list):
    for i in range(len(a_list) - 1):
        print(i, a_list[i])
        if a_list[i] != a_list[i + 1] - 1:
            return False
    return True


print(is_consecutive([2,3,4,5,6,7]))



# I had help from Brandt Carlson with the 2nd draft.  I left 1st draft so you can see my thought process.  I did study the 2nd draft and believe I understand it now.


