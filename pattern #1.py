#______________________________________________________________Pattern_no.#2_____________________________________________
# OUTPUT:-

                    # Enter row:5
                        *
                       * *
                      * * *
                     * * * *
                    * * * * *


# ______________________________________________________SATYANSH_PANDEY__________________________________________________


num = int(input("Enter row:"))
for i in range(0,num):
    # print(i)
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()