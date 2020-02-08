import random
import sys
#set the 3 hands
#variables
#using deck position to keep track of cards instead of removing
#Some global variables
d = []
p = []
deck=["A", "A", "A", "A", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
game_counter = deck_pos = hand_value = playerstatus = pvalue = 0
total_count = win_count = win_percent = 0
print("Welcome to Blackjack!")
print("the goal of game is to draw cards that total as close to 21 as possible without")
print("going over(called a bust). All face cards count as 10 points,")
print("while aces can count as 1 or 11. Good luck!\n")

def main():
    global game_counter, total_count
    shuffleCards()
    game_counter = 0
    while game_counter < 6:
        initializeRound()
        player()
        dealer()
        game_counter = game_counter + 1
        total_count = total_count + 1
        win_percent = win_count / total_count * 100
        win_round = round(win_percent,2)
        print("You have played ", total_count, "games and your win count is: ", win_count)
        print("Your current win percentage is : ", win_round,"%")
    print("6 Rounds finished. Reshuffling deck!\n")
    main()
    
#FUNCTIONS NEEDED
#deck shuffling function
def shuffleCards():
    global deck, deck_pos
    random.shuffle(deck)
    deck_pos = 0

#check the value of the hands
def check_values(hand):
    sum_hand = 0
    x = len(hand)
    for i in range (0,x):
        if(hand[i] == "J" or hand[i] == "Q" or hand[i] == "K"):
            sum_hand = sum_hand + 10
        elif(hand[i] == "A" and sum_hand > 10):
            sum_hand = sum_hand + 1
        elif(hand[i] == "A" and sum_hand <= 10):
            sum_hand = sum_hand + 11
        else:
            sum_hand = sum_hand + int(hand[i])
    return sum_hand

#deals another card to the player or dealer
def deal(hand):
    global deck_pos, deck
    hand.append(deck[deck_pos])
    deck_pos = deck_pos + 1

#Checker to deal with soft 17 
def check_soft(dealer_hand):
    is_soft = 0
    dsize = len(dealer_hand)
    for x in range (0,dsize):
        if(dealer_hand[x] == "A"):
            is_soft = 1
        else:
            is_soft = 0
    return is_soft

#Start the round out
def initializeRound():
    global deck, deck_pos, p, d
    p = []
    d = []
    p.append(deck[deck_pos])
    print("Dealer deals your 1st card: ", p[0])
    d.append(deck[deck_pos+1])
    print("Dealer deals his 1st card: ", d[0])
    p.append(deck[deck_pos+2])
    print("Dealer deals your 2nd card: ", p[1])
    d.append(deck[deck_pos+3])
    #keep dealer 2nd card hidden 
    deck_pos = deck_pos + 4
    print("Dealer deals his 2nd card")


#PLAYER then DEALER turns
def player():
    global p
    pstatus = 0
    while pstatus < 1:
        pvalue = check_values(p)
        print("Your current hand consists of: ", *p)
        if pvalue == 21:
            print("Blackjack! let's see what the dealer has")
            pstatus = 1
        elif pvalue > 21:
            print("You're hand is over 21 it's a bust, you lose\n")
            pstatus = 2
        else:
            ans = input("Hit(H) or Stand(S)")
            if ans == "H":
                deal(p)
            elif ans == "S":
                print("You're keeping your current value of: ", pvalue)
                pstatus = 1
            else:
                print("Enter one of the options")

def dealer():
    global p, d, win_count
    pvalue = check_values(p)
    if pvalue > 21:
        return    
    print("Player has: ", *p, "Value: ", pvalue)
    print("Dealer shows his hidden card")
    while True:
        print("Dealer has: ", *d)
        dvalue = check_values(d)
        print("The value of his hand is: ", dvalue)        
        if dvalue == 21 and pvalue == 21:
            print("It's a tie! \n")
            break
        elif dvalue < 17:
            print("Dealer draws")
            deal(d)
        elif (dvalue == 17 and check_soft(d) == 1):
            print("Dealer draws on Soft 17")
            deal(d)
        else:
            if dvalue > 21:
                print("Dealer busts! You win\n")
                win_count = win_count + 1
                break
            elif pvalue > dvalue:
                print("You won!\n")
                win_count = win_count + 1
                break
            elif pvalue < dvalue:
                print("Dealer won!\n")
                break
            else:
                print("It's a tie! \n")
                break
    return win_count
        
        
if __name__ == "__main__":
    main()