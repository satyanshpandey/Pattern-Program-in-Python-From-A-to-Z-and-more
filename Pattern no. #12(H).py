#____________________________________________Pattern_no.#12_(H)___________________________________
# OUTPUT:-

#                                                *   *
#                                                *   *
#                                                *   *
#                                                *****
#                                                *   *
#                                                *   *
#                                                *   *

# __________________________________________SATYANSH_PANDEY___________________________________





for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 or (row==3 and (col>0 and col<4))):
            print("*",end="")
        else:
            print(end=" ")
    print()

