def fizz_buzz(m):
    """Checks if the specified numbers in range is fizz or buzz or both."""
    for n in range(1, m + 1):  # start loop for iteration through specified list
        if n % 2 == 0 and n % 3 == 0:  # checks if the number can be divided by 2 and 3
            print("Fizz Buzz")
        elif n % 3 == 0:  # checks if the number can be divided by 3
            print("Buzz")
        elif n % 2 == 0:  # checks if the number can be divided by 2
            print("Fizz")
        else:
            print(n)

fizz_buzz(100)  # calling the fizz_buzz function with specified range
