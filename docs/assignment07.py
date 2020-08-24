# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# Zshen 08/23/2020 add pickle demo and error handling demo
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []


# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    # TODO: Add code here
    file = open(file_name, 'wb')
    pickle.dump(list_of_data, file)
    file.close()


def read_data_from_file(file_name):
    # TODO: Add code here

    file = open(file_name, 'rb')
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data


# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
# TODO: store the list object into a binary file
# TODO: Read the data from the file into a new list object and display the contents
ID = input('Enter your ID number: ')
Name = input('Enter your name: ')
lstCustomer = [ID, Name]
save_data_to_file(strFileName, lstCustomer)
print(read_data_from_file(strFileName))

# demo error handling #
try:

    a = [1,2,3,4,5]
    number = input('please guess the length of the list from 1 to 10: ')
    if not number.isdigit():
        raise Exception('Please enter number and integer only')

    elif len(a) > int(number):
        raise Exception('Your estimation is too low, please guess again')

    elif int(number)>len(a):
        raise Exception('Your estimation is too high, please guess again')

    elif int(number)==len(a):
        print()
        print('Congratulation you won the jackpot')

except Exception as e:
    print('There was a non-specific error')
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
print()
print('------------------')

try:
    userinput = input("Enter name of module to import: ")
    module = __import__(userinput)

except ModuleNotFoundError as e:
    print('Please verify module name')
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except ValueError as e:
    print('Module name can\'t be empty')
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print('There was a non-specific error')
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

print()
print('------------------')

try:
    number1=input('enter a first number: ')
    number2=int(input('Enter a second number: '))
    sum_totoal=number1+number2
    print(sum)
except TypeError as e:
    print('Check with author, code is incorrect.')
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print('There was a non-specific error')
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
