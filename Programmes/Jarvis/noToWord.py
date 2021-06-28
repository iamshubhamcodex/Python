

lis_no = {1:"One", 2:"Two", 3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine", 0:""}
lis_ty = {1:"", 2:"Twenty", 3:"Thirty",4:"Fourty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety",0:""}
lis_hu = [" Hundred", " Thousand"," Lakh"," Crore"," Arab"," Kharab"," Nil"," Paddam"," Sankh"," Mahasankh"]        
lis_el = {1:"Eleven", 2:"Twelve", 3:"Thirteen",4:"Fourteen",5:"Fifteen",6:"Sixteen",7:"Seventeen",8:"Eighteen",9:"Nineteen"}
c = []


# ['Twenty One', 'Thirty Three', 'Fifty Five'] ==> 'Twenty One Crore Thirty Three Lakh Fifty Five Thousand'
def finwor(lis):
    i = len(lis)
    j = 0
    finstr = ""
    while j < len(lis):
        lis[j] = lis[j] + lis_hu[i]
        finstr = finstr + lis[j] + " "
        i -= 1
        j += 1
    return finstr

# [2,1] ==> 'Twenty One' / [5] ==> 'Five'
def worT(lis):
    if len(lis) == 1:
        lis[0] = lis_no[lis[0]]
        strwoT = lis[0]    
    else:
        if lis[0] == 1:
            lis[0] = lis_el[lis[1]]
            lis.pop()
            strwoT = lis[0]
        else:
            lis[0] = lis_ty[lis[0]]
            lis[1] = lis_no[lis[1]]
            strwoT = lis[0] + " " + lis[1]
    return strwoT

# [2,1,4] ==> 'Two Hundred Fourteen' 
def worLT(lis):
    lis[0] = lis_no[lis[0]] + lis_hu[0]
    lis_d = [lis[1], lis[2]]
    ret_lis_d = worT(lis_d)
    lis.pop()
    lis[1] = ret_lis_d
    strwoLt = lis[0] + " " + lis[1]
    return strwoLt

# Getting WORD from Number (Actual Number)[4,2,4,5,7,8,6,9]
def Word(lis):
    
    if 0 < len(lis) < 4:
        if len(lis) == 3:
            print(worLT(lis))
        else:
            print(worT(lis))
    else:
        leng = len(lis) - 1
        n_lis = []
        for _ in range(3):
            n_lis.append(lis[leng])         #[9,6,8] ==> n_lis
            lis.pop()
            leng = leng - 1             #lis ==> [4,2,4,5,7]
        n_lis.reverse()         #[8,6,9] ==> n_lis
        last_word = worLT(n_lis)
        lis.reverse()           #[7,5,4,2,4]
        o  = 0
        word_lis = []
        while o < len(lis): 
            dep_lis = []            
            if o % 2 == 0:  
                dep_lis.append(lis[o])              #[7,5]  [4,2]  [4] ==> each time dep_lis
                try:
                    dep_lis.append(lis[o + 1])
                except:
                    pass                    
                dep_lis.reverse()                   #[5,7]  [2,4] [4]
                lim_word = worT(dep_lis)        #'Fifty Seven'  'Twenty Four'  'Four'
                word_lis.append(lim_word)       # ['Fifty Seven','Twenty Four','Four'] ==> word_lis
            
            o = o + 1
        word_lis.reverse()                  # ['Four','Twenty Four','Fifty Seven'] ==> word_lis
        lastt = finwor(word_lis)            # 'Four Crore Twenty Four Lakh Fifty Seven Thousand'
        
        lastt = lastt + last_word          # 'Four Crore Twenty Four Lakh Fifty Seven Thousand Eight Hundred Sixty Nine' ==> word_lis
    
        print(lastt)

#Taking User Input
def UserInp():
    userNo = input("Enter a number\t")
    list_of_no = list(userNo)
    if len(list_of_no) > 21:
        print("Sorry I can count up to MAHASANKHA only (that is 21 ZEROES after 1)")
    else:
        for i in range(len(list_of_no)):
            list_of_no[i] = int(list_of_no[i])
        Word(list_of_no)

if __name__ == "__main__":
    UserInp()
