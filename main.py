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
            print("You pick up the box and call to the hooded stranger and when they turn\n and see what's in your hand\n the stranger then grabs you by the hand and pulls you into an alley,\n “What are you doing?” hissed the stranger at you, you explain that\n she dropped the box and you were simply returning it.\n She tells you that there's no time to explain and you have to follow her.")
            print("Decision 4. [G]o back to your car")
            print("Decision 4. [F]ollow her")
            
            ans4 = input("Choice:\n").lower().strip()
            
            if ans4 == "g":
                print("You decide that this is probably some hoax so that she can rob you, so you make an excuse and while walking back to your car, Hive Troops point at you and open fire.\n You Die")
                
            elif ans4 == "f":
                print("You look into the woman's eyes and realize she is genuinely\n worried so you agree to follow her.\n She takes you to a dead end and then presses a series of bricks which gives way to a hideout,\n the woman then tells you that she and her team is looking for new recruits.")
                print("Decision 5. [T]ell her you'll join.")
                print("Decision 5. [R]eject her offer")
                
                ans5 = input("Choice:\n").lower().strip()
                
                if ans5 == "t":
                    print("You tell her that you are willing to join her and help to stop the Hive,\n she then gives you a blaster pistol and\n a Resistance badge to show other members when you see them.\n You then are instructed to drive a car to a remote location almost\n a day and a half worth of driving,\n but you become low on gas...")
                    print("Decision 6. [K]eep driving on the highway")
                    print("Decision 6. [T]ry and find a gas station")
                    
                    ans6 = input("Choice:\n").lower().strip()
                    
                    if ans6 == "k":
                        print("You continue driving, ignoring the warning,\n your tank runs out in the middle of the highway and a semi truck\n from behind crushes you and your car.\n You Die")
                        
                    elif ans6 == "t":
                        print("You get off the highway and after a few miles see a gas station,\n you fill your tank and continue driving, after a few hours\n you’ve reached your destination and the\n same woman from before is waiting for you, you go up to her\n and she hands you a pair of  binoculars, you are told to wait for the signal\n as the woman slides down.")
                        print("Decision 7. [T]rust your gut and go down to the outpost")
                        print("Decision 7. [S]tay on the cliff and wait for the signal")
                        
                        ans7 = input("Choice:\n").lower().strip()
                        
                        if ans7 == "t":
                            print("You slide down to the outpost and sneak past the cards,\n while hiding behind a transport, out of the corner of your eye you notice a cluster of explosives and are blown into many pieces around the ground.\nYou Die")
                            
                        elif ans7 == "s":
                            print("You wait on the cliff and all of a sudden hear explosions and gunfire as the other rebel team engages the troops,\n you see a bright flare in the sky and slide down to the outpost.")
                            print("Decision 8. [I]gnore the fight and continue to the power room")
                            print("Decision 8. [H]elp the other rebels and join the fight")
                            
                            ans8 = input("Choice:\n").lower().strip()
                            
                            if ans8 == "i":
                                print("You remember what your true objective is and sneak through\n the rear of the gunfight, crawling into a vent to enter the power room,\n You push through and then fall from the top of the room\n straight into the Core room, You go to the Core and then see a ray shield around the core.\n You pull out a piece of floor holding the wiring for the ray shield,\n the box that was stolen held the information on how to decipher their language,\n and once you attach it to the wiring box it gives you a choice...\n between a red wire or a black wire.")
                                print("Decision 9.  Cut the [R]ed wire")
                                print("Decision 9. Cut the [B]lack wire")
                                
                                ans9 = input("Choice:\n").lower().strip()
                                
                                if ans9 == "r":
                                    print(" You cut the red wire which causes a self-destruct sequence because of\n tampering and you are incinerated in the room.\n You Die")
                                    
                                elif ans9 == "b":
                                    print("You cut the black wire and the ray shield fades away,\n you attach the explosives to the Core room and as you exit the building you see the rebels waiting in speeders,\n as you get in one you press the detonator and the outpost is blown up, You Win!!")
                                
                                
                                
                            elif ans8 == "h":
                                print("You Feel an anger burning in you seeing fellow Resistance members dying and join the battle,\n you hear the rumbling of engines and are disintegrated by Hive Hyperjets.\n You Die")


                    
                elif ans5 == "r":
                    print("You tell her that you can’t, you see the Deli is badly damaged\n but your car is intact so you drive it home, as you enter your house,\n a guard knocks you out, you are taken to a prison and die there.\n You Die")
                
            
            
            
            
            
        # bad choice
        elif ans3 == "p":
            print("You pick up the box and wait for the person to leave,\n as you exit the Deli you notice the infamous Hive insignia on it. As you try and decide what to do with it you are then knocked out by a soldier.\n You are taken to a prison where you get tortured and killed for info on the box.\n You Die.")

            
            
            
           
        elif ans2 == "p":
            print("You pick up the box and wait for the person to leave, as you exit the Deli you notice the infamous Hive insignia on it.\n As you try and decide what to do with it you are then knocked out by a soldier. You are taken to a prison where you get tortured and killed for info on the box.\nYou Die")
   
   
   


elif ans1 == "g":
    print("\nYou force yourself into the car and head to work, fighting through the exhaustion...You fall asleep and die in a crash.\n Game Over")


else:
    print("\nThat is not one of the choices.\nGame Over.")
