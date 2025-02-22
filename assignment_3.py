
# # DATA 602 Assignment 3
# Author: Kevin Havis

# ## Q1
# Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner


import random

def meal_time():

    # initiate menu
    bfast = ['oatmeal', 'cereal', 'fruit']
    lunch = ['sandwich', 'salad', 'rice bowl']
    dinner = ['stew', 'roast', 'pizza']

    # Get user input
    meal = input('What meal are you having?')

    # Recommend random menu item
    if meal == 'breakfast':
        print(f"What about some {bfast[random.randint(0,2)]}?")
    elif meal == 'lunch':
        print(f"What about a {lunch[random.randint(0,2)]}?")
    elif meal == 'dinner':
        print(f"What about a {dinner[random.randint(0,2)]}?")
    else:
        "New meal, cool!"
    
    return None

meal_time()


# ## Q2
# The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20. 
# You should take in the user’s input for the number of hours worked, and their rate of pay.


def payroll():

    OVER_RATE = 1.5
    BASE_HOURS = 20

    hours = float(input("Employee hours worked: "))
    rate = float(input("Employee pay rate: "))

    if hours > BASE_HOURS:
        base_pay = BASE_HOURS * rate
        overtime = hours % BASE_HOURS        
        over_pay = overtime * OVER_RATE
        gross_pay = base_pay + over_pay
    else:
        gross_pay = hours * rate

    print(f"Employee gross pay: {gross_pay}")

    return None

payroll()

# 
# ## Q3
# Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.


def times_ten(x):
    
    y = x * 10
    print (y)

    return None

times_ten(10)


# ## Q4
# Find the errors, debug the program, and then execute to show the output.
# ```python
# def main()
#       Calories1 = input( "How many calories are in the first food?")
#       Calories2 = input( "How many calories are in the first food?")
#       showCalories(calories1, calories2)
# 
# def showCalories()   
#    print(“The total calories you ate today”, format(calories1 + calories2,.2f))
# ```



# Fixed version

# This needs to be defined before main()
def showCalories(calories1, calories2): # added colon,  arguments
   print(f'The total calories you ate today {calories1 + calories2:.2f}')

def main(): # added colon
      calories1 = int(input( "How many calories are in the first food?")) # fixed variable names, convert to int
      calories2 = int(input( "How many calories are in the second food?")) # updated prompt to "second food"
      showCalories(calories1, calories2)

main()


# ## Q5
# Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
#          1/30 + 2/29 + 3/28 ............. + 30/1


def factorial_fractions():

    # initiate variables
    num = 1
    denom = 30
    x = 0

    # Divide, add to total, update variables, repeat
    while num < 31 and denom > 0: # redundacy, but good practice I think?
        x += num / denom
        num += 1
        denom -= 1
    
    print(x)

    return None

factorial_fractions()


# ## Q6
# Write a function that computes the area of a triangle given its base and height.
# The formula for an area of a triangle is:
# AREA = 1/2 * BASE * HEIGHT
# 
# For example, if the base was 5 and the height was 4, the area would be 10.
# triangle_area(5, 4)   # should print 10



def triangle_area(base, height):
    area = base * height * 0.5
    print(area)
    return None

triangle_area(5, 4)


