conducted = 0
attended = 0
tempPercent = 0
reqPercent = 85
flag = 0
attendedT = attended
conductedT = conducted
required = 0
bunkable = 0


conducted=int(input("Enter classes conducted\n"))
attended=int(input("Enter classes attended\n"))

attendedT = attended
conductedT = conducted

tempPercent = (attendedT / conductedT) * 100
print("Your percent is " + str(tempPercent))

if tempPercent < reqPercent:
    while flag == 0:
        if tempPercent < reqPercent:
            tempPercent = (attendedT / conductedT) * 100
            attendedT += 1
            conductedT += 1
            required += 1
        else:
            print("You need to attend " + str(required) + " lectures")
            flag = 1

elif tempPercent > reqPercent:
    while flag == 0:
        conductedT += 1
        tempPercent = (attendedT / conductedT) * 100
        if tempPercent > reqPercent:
            bunkable += 1
        else:
            flag = 1
            print("You can bunk " + str(bunkable) + " lectures")
