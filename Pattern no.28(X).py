#____________________________________________Pattern_no.#28_(X)___________________________________
# OUTPUT:-

#                                                    *   *
#                                                     * *
#                                                      *
#                                                     * *
#                                                    *   *

# ______________________________________________SATYANSH_PANDEY___________________________________



for row in range(5):
    for col in range(5):
        if (row==col) or (row+col==4):
            print("*",end="")
        else:
            print(end=" ")
    print()

