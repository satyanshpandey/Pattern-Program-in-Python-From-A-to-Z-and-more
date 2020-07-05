#____________________________________________Pattern_no.#29_(Y)___________________________________
# OUTPUT:-

#                                                    *   *
#                                                     * *
#                                                      *
#                                                      *
#                                                      *
#

# ______________________________________________SATYANSH_PANDEY___________________________________





for row in range(5):
    for col in range(5):
        if (col==2 and row>1) or (row==col and col<2) or (row+col==4 and col>2):
            print("*",end="")
        else:
            print(end=" ")
    print()

