# Compas
#               N (Shimol)
#               |
#               |
# (G'arb)       |
# W <----------(*)----------> E 
#               |      (Sharq)
#               |
#               |
#       (Janub) S


Y = input("Enter direction of robot;\n'To North(n)', 'To South(s)', 'To East(e)', 'To West(w)' -> ")
K = input("Enter your command;\n'Continue your action(0), 'Turn Left(1), 'Turn Right(2)' -> ")

print("Action of the Robot is: ", end="")

# if (Y != "n" or Y != "s" or Y != "e"or Y != "w") and (K != "0" or K != "1" or K != "2"):
#     print("YOU DID NOT ENTER TRUE DIRECTION & COMMAND. Please enter Direction and Command again!")

if Y == "n":
    if K == "0":
        print("It continued to move northward")
    elif K == "1":
        print("It turned Left to the north")
    elif K == "2":
        print("It turned Right to the north")
    else:
        print("YOU DID NOT ENTER TRUE COMMAND. Please enter Direction and Command again!")
elif Y == "s":
    if K == "0":
        print("It continued to move southward")
    elif K == "1":
        print("It turned Left to the south")
    elif K == "2":
        print("It turned Right to the south")
    else:
        print("YOU DID NOT ENTER TRUE COMMAND. Please enter Direction and Command again!")
elif Y == "e":
    if K == "0":
        print("It continued to move eastward")
    elif K == "1":
        print("It turned Left to the east")
    elif K == "2":
        print("It turned Right to the east")
    else:
        print("YOU DID NOT ENTER TRUE COMMAND. Please enter Direction and Command again!")
elif Y == "w":
    if K == "0":
        print("It continued to move westward")
    elif K == "1":
        print("It turned Left to the west")
    elif K == "2":
        print("It turned Right to the west")
    else:
        print("YOU DID NOT ENTER TRUE COMMAND. Please enter Direction and Command again!")
elif (Y != "n" or Y != "s" or Y != "e"or Y != "w") and (K != "0" or K != "1" or K != "2"):
    print("YOU DID NOT ENTER TRUE DIRECTION & COMMAND. Please enter Direction and Command again!")
# else:
#     print("YOU DID NOT ENTER TRUE DIRECTION & COMMAND. Please enter Direction and Command again!")
