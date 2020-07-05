airline = input()
Source = []
src = input("Enter Source:")
dest = input("Enter destination:")
starting_no = 101
print(src[0:3])
print(dest[0:3])
newSrc = src[0:3]
newDest = dest[0:3]
no_of_passengers = int(input("Enter no of passengers:"))
ticket_no = 0
total = []
list = []
for ticket_no in range(1,no_of_passengers+1):
    # print(ticket_no)
    # print("Ticket no. is :",starting_no)

    total = [(airline+":"+newSrc+":"+newDest+":"+ str(starting_no))]
    starting_no = starting_no+1
    print(total)
    list.append(total)
    # print(list)

print(list[::1])