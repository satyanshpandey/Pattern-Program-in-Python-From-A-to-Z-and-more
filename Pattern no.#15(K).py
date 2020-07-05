#____________________________________________Pattern_no.#15_(K)___________________________________
# OUTPUT:-

#                                                 *   *
#                                                 *  *
#                                                 * *
#                                                 **
#                                                 * *
#                                                 *  *
#                                                 *   *


# _____________________________________________SATYANSH_PANDEY___________________________________

for row in range(7):
    for col in range(5):
        if col==0 or (row==col+2 and col>1) or (row+col==4):
            print("*",end="")
        else:
            print(end=" ")
    print()


#
#
########### ANOTHER WAY TO PRINT THE 'K' SHAPE PATTERN IN PYTHON
#
#




# i=0
# j=4
# for row in range(7):
#     for col in range(5):
#         if col==0 or (row==col+2 and col>1):
#             print("*",end="")
#         elif (col==j and row==i):
#             print("*",end="")
#             i=i+1
#             j=j-1
#         else:
#             print(end=" ")
#     print()



