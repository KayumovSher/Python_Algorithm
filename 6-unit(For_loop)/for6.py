price = int(input("Enter a kg sweet of price $"))

for i in range(2, 21):
    if i%2==0:
        print(f"{i/10}kg -> ${i/10*price}")