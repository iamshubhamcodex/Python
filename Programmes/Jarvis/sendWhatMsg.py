def sendWhatsapp(): 
    import pywhatkit as kit
    no1 = ""
    print("Enter NEGATIVE HOUR to send msg NOW\n")
    sent = False
    name = input("Enter name\t")
    with open("con_dic.txt", "r+") as f:
        all_con = f.readlines()
    if name == "list":
        for i in range(len(all_con)-1):
            print(str(i) + "\t" + all_con[i], end="")
        no1 = all_con[int(input("Enter Name or Serial Number\t"))].split(":")[1]
        kit.sendwhatmsg(no1, input("Enter Messege:\t"), int(input("Hour[24]:\t")), int(input("Minutes:\t")))
    else:
        for i in range(len(all_con)):
            conc = all_con[i].split(":")
            if conc[0] == name:
                no1 = conc[1].replace("\n", "")
                kit.sendwhatmsg(no1, input("Enter Messege:\t"), int(input("Hour[24]:\t")), int(input("Minutes:\t")))
                sent = True
                break
        if not sent and input("Want to add this name[Y]\t").lower() == "y":
            enter_num = input("Enter the Number\t")
            with open("con_dic.txt", 'a') as f:
                f.write(str(name) + ":" + str(enter_num) + "\n")
            print("Name Added \t Send Again",end="\n\n")
            sendWhatsapp()

if __name__ == "__main__":
    sendWhatsapp()