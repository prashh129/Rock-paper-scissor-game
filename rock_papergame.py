import random

choice={1:"Rock",2:"Paper",3:"Scissor"}
valid_input={"rock":1,"paper":2,"scissor":3,"1":1,"2":2,"3":3}

def get_winner(player,computer):
    if player==computer:
        print("It's a Draw\n")
    elif (player,computer) in [(1,3),(2,1),(3,2)]:
        print("Player Won!\n")
    else:
        print("Player lose!\n")

while True:
    print("\nRock Paper and Scissor Game")
    for num,text in choice.items():
        print(f"{num}.{text}")

    try:
        ans=input("Enter your choice:").lower().strip()
        if ans not in valid_input:
            print("\nPlease choose between Rock, Paper or Scissor or (1-3) \n")
            continue
            
        computer_choice=random.choice(list(choice.keys()))
        player_choice=valid_input[ans]
        print(f"\nPlayer:{choice[player_choice]}")
        print(f"Computer:{choice[computer_choice]}")
        get_winner(player_choice,computer_choice)

    except ValueError:
        print ("Invalid input! Please enter a valid chocie.")
        continue
    
    play_again=input("Do you want to play again(y/n):").lower().strip()
    if play_again != "y":
        print("Thank you for playing!!!")
        break
        


