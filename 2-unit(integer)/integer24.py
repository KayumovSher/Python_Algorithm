# The days of the week are given in the following order. 0 Sunday, 1 Monday, 2 Tuesday, 3 Wednesday, 4 Thursday, 5 Friday, 6 Saturday.
# A number K lying in the interval 1-365 is given. If January 1 is Monday, create a program that determines which day of the week the entered K-day falls on.

K = int(input("Iltimos 1dan 365 gacha istalgan butun son kiriting. K -> "))


# Define a dictionary to map day numbers to their names
days_map = {
    0: "Yakshanba",
    1: "Dushanba",
    2: "Seshanba",
    3: "Chorshanba",
    4: "Payshanba",
    5: "Juma",
    6: "Shanba"
}

# hafta = K%int(days_map[1])
hafta = K%7


print(f"{K} kuni haftaning {days_map[hafta]} kuniga to'g'ri keladi.")
# x2 = days_map[2]
# print(x2)