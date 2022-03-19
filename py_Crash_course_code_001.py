def greeting(name, department):
    print("Welcome, "+name)
    print("You are part of " + department)


greeting("Kay", "Engneering")


def print_seconds(hours, minutes, seconds):
    print("Total seconds are ", 3600*hours+60*minutes+seconds)


print_seconds(1, 2, 3)


def area_triangle(base, height):
    return base*height/2


print(area_triangle(4, 3))


def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds


amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a+amount_b
print(result)


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600)//60
    remaining_seconds = seconds - hours*3600 - minutes * 60
    return hours, minutes, remaining_seconds


print(convert_seconds(7653))


def lucky_number(name):
    number = len(name)*9
    print("Hello "+name+". Your lucky number is "+str(number))


lucky_number("Kay")
lucky_number("Cameron")


def month_days(month, days):
    print(month+" has "+str(days)+" days.")


month_days("June", 30)
month_days("July", 31)


def rectangle_area(base, height):
    area = base*height  # the area is base*height
    print("The area is " + str(area))


rectangle_area(5, 6)


# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km


my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2*my_trip_km))


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1


# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)


def lucky_number(name):
    number = len(name) * 9
    message = "Hello " + name + ". Your lucky number is " + str(number)
    return message


print(lucky_number("Kay"))
print(lucky_number("Cameron"))


def is_positive(number):
    if number > 0:
        return True
    else:
        return False


print(is_positive(13))
print(is_positive(-1))
print(is_positive(0))


def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Good to go")


hint_username("Rock")
hint_username("Rock and Roll Forever")


def is_even(number):
    if number % 2 == 0:
        return True
    return False


is_even(17)
is_even(6)
is_even(0)


def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


print(number_group(10))  # Should be Positive
print(number_group(0))  # Should be Zero
print(number_group(-5))  # Should be Negative

print(2**2)

# Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based on whether or not that name is "Taylor".


def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor!"
    else:
        return "Hello there, " + name


print(greeting("Taylor"))
print(greeting("John"))


# What’s the output of this code if number equals 10?
def test_number(number):
    if number > 11:
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
        print(2)
    else:
        print(3)


test_number(10)


# Is "A dog" smaller or larger than "A mouse"? Is 9999+8888 smaller or larger than 100*100? Replace the plus sign in the following code to let Python check it for you and then answer.
print("A dog" < "A mouse")
print(9999+8888 < 100*100)

# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks+1)*block_size
    return full_blocks*block_size


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192


# Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.
def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color


print(color_translator("blue"))  # Should be #0000ff
print(color_translator("yellow"))  # Should be unknown
print(color_translator("red"))  # Should be #ff0000
print(color_translator("black"))  # Should be unknown
print(color_translator("green"))  # Should be #00ff00
print(color_translator(""))  # Should be unknown


print("big" > "small")


# Students in a class receive their grades as Pass/Fail. Scores of 60 or more(out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". Fill in this function so that it returns the proper grade.

def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade


print(exam_grade(65))  # Should be Pass
print(exam_grade(55))  # Should be Fail
print(exam_grade(60))  # Should be Pass
print(exam_grade(95))  # Should be Pass
print(exam_grade(100))  # Should be Top Score
print(exam_grade(0))  # Should be Fail


print(11 % 5)


# Complete the body of the format_name function. This function receives the first_name and last_name parameters and then returns a properly formatted string.

def format_name(first_name, last_name):
    # code goes here
    if first_name != "" and last_name != "":
        string = ("Name: " + last_name + ", " + first_name)
    elif first_name != "" and last_name == "":
        string = ("Name: " + first_name)
    elif first_name == "" and last_name != "":
        string = ("Name: " + last_name)
    else:
        string = ""
    return string


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


# Question 7
# The longest_word function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length). Fill in the blank to make this happen.

def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1
    elif len(word2) >= len(word1) and len(word2) >= len(word3):
        word = word2
    else:
        word = word3
    return(word)


print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


# Q8: What’s the output of this code?

def sum(x, y):
    return(x+y)


print(sum(sum(1, 2), sum(3, 4)))


print(((10 >= 5*2) and (10 <= 5*2)))


# Question 10:
# The fractional_part function divides the numerator by the denominator, and returns just the fractional part(a number between 0 and 1). Complete the body of the function so that it returns the right number.
# Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient
    if denominator == 0:
        return 0
    elif numerator % denominator == 0:
        return 0
    else:
        return(numerator/denominator-numerator//denominator)


print(fractional_part(5, 5))  # Should be 0
print(fractional_part(5, 4))  # Should be 0.25
print(fractional_part(5, 3))  # Should be 0.66...
print(fractional_part(5, 2))  # Should be 0.5
print(fractional_part(5, 0))  # Should be 0
print(fractional_part(0, 5))  # Should be 0


x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x+1
print("x=" + str(x))

# While Loop


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(5)


# while example 03
'''
username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()
'''

# initializing variables


def count_down(start_number):
    current = start_number
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")


count_down(3)


# Infinite Loop

def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)
        n += 1


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)

# Loop quiz:


# Question 2: Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.

def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            # If it's not, increment the factor by one
            factor += 1
    return "Done"


print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT


# Question 3：The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.
# Note: Try running your function with the number 0 as the input, and see what you get!

def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    if n == 0:
        return False
    else:
        while n % 2 == 0:
            n = n / 2
        # If after dividing by two the number is 1, it's a power of two
        if n == 1:
            return True
        return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False


# Question 4: Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
    sum = 0
    divisor = 1
    if n == 0:
        return 0
    else:
        while divisor <= n/2:
            if n % divisor == 0:
                sum += divisor
            divisor += 1
        # Return the sum of all divisors of n, not including n
        return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 1+2+3+6+17+34+51
# 114


# The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. An additional requirement is that the result is not to exceed 25, which is done with the break statement. Fill in the blanks to complete the function to satisfy these conditions.

def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number * multiplier
        # What is the additional condition to exit out of the loop?
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        multiplier += 1


multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24


# For Loop

def square(n):
    return n*n


def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum


print(sum_squares(10))  # Should be 285


# In math, the factorial of a number is defined as the product of an integer and all the integers below it. For example, the factorial of four (4!) is equal to 1*2*3*4=24. Fill in the blanks to make the factorial function return the right number.
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(factorial(4))  # should return 24
print(factorial(5))  # should return 120


# Domino cards
for left in range(7):
    for right in range(left, 7):
        print("["+str(left)+"|"+str(right)+"]", end=" ")
    print()


# team paring
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team+" VS "+away_team)


# The validate_users function is used by the system to check if a list of users is valid or invalid. A valid user is one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. When calling it like in this example, something is not right. Can you figure out what to fix?

def is_valid(user):
    if len(user) >= 3:
        return True
    else:
        return False


def validate_users(users):
    for user in users:
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")


validate_users(["purplecat"])


# Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.
def factorial(n):
    result = 1
    for x in range(1, n+1):
        result = result * x
    return result


for n in range(0, 10):
    print(n, factorial(n))


# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.
for x in range(1, 11):
    print(x**3)


# Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.

def mul7(n):
    for n in range(0, n+1):
        if n % 7 == 0:
            print(n)
    return


mul7(100)


# The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.  Currently the code will keep executing the function even if it succeeds. Fill in the blank so the code stops trying after the operation succeeded.

def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("Attempt " + str(n) + " succeeded")
            break
        else:
            print("Attempt " + str(n) + " failed")


retry(create_user, 3)
retry(stop_service, 5)
