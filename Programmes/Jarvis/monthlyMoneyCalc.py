def totalMoney():
    amt = float(input("Enter Amount\t"))
    yr = int(input("Enter Year\t")) - 1
    rt = input("Enter Rate in percentage [5% is default]\t")
    sum = 0
    amt_lis = [int(amt + 1)]
    if rt == "":
        rt = 5
    else:
        rt = int(rt)
    for i in range(0, yr-1):
        amt = amt + (amt * 0.05)
        amt_lis.append(int(amt + 1))
    for i in range(len(amt_lis)):
        sum = sum + amt_lis[i]

    print("\nThe total sum is:\t" + str(sum))

if __name__ == "__main__":
    totalMoney()