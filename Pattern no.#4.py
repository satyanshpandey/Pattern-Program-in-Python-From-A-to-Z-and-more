
#___________________________________________________Pattern_no.#4_____________________________________________
# OUTPUT:-

#                           Enter row:5
#                           * * * * *
#                            * * * *
#                             * * *
#                              * *
#                               *

# ______________________________________________________SATYANSH_PANDEY__________________________________________________
num = int(input("Enter row:"))
for i in range(num,0,-1):
    # print(i)+
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()