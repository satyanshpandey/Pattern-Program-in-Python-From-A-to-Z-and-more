#____________________________________________Pattern_no.#14_(J)___________________________________
# OUTPUT:-

#                                               *****
#                                                 *
#                                                 *
#                                                 *
#                                                 *
#                                               * *
#                                               ***

# __________________________________________SATYANSH_PANDEY___________________________________





for row in range(7):
    for col in range(5):
        if col==2 or (row==0) or (row==6 and col<2) or (row==5 and col==0):
            print("*",end="")
        else:
            print(end=" ")
    print()

