import random
def playG():
    try:
        b = int(input("Enter max score to win\t"))
        my_score = 0
        comp_score = 0
        while True:
            lis = ["scissor","rock", "paper", "scissor","rock", "paper", "scissor", "rock", "paper", "scissor", "rock", "paper","scissor", "rock", "paper"]
            no = random.randint(0 ,len(lis)-1)
            c = lis[no]
            if my_score >= b or comp_score >= b:
                print(f"Match Finished\n\tYour score is: {comp_score} and computer's score is: {my_score}")
                if my_score > comp_score:
                    print("Computer Wins")
                else:
                    print("You Win")
                b = input("Wanna Play Again (Y or N)\t").lower()
                if b == "y":
                    playG()
                else:
                    break                    
                break
            else:
                a = input("Enter only R[ROCK], S[SCISSOR], P[PAPER], Q[QUITE]\t").lower()
                if a == "s":
                    a = "scissor"
                elif a == "p":
                    a = "paper"
                elif a == "r":
                    a = "rock"
                elif a == "q":
                    break
                else:
                    print("Please enter only R[ROCK], S[SCISSOR], P[PAPER]")
            
                if a == str(c):
                    print("Match Draw")
                elif a == "rock" and c == "scissor":
                    print("You Win")
                    comp_score =  comp_score + 1
                elif a == "rock" and c == "paper":
                    print("Computer Wins")
                    my_score =  my_score + 1
                elif a == "paper" and c == "scissor":
                    print("Computer Wins")
                    my_score =  my_score + 1
                elif a == "paper" and c == "rock":
                    print("You Win")
                    comp_score =  comp_score + 1
                elif a == "scissor" and c == "paper":
                    print("You Win")
                    comp_score =  comp_score + 1
                elif a == "scissor" and c == "rock":
                    print("Computer Wins")
                    my_score =  my_score + 1
    except:
       playG()

if  __name__ == "__main__":    
    playG()

