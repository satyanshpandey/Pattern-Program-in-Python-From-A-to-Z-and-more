#____________________________________________Pattern_no.#22_(R)___________________________________
# OUTPUT:-

#                                                    ****
#                                                    *   *
#                                                    *   *
#                                                    ****
#                                                    *   *
#                                                    *   *
#                                                    *   *

# ______________________________________________SATYANSH_PANDEY___________________________________





for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=3)) or ((row==0 or row==3) and col!=4):
            print("*",end="")
        else:
            print(end=" ")
    print()

