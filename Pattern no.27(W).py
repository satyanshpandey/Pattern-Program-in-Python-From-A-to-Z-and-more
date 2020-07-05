#____________________________________________Pattern_no.#27_(W)___________________________________
# OUTPUT:-

#                                                    *  *  *
#                                                    * * * *
#                                                    **   **
#                                                    *     *

# ______________________________________________SATYANSH_PANDEY___________________________________





for row in range(4):
    for col in range(7):
        if (col==0 or col==6) or (col==5 and row==2) or (col==4 and row==1) or (col+row==3):
            print("*",end="")
        else:
            print(end=" ")
    print()

