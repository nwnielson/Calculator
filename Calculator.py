import Calc_Functions

keep_solving = "yes"

equation = input("\nWelcome to the Calculator!\n\n\
Enter the equation you would like solved: \nEquation: ")

while keep_solving == "yes":
    solution = Calc_Functions.pemdas(equation)
    print("Solution:", solution, "\n")
    
    # If there is an error, blank list will be produced and loop will run
    while solution == [] :
        equation = input("Error, please ensure there are no characters other than numbers and +-*/^() ")
        solution = Calc_Functions.pemdas(equation)
    keep_solving = input("Would you like to solve another equation? (Yes or No) ").lower()
    
    # If something other than yes or no, will prompt user to enter yes or no to keep solving
    while keep_solving not in "yes,no" :
        print("Invalid response. Please enter yes or no.")
        keep_solving = input("Would you like to solve another equation? (Yes or No) ").lower()
    if keep_solving == "yes" :
        equation = input("\n\nEnter the equation you would like solved: \nEquation: ")
        