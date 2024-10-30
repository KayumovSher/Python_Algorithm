a = int(input("a = "))
b = int(input("b = "))

sum_of_number = 0
if a < b:
    for i in range(a, b+1):
        sum_of_number += i
    print(sum_of_number)
        
# # Input two integers
# start_num = int(input("Enter the starting integer: "))
# end_num = int(input("Enter the ending integer: "))

# # Initialize a variable to store the sum
# sum_of_numbers = 0

# # Use a for loop to iterate through the range and calculate the sum
# for num in range(start_num, end_num + 1):
#     sum_of_numbers += num

# # Output the result
# print("The sum of numbers from {} to {} is: {}".format(start_num, end_num, sum_of_numbers))
