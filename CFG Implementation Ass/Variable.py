# ===============================================JAVA LANGUAGE===============================================
# ============================================CFG IMPLEMENTATION=============================================
# =================================FOR VARIABLE DECLARATION & INITIALIZAATION================================


# Storing values for variable initialization
# __________________________________________

integer_values = [str(x) for x in range(1001)]


bool_values = ['True', 'False']
symbols = ['$', '_']

# Defining keywords for variable declaration
# __________________________________________

key_words = ['int', 'boolean', 'char']

# Defining a function
# ___________________

def func(programmer_input):
    if (programmer_input[0] in key_words):  # Checking data type
        if programmer_input[1][0].isalpha() or programmer_input[1][0] in symbols:  # Checking variable declaration
            if len(programmer_input) >= 4 and programmer_input[2] == '=' and programmer_input[-1] == ';':  # Checking syntax
                if (programmer_input[0] == 'int'): # Checking for integer
                    if (programmer_input[3] in integer_values):  # Checking variable initialization
                        print("\nYou created a valid int variable.")
                    else:
                        print("\nInvalid int variable initialization!")
                elif (programmer_input[0] == 'boolean'):
                    if programmer_input[3] in bool_values:  # Checking variable initialization
                        print("\nYou created a valid boolean variable.")
                    else:
                        print("\nInvalid boolean variable initialization!")
                
                elif programmer_input[0] == 'char':
                    if len(programmer_input[3]) == 3 and programmer_input[3][0] == "'" and programmer_input[3][2] == "'":  # Checking variable initialization
                        print("\nYou created a valid char variable.")
                    else:
                        print("\nInvalid char variable initialization!")
                else:
                    print("\nInvalid data type!")
            else:
                print("\nInvalid syntax!")
        else:
            print("\nInvalid variable name!")
    else:
        print("\nInvalid data type!")


# Taking input from the programmer
# ________________________________

programmer_input = input("\nEnter a variable declaration and initialization: ")
# Creating a list of strings given by the programmer
# __________________________________________________

array_programmer_input = programmer_input.split()
func(array_programmer_input) # calling function to check whether a programmer declare and initiazlize a variable correctly?
