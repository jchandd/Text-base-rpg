# Introduce user to game title
print("Welcome to Last Hope Of Earth!")

# Ask user for their name
name = input("What is your first name? ")
print(f"Hey {name}! Welcome to Last Hope Of Earth.\n")

# Start Story
print("You wake up groggy and sore from your shift in the coal mines.\nYou had to work overtime because there weren’t enough workers.")
print("Decision 1. [S]kip work today and report ill")
print("Decision 1. [G]et in your car and muscle through the exhaustion")

ans1 = input("Choice:\n").lower().strip()

if ans1 == "s":
    print("\nYou choose to stay home. On the radio, you hear reports of brutal Resistance fighting against a Hive convoy with heavy human casualties.")
    print("You're hungry and want to make breakfast to shake off the exhaustion,\n but you’re missing ingredients.")
    print("Decision 2. [L]ook in the higher cupboards for ingredients")
    print("Decision 2. [G]o to the Deli to get ingredients for breakfast")

    ans2 = input("Choice:\n").lower().strip()
    
    if ans2 == "l":
        print("\nYou pull up a chair and climb up to check the high cupboards.")
        print("Unfortunately, you lose your balance, fall, and suffer a fatal head injury on the counter.\nYou Die.")
        
    elif ans2 == "g":
        print("\nAs you're driving to the Deli you stick to local roads and reach there, you bump into someone on the way out and they drop something")
        print("Decision 3.[P]ick up the box and keep it.")
        print("Decision 3.P[I]ck up the box and return it to its owner")
        
        ans3 = input("Choice:\n").lower().strip()
        # good choice here
        if ans3 == "i":
            print("You pick up the box and call to the hooded stranger and when they turn and see what's in your hand the stranger then grabs you by the hand and pulls you into an alley,\n “What are you doing?” hissed the stranger at you, you explain that she dropped the box and you were simply returning it.\n She tells you that there's no time to explain and you have to follow her.")
            print("Decision 4. [G]o back to your car")
            print("Decision 4. [F]ollow her")
            
            ans4 = input("Choice:\n").lower().strip()
            
            if ans4 == "g":
                print("You decide that this is probably some hoax so that she can rob you, so you make an excuse and while walking back to your car, Hive Troops point at you and open fire.\n You Die")
                
            elif ans4 == "f":
                print("You look into the woman's eyes and realize she is genuinely worried so you agree to follow her.\n She takes you to a dead end and then presses a series of bricks which gives way to a hideout,\n the woman then tells you that she and her team is looking for new recruits.")
                print("Decision 5. [T]ell her you'll join.")
                print("Decision 5. [R]eject her offer")
                
            
            
            
            
            
        # bad choice
        elif ans3 == "p":
            print("You pick up the box and wait for the person to leave,\n as you exit the Deli you notice the infamous Hive insignia on it. As you try and decide what to do with it you are then knocked out by a soldier.\n You are taken to a prison where you get tortured and killed for info on the box.\n You Die.")

            
            
            
           
        elif ans2 == "p":
            print("You pick up the box and wait for the person to leave, as you exit the Deli you notice the infamous Hive insignia on it.\n As you try and decide what to do with it you are then knocked out by a soldier. You are taken to a prison where you get tortured and killed for info on the box.\nYou Die")
   
   
   


elif ans1 == "g":
    print("\nYou force yourself into the car and head to work, fighting through the exhaustion...You fall asleep and die in a crash.\n Game Over")


else:
    print("\nThat is not one of the choices.\nGame Over.")
