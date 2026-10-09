"""
Name: Oluwaseun Oyatorisa
Peers: None
References: (anything you checked to solve this)
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    """ updates content of grades depending on the user's input

    Updates the values inside the global variable grades (list)
    with each of the user's 5 input ints.
    If the user inputs are not digits, it prints
    "Error in read_five_ints: input string is not for an integer",
    and if the input converted to int is outside of [0,10], prints
    "Error in read_five_ints: input integer outside of range".
    """
    for idx in range(5):
        #User gives in grade input in the interval [0, 10]
        in_str = input("Give me the next grade in [0,10]:")
 #If the input isn't inside the interval, then it prints the error
        if not in_str.isdigit():
            print("Error in read_five_ints: input string is not for an integer")
            exit()
#Convert the string into a integer
        num = int(in_str)
#Check if the input is outside of the interval [0,10] if it is then print the following error statement
        if num < 0 or num > 10:
            print("Error in read_five_ints: input integer outside of range")
            exit()
#Store the integers into the grades index
        grades[idx] = num
    pass
    #Anything with this indentation is NO LONGER inside the loop


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """ returns an average depending on the user's selection

    Obtains an average using either mean, median or mode,
    depending on user input.
    User should pick 'a' for mean, 'b' for median, 'c' for mode.
    Any other input prints
    'Error in pick_averaging_method: incorrect option picked'.
    """
    #Let the user pic their averaging metod, user should pick between a to c
    choice = input("Pick an averaging method (a: mean, b: median, c: mode):")
    if choice == "a":
        return statistics.mean(grades)
    elif choice == "b":
        return statistics.median(grades)
    elif choice == "c":
        return statistics.mode(grades)
    #if they don't pick within the 3 options of a to c, then return the error as follow
    else:
        print("Error in picking_averaging_method: incorrect option picked")
    pass

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    """
    #print result using user's selection
    choice = input("Pick how to print average method( 1: print average, or 2: plot average):")

    # Sort the grades and display them in order
    grades.sort()
    print(f"sorted grades: {grades}")
    # print the numeric average if it equals 1 = numeric average
    if choice == "1":
        print("average")
    # print the plot average if the user picks 2
    elif choice == "2":
        print(f"Average: {average}")
    # if the user choice an option thats not part, then say the following error
    else:
        print("Error in pick_visualization:incorrect option picked")
    pass


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
