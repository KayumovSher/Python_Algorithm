# Input the positive integers.
N = int(input('Enter N value: '))
K = int(input('Enter K value: '))

# Chek both integers positive or not.
if N < 0:
    # Ensure K value bigger than 0 or not.
    while K <= 0:
        # Output the incorrect value.
        print("K value must be bigger than 0. Please enter valid value!")
        # Input the positive integers.
        # N = int(input('Enter N value: '))
        K = int(input('Enter K value: '))
    # Initialize to digest variables.
    reminder = 0
    patent = 0
    # Ensure K value is bigger than N value
    while N >= K:
        N -= K
        patent += 1
    # To digest the N value to 'patent' variable
    reminder = N
    # Output two results
    print(f"The reminder {N} divided by {K} is: {reminder}")
    print(f"The patent {N} divided by {K} is: {patent}")
    
# Output the valid negative number.
else:
    print("N value must be positive numbers. Please enter valid value.")