N = int(input("Enter how many seconds passed from beginning a day -> "))

hour = N//3600
second = N%60

print(f"Given passed seconds are {N}, from beginning a day - {hour}hour and {second}seconds passed.")