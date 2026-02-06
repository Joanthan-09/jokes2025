


# # make this performance task ready for submission
# # To give the user a fun experience hearing knock knock jokes

# joke = input("Do you want to hear a joke? ")
# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")



# Jonathan Modesto & Christian Garcia 
        

import random


#  DATA STORAGE 
# A list of tuples, where each tuple is (Title, Setup, Punchline)

joke_list = [
    ("Robbers", "Calder", "Calder police - I've been robbed!"),
    ("Tanks", "Tank", "You are welcome!"),
    ("Pencils", "Broken pencil", "Nevermind, it's pointless!")
]

# FUNCTION DEFINITION 

def tell_joke(joke_tuple):
#   Prints a structured knock-knock joke with pauses
    print(f"\n--- {joke_tuple[0]} Joke ---")
    input("Knock Knock. (Press Enter) ")
    input("Who's there? (Press Enter) ")
    input(f"{joke_tuple[1]}! (Press Enter) ")
    input(f"{joke_tuple[1]} who? (Press Enter) ")
    print(f"{joke_tuple[2]}")
    print("-------------------------")

    # MAIN GAME LOOP
print("Welcome to the Interactive Joke Teller!")

playing = True    # Flag to keep the game running
while playing: 
        # Ask user to play, convert to lowercase to handle 'Yes' or 'yes'
    choice = input("\nDo you want to hear a joke? (yes/no): ").lower()

    if choice == "yes":            # Select and play a random joke
        selected_joke = random.choice(joke_list)
        tell_joke(selected_joke)
        
        # Ask if they want another
        more = input("Want another joke? (yes/no): ").lower()
        if more != "yes":
            playing = True   # Continue loop
    else:
        print("Okay, suit yourself!")
        playing = False    # Exit loop

#   CLOSING & RATING 

print("\nThanks for playing!")
rate = input("Please rate our game 1-10: ")
rate = int(rate)     # Convert input string to integer
        # Conditional for rating
if rate <= 4 :
    print(f" You rated us {rate}/10, Appericate the critism...")
elif rate <= 6 :
    print(f" You rated us {rate}/10, we'll do better next time.")
else:
    print(f"Thanks! You rated us {rate}/10.")

