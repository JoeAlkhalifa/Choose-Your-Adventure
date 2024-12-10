one_piece = [
    ["One Piece - Treasure Hunt Adventure (Enter 1 to start) (Enter 0 to leave game)", 1],
    ["Page 1: You're a pirate on a quest to find the legendary One Piece treasure. The Grand Line is full of dangers. Do you set sail to the Grand Line (Enter 2) or stay on a nearby island to gather more crew (Enter 3)?", 2, 3],
    ["Page 2: You set sail and face a mighty storm. Your ship gets damaged. Do you REPAIR the ship (Enter 4) or continue despite the damage (Enter 5)?", 4, 5],
    ["Page 3: You recruit a powerful new crewmate, but the Marines are hot on your trail. Do you FIGHT them (Enter 6) or ESCAPE (Enter 7)?", 6, 7],
    ["Page 4: You manage to repair the ship, but it takes a long time. The storm subsides and you continue your journey. You arrive at a mysterious island. Do you EXPLORE the island (Enter 8) or leave immediately (Enter 9)?", 8, 9],
    ["Page 5: You continue sailing, but the ship sinks. You're stranded on a deserted island. THE END. (Enter 0)", 0],
    ["Page 6: You fight the Marines, but they call for reinforcements. You're overwhelmed and captured. THE END. (Enter 0)", 0],
    ["Page 7: You manage to escape the Marines, but you lose valuable time. The Grand Line is getting more dangerous. THE END. (Enter 0)", 0],
    ["Page 8: On the island, you discover a hidden map to a secret treasure. But a rival pirate crew arrives! Do you FIGHT them (Enter 10) or BARGAIN with them (Enter 11)?", 10, 11],
    ["Page 9: You leave the island and sail to a new location. The Grand Line is vast and unpredictable. THE END. (Enter 0)", 0],
    ["Page 10: You fight the rival pirates, but they're too strong. Your crew is defeated. THE END. (Enter 0)", 0],
    ["Page 11: You attempt to bargain with the rival pirates, but they betray you and steal the map. You're left stranded. THE END. (Enter 0)", 0]
]

naruto = [
    ["Naruto - Ninja Adventure (Enter 1 to start) (Enter 0 to leave game)", 1],
    ["Page 1: You're a young ninja in the Hidden Leaf Village. You've just graduated from the Ninja Academy! Do you take a mission to deliver a message (Enter 2) or train more (Enter 3)?", 2, 3],
    ["Page 2: You take the mission to deliver a message, but you encounter a rogue ninja! Do you FIGHT (Enter 4) or RUN (Enter 5)?", 4, 5],
    ["Page 3: You decide to train, but while you're practicing, you accidentally damage a village building. The villagers are angry! Do you APOLOGIZE (Enter 6) or ESCAPE (Enter 7)?", 6, 7],
    ["Page 4: You fight the rogue ninja, but he's stronger than you expected. You are injured. THE END. (Enter 0)", 0],
    ["Page 5: You manage to escape, but you lose the message. The mission is a failure. THE END. (Enter 0)", 0],
    ["Page 6: You apologize, and the villagers forgive you. You gain their respect and are ready for your next mission. THE END. (Enter 0)", 0],
    ["Page 7: You run from the village, but you’re caught by the village elders. They strip you of your ninja headband. THE END. (Enter 0)", 0],
    ["Page 8: You face a rival ninja during a mission. Do you choose to FIGHT (Enter 9) or TALK to him (Enter 10)?", 9, 10],
    ["Page 9: You defeat the rival ninja, but you're injured and need help. You head back to the village for treatment. THE END. (Enter 0)", 0],
    ["Page 10: You talk to the rival ninja and convince him to join forces with you. Together, you complete the mission. THE END. (Enter 0)", 0]
]

bleach = [
    ["Bleach - Soul Reaper Adventure (Enter 1 to start) (Enter 0 to leave game)", 1],
    ["Page 1: You're a Soul Reaper in the Soul Society. Your mission is to protect the world of the living from evil spirits. Do you accept a mission to eliminate a Hollow (Enter 2) or report to your Captain (Enter 3)?", 2, 3],
    ["Page 2: You confront the Hollow in a quiet town. It attacks you unexpectedly. Do you FIGHT (Enter 4) or ESCAPE to lure it away (Enter 5)?", 4, 5],
    ["Page 3: You report to your Captain, but he assigns you a tougher task. Do you ACCEPT the task (Enter 6) or ask for more time to prepare (Enter 7)?", 6, 7],
    ["Page 4: You fight the Hollow and defeat it. But its death triggers an even more dangerous spirit to appear. Do you confront it (Enter 8) or RUN (Enter 9)?", 8, 9],
    ["Page 5: You escape to a safer location, but the Hollow escapes with you. It attacks again in the Soul Society. THE END. (Enter 0)", 0],
    ["Page 6: You accept the task, but you encounter a powerful enemy. You have no choice but to fight. Do you use your Bankai (Enter 10) or rely on your regular powers (Enter 11)?", 10, 11],
    ["Page 7: You ask for more time, but your Captain becomes disappointed. He takes away your Soul Reaper duties. THE END. (Enter 0)", 0],
    ["Page 8: You confront the powerful spirit. You fight hard, but it proves too strong. You barely escape with your life. THE END. (Enter 0)", 0],
    ["Page 9: You run, but the spirit follows you and destroys the town. You failed your mission. THE END. (Enter 0)", 0],
    ["Page 10: You use your Bankai and defeat the enemy. Your powers grow stronger, and you protect the Soul Society. THE END. (Enter 0)", 0],
    ["Page 11: You use your regular powers, but the enemy proves too strong. You fail to stop the attack. THE END. (Enter 0)", 0]
]

def cya():
    running = True
    while running:
        print("Welcome to Choose Your Own Adventure. Would you like to play One Piece (Enter 1), Naruto (Enter 2), or Bleach (Enter 3)? (0 to quit)")
        storychoice = int(input("Enter 1, 2, or 3? "))
        while storychoice not in [0, 1, 2, 3]:
            storychoice = int(input("Invalid input. Please enter 0, 1, 2, or 3: "))
        
        if storychoice == 0:
            running = False
        elif storychoice == 1:
            story = one_piece
        elif storychoice == 2:
            story = naruto
        elif storychoice == 3:
            story = bleach
        
        if running:
            selection = story[0]  # Starting page
            game = True
            while game:
                text = selection[0]
                options = selection[1:]
                opt_text = ("Options: " + str(options))
                print(text)
                print("")
                choice = int(input(opt_text))
                
                while choice not in options and choice != 0:
                    choice = int(input("Invalid, " + opt_text))
                    print("1")
                
                if choice in options:
                    selection = story[choice]
                elif choice == 0:
                    game = False
    
    print("Thanks for playing Choose Your Own Adventure")
cya()
