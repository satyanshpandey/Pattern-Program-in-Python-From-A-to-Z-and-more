#____________________________________________Pattern_no.#13_(I)___________________________________
# OUTPUT:-

#                                                *****
#                                                  *
#                                                  *
#                                                  *
#                                                  *
#                                                  *
#                                                *****

# __________________________________________SATYANSH_PANDEY___________________________________





for row in range(7):
    for col in range(5):
        if col==2 or (row==0 or row==6):
            print("*",end="")
        else:
            print(end=" ")
    print()

