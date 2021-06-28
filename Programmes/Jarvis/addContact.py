def addCon():
    while True:
        name = input("Enter name\t")
        if name == "":
            break

        exist = False

        with open("con_dic.txt", "r+") as f:
            all_con = f.readlines()
        for i in range(len(all_con)):
            conc = all_con[i].split(":")
            if conc[0] == name:
                print("Contact Already Exists")
                exist = True
                break
        if not exist:
            enter_num = input("Enter the Number\t")
            if enter_num == "":
                addCon()
            with open("con_dic.txt", 'a') as f:
                f.write(str(name) + ":" + str(enter_num) + "\n")
            print("Name Added",end="\n\n")


if __name__ == "__main__":
    addCon()