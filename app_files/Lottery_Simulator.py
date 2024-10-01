import random

#Function to initiate the lattery
def start_Lotto():
    #Creates an empty list to store lottery numbers
    winning_numbers = []

    #creates an empty list to store the sets of user inputs
    all_sets = []

    #numbers of sets of numbers
    num_sets = 5

    return winning_numbers, all_sets, num_sets

#Function to start the lottery and draw the numbers
def play_Lotto(winning_numbers, all_sets, num_sets):
        #for loop to create a list with 5 random numbers
        #to be used as the winning set
        for i in range(5):
            lotnum = random.randrange(1, 70)

            # Check if the generated number is already in the list to avoid duplicates
            while lotnum in winning_numbers:
                lotnum = random.randrange(1, 70)
            
            #adds the non-duplicate numbers to the list 
            winning_numbers.append(lotnum)
            i += 1

        #Sorts the list of integers allowing for camparison
        winning_numbers.sort()

        print(winning_numbers)

        #Asks the user to input 5 sets of 5 numbers to guess the lottery
        for set_index in range(num_sets):
            set1 = input(f"Enter a 5 number combination between 1 and 69 for set {set_index + 1}: ")
            atmpts = set1.split(" ")

            # Converts the string list into a list of integers
            int_atmpts = [int(i) for i in atmpts]

            # Sorts the list of integers
            int_atmpts.sort()

            # Appends the sorted list to atmpts
            all_sets.append(int_atmpts)

        # Print each set with its index
        for index, lot_set in enumerate(all_sets):
            print(f"Set {index + 1}: {lot_set}")
        
        return all_sets, winning_numbers

#Function to replay the lottery
def replay_Lotto(all_sets, winning_numbers):
        is_winner = False

        #checks to see if the combination you entered is a winner
        for index, lot_set in enumerate(all_sets):
            if (lot_set == winning_numbers):
                print("You Hit The Jackpot!\n")
                is_winner = True
                break

        # if not, say you lose
        if not is_winner:
            print ("You Lose\n")

        #prompt the user whether they want to play again
        choice = input("Wanna go again? (y or n): ")

        #determines the users input and resets the lists if yes
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False

def main():
    #Resets the game based on the return value
    reset = True

    #plays and replays the game based on the boolean value of reset
    while reset:
        winning_numbers, all_sets, num_sets = start_Lotto()
        all_sets, winning_numbers = play_Lotto(winning_numbers, all_sets, num_sets)
        reset = replay_Lotto(all_sets, winning_numbers)

if __name__ == "__main__":
    main()