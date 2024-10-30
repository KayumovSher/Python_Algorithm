number_month = int(input("Please enter number of month -> "))

if 1 <= number_month <= 12:
    if number_month == 1:
        print("January 31 days")
    elif number_month == 2:
        print("February 28 days")
    elif number_month == 3:
        print("March 31 days")
    elif number_month == 4:
        print("April 30 days")
    elif number_month == 5:
        print("May 31 days")
    elif number_month == 6:
        print("June 30 days")
    elif number_month == 7:
        print("July 31 days")
    elif number_month == 8:
        print("August 31 days")
    elif number_month == 9:
        print("September 30 days")
    elif number_month == 10:
        print("October 30 days")
    elif number_month == 11:
        print("November 30 days")
    elif number_month == 12:
        print("December 31 days")
        
else:
    print("You did not enter from 1 to 12")