#____________________________________________Pattern_no.#30_(Z)___________________________________
# OUTPUT:-

#                                                    ****
#                                                      *
#                                                     *
#                                                    ****

# ______________________________________________SATYANSH_PANDEY___________________________________





for row in range(4):
    for col in range(4):
        if (row==0 or row==3) or (row+col==3):
            print("*",end="")
        else:
            print(end=" ")
    print()

