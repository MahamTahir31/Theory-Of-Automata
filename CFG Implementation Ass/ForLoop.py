# ===============================================JAVA LANGUAGE===============================================
# ============================================CFG IMPLEMENTATION=============================================
# ==============================================FOR 'for' LOOP===============================================


# Storing values for 'for loop'
# _____________________________

values = [str(x) for x in range(1001)]
operators_for_condition = ['<','>','<=','>=','==','!']
operators_for_incremental = ['++', '--']

# Defining a function
# ___________________

def func(programmer_input):
    if(len(programmer_input)==14):
        if (programmer_input[0] =='for'): # checking for 'for' keyword
            if(programmer_input[1]=='(' and programmer_input[13]==')'): # checking syntax
                if(programmer_input[2]== 'int' and programmer_input[3][0].isalpha() and programmer_input[4]=='=' and programmer_input[5] in values): #checking initialization 
                    if(programmer_input[6] ==';' and programmer_input[10]==';'): # checking syntax inside the for loop
                        if(programmer_input[7][0].isalpha() and programmer_input[8] in operators_for_condition and programmer_input[9] in values): # checking for conditional statement
                            if(programmer_input[11].isalpha() and programmer_input[12] in operators_for_incremental): # checking for incremental condition
                                print("\nValid For Loop")
                            else:
                                print("\nInvalid Syntax for incremental!")
                        else:
                            print("\nInvalid Syntax for condition!")
                    else:
                        print("\nInvalid separation of for loop parameters!")
                   
                else:
                    print("\nInvalid Syntax for initialization!")
            else:
                print("\nInvalid Syntax!")  

        else:
            print("\nInvalid Syntax to create a for loop!")
    else:
        print("\nyour statement is too short to define a for loop!")




# Taking input from the programmer
# ________________________________

programmer_input = input("\nEnter for loop: ")

# Creating a list of strings given by the programmer
# __________________________________________________

array_programmer_input = programmer_input.split()
func(array_programmer_input)  # calling function to check whether a programmer define prototype of for loop correctly?