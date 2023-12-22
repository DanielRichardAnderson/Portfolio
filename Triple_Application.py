"""
An application with three different programmes:
   -A panlindrome detector, which will strip all numbers, white-space
    and punctuation from a string, then test if it's the same when 
    reversed. i.e. a palindrome.
    
  - A number guessing game, where the user chooses a number range, then 
    they have to guess, using the hints, the randomly chosen number 
    within that range.
    
   -A simple calculator. Self explanitory. Only the operations +,-,/ 
    and * can be used.
"""
#####################################################
#                                                   #
# Supporting functions                              #
#                                                   #
#####################################################

import random
import pickle
import os

# Getting the username.
username = os.environ.get("USER")

######################################
# Palindrome Detector                #
######################################
def is_palindrome(word):
    word = word.lower()
    
    # Taking the imput word adn removing all spaces,
    # punctuation, etc...
    word2=''
    for letter in word:
        if letter.isalpha():
            word2 += letter
            
    # Checking if the cleaned word is the same forwards as backwards.
    return word2 == word2[::-1]
    

def main():
    user_input = input("Enter a word: ")
    result = is_palindrome(user_input)
    
    if result:
        print(f"{user_input} is a palindrome!")
    else:
        print(f"{user_input} is not a palindrome.")

######################################
# Number Guessing Game               #
######################################
def guessing_game():
    # Starting a counter for attempts
    attempts = 0
    
    # Getting user to choose their number-range
    print("\n____|||| Number Guessing Game ||||____")
    print("Let's try and guess a number between 1 and your choice...")
    while True:
        try:
            num_choice = int(input("Enter number here:"))
            break
        except:
            print("Error: You need to enter a whole-number")
        
    # Finding the number to guess
    rand = random.randint(1, num_choice)
    
    # Opening the total_attempts
    file_path = f"/Users/{username}/Documents/python_files"
    if os.path.exists(file_path+'/all_time_attempts.pkl'):
        with open(file_path+'/all_time_attempts.pkl', 'rb') as to_open:
            all_time_att = pickle.load(to_open)
    else:
        all_time_att = 0
      
    # Opening the total_guesses   
    if os.path.exists(file_path+'/all_time_guesses.pkl'):
        with open(file_path+'/all_time_guesses.pkl','rb') as to_open:
            all_time_ges = pickle.load(to_open)
    else:
        all_time_ges = 0
    
    print(f"Great choice! So it's between 1 and {num_choice}.\n")
    
    # Looping until the the user guesses the number
    # or types 'exit'
    while True:
        user_input = int(input("Make a guess!\
                                \n-Or type 'exit' to quit: "))
        attempts +=1
        
        if user_input == rand:
            print(f"\nPerfect! {user_input} is right!\
                   \nAnd it took you {attempts} attempts.") 
            
            all_time_att += 1
            all_time_ges += attempts
            
            print(f"The all-time average number of guesses is"\
                  f" {all_time_ges/all_time_att}")
            
            with open(file_path+"/all_time_attempts.pkl", 'wb') as to_write:
                pickle.dump(all_time_att, to_write)
            
            with open(file_path+"/all_time_guesses.pkl", "wb") as to_write:
                pickle.dump(all_time_ges, to_write)
            break
        
        elif user_input < rand:
            print(f"--Nope, it's higher than {user_input}")
            continue
        elif user_input > rand:
            print(f"--Nope, it's lower than  {user_input}")
            continue
        elif user_input.lower() == 'exit':
            print("Exiting the Number Guessing Game.\n")
            break
             
#####################################
# Simple Calculator                 #
#####################################
def calculator():
    print("\n____|||| Calculator ||||____")
    
    while True:
        # Getting the first input
        while True:
            try:
                num1 = float(input("Enter first number here: "))
                break
            except ValueError:
                print("Value Error. Enter a number.")
        
        # Getting the operation
        while True:
            operation = input("Enter operation here (+, -, /, * ): ")
            if len(operation)== 1 and operation in ['+', '-', '/', '*']:
                break
            else:
                print("You need to enter +, -, /, or * ONLY ")
                continue
        # Getting tge second number
        while True:
            try:
                num2 = float(input("Enter second number here: "))
                break
            except ValueError:
                print("Value Error. Enter a number.")
        
        XX = 'ok'
        # Getting the results from the calculations.
        if operation == '+':
            result = num1+num2
        
        elif operation =='-':
            result = num1-num2
        
        elif operation =='*':
            result = num1*num2
            
        elif operation =='/':
            if num2 != 0:
                result = num1/num2
            else:
                print("\nError: Devision by zero!")
                XX = 'err'
        else:
            print("\nThere's some error with the input.")
            XX = 'err'
        
        # Printing the result
        if XX != 'err':
            print(f"{num1} {operation} {num2} = {result}")
        
        # Asking if user wants to play again.
        while True:
            in2 = input("\nDo you want to calculate again? (y/n): ")
            print()
            
            if in2.lower() == 'y':
                ans = 'y'
                break
            elif in2.lower() == 'n':
                ans= 'n'
                break
            else:
                print('You need to type "y" or "n"...')
                continue
        
        # If user choses to play again, to back to the top
        # else break and finish the application.
        if ans=='y':
            continue
        else:
            break

#####################################################
#                                                   #
# Main menu                                         #
#                                                   #
#####################################################

# Checking if the the programme is being run on its own
# or if one of its functions is being used as an import elsewhere.
if __name__ == "__main__":
    pass

# Starting the application.
print('** Application opened **\n')
while True:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    in1 = input("\nProgramme list:\
                \n  1) Palindrome Detector.\
                \n  2) Number Guessing Game.\
                \n  3) Simple Calculator.\
                \nOr type 'exit' to close the application.\
                \nWhich programme do you want to run?: ")
    
    if in1 == '1':
        print("\n____|||| Palindrome Detector ||||____")
        main()
        
    elif in1 == '2':
        guessing_game()
        
    elif in1 == '3':
        calculator()
        
    elif in1.lower() == 'exit':
        break
    else:
        print("\nYou need to input a valid number or 'exit'.")
        continue
    
    # Asking if the user wants to use another programme.
    while True:
        in2 = input("\n_______Main Menu\nSelect another programme? (y/n): ")
        
        if in2.lower() == 'y':
            ans = 'y'
            break
        elif in2.lower() == 'n':
            ans= 'n'
            break
        else:
            print('You need to type "y" or "n"...')
            continue
    
    # If user choses to play again, to back to the top
    # else break and finish the application.
    if ans=='y':
        continue
    else:
        break
print("\n** Application closed **\n")