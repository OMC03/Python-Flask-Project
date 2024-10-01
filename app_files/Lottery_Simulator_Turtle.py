import random
import turtle

# Setup the turtle screen
screen = turtle.Screen()
screen.title("Lottery Simulator")
screen.setup(width=600, height=400)

# Turtle object to display text
pen = turtle.Turtle()
pen.hideturtle()

def display_message(message, x=0, y=0, font_size=18):
    pen.clear()
    pen.penup()
    pen.goto(x, y)
    pen.write(message, align="center", font=("Arial", font_size, "normal"))

def get_user_input(prompt):
    screen.textinput("Lottery Input", prompt)

# Function to initiate the lottery
def start_lotto():
    winning_numbers = []
    all_sets = []
    num_sets = 5
    return winning_numbers, all_sets, num_sets

# Function to start the lottery and draw the numbers
def play_lotto(winning_numbers, all_sets, num_sets):
    for i in range(5):
        lotnum = random.randrange(1, 70)
        while lotnum in winning_numbers:
            lotnum = random.randrange(1, 70)
        winning_numbers.append(lotnum)
    
    winning_numbers.sort()
    display_message(f"Welcome to the Lottery!", y=100)

    for set_index in range(num_sets):
        set1 = screen.textinput("Lottery Input", f"Enter 5 numbers between 1 and 69 for set {set_index + 1}: ")
        
        if set1 is None:
            display_message("Input was canceled. Exiting game.", y=0)
            return all_sets, winning_numbers

        atmpts = set1.split(" ")

        try:
            int_atmpts = [int(i) for i in atmpts]
            if len(int_atmpts) != 5:
                raise ValueError("You must enter exactly 5 numbers.")
            int_atmpts.sort()
            all_sets.append(int_atmpts)
        except ValueError as e:
            display_message(f"Invalid input: {e}", y=0)
            return all_sets, winning_numbers

    return all_sets, winning_numbers

# Function to replay the lottery
def replay_lotto(all_sets, winning_numbers):
    is_winner = False
    for index, lot_set in enumerate(all_sets):
        if lot_set == winning_numbers:
            display_message("You Hit The Jackpot!", y=-50)
            is_winner = True
            break

    if not is_winner:
        display_message("You Lose", y=-50)

    choice = screen.textinput("Play Again?", "Wanna go again? (y or n): ")
    if choice.lower() == 'y':
        return True
    elif choice.lower() == 'n':
        return False

def reset_game():
    pen.clear()
    return start_lotto()

def main():
    reset = True

    while reset:
        winning_numbers, all_sets, num_sets = start_lotto()
        all_sets, winning_numbers = play_lotto(winning_numbers, all_sets, num_sets)
        reset = replay_lotto(all_sets, winning_numbers)
        if reset:
            winning_numbers, all_sets, num_sets = reset_game()

if __name__ == "__main__":
    main()
    screen.mainloop()  # Keeps the window open
