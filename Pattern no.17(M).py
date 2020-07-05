#____________________________________________Pattern_no.#17_(M)___________________________________
# OUTPUT:-

#                                                    *     *
#                                                    **   **
#                                                    * * * *
#                                                    *  *  *
#                                                    *     *
#                                                    *     *
#                                                    *     *

# _______________________________________________SATYANSH_PANDEY___________________________________


for row in range(7):
    for col in range(7):
        if (col==0 or col==6) or (row==col and col<4) or (row+col==6 and col>3) :
            print("*",end="")
        else:
            print(end=" ")
    print()

