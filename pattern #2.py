#______________________________________________________________Pattern_no.#2_____________________________________________
# OUTPUT:-
# Enter the value of the row:6
#      1
#     212
#    32123
#   4321234
#  543212345
# 65432123456
# ______________________________________________________SATYANSH_PANDEY__________________________________________________

num = int(input("Enter the value of the row:"))
for i in range(1,num+1):
        for j in range(1,num-i+1):
                print(end=" ")
        for j in range(i,0,-1):
                print(j,end="")
        for j in range(2,i+1):
                print(j,end="")
        print()


