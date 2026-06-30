# ==========================================
# 🌸 Beyond the Plains 🌸
# v0.1 — The Flowery Plains
#
# Created: June 29, 2026
# Developer: Sharanya the Great 😎
# ==========================================


print("Welcome, adventurer! ⚔️ 🌟")
username = input("What should the villagers call you? 🤔 : ")

print("Welcome,", username, "!")
backpack = []
coins = 0

print("A cool breeze caresses your face, carrying the crisp scent of the roses. 🥀")
print("Bees buzz noisily as sheep and horses frolick around, the cows munching grass. 🐎")
print("As you squint into the distance of the color drenched meadow, you spot a village, thin tendrils of smoke curling around the chimneys-")

print("'Hiya! I'm Professor Goblin! I'm your world guide! Oh, do ya want some potatoes?'")
print("'Anyways, if ya see anything that looks colorful, pretty or tasty, feel free to keep it!'")
print("'So, what do ya want to do?'")
print("1. Explore the meadow 🌸 \n2. Visit the village 🏡")

activity = input("What do you want to do? : ").lower()

if activity == "explore meadow" :
    print("You might find flowers...🌼")
    print("You might find some feathers...✨")
    print("You may also discover honey! 🍯")
    print("Go collect them!")
    print("🌼 A startlingly blue flower catches your eye as it sways gently in the breeze.")
    print("'Ooh...That looks tasty...if ya don't want it... can I have a bite?'")

    collect_flower = input("Do you want to collect a flower? : ").lower()
    if collect_flower == "yes" :
        pick_flower = input("Do you want to pick it up? : ").lower()
        if pick_flower == "yes" :
            backpack.append("flower")
            print("🌼 Flower added to backpack!")
        elif pick_flower == "no" :
            print("The flower stays in the meadow. Your goblin guide might eat it. If that happens, you can always find another flower elsewhere.")
        else :
            print("Invalid input. Please try again.")
            while pick_flower != "yes" and pick_flower != "no" :
                pick_flower = input("Do you want to pick it up? : ").lower()
                if pick_flower == "yes" :
                    backpack.append("flower")
                    print("🌼 Flower added to backpack!")
                elif pick_flower == "no" :
                    print("The flower stays in the meadow. Your goblin guide might eat it. If that happens, you can always find another flower elsewhere.")

    elif collect_flower == "no" :
        print("'Okay! You could collect it though, ya know. I've never tried eating a potato with a flower.'")
    else :
        print("Invalid input. Please try again.")
        while collect_flower != "yes" and collect_flower != "no" :      # theres alot of duplicate code. fix later when learned functions
            collect_flower = input("Do you want to collect a flower? : ").lower()
            if collect_flower == "yes" :
                pick_flower = input("Do you want to pick it up? : ").lower()
                if pick_flower == "yes" :
                    backpack.append("flower")
                    print("🌼 Flower added to backpack!")
            elif collect_flower == "no" :
                print("The flower stays in the meadow. Your goblin guide might eat it. If that happens, you can always find another flower elsewhere.")
            else :
                print("Invalid input. Please try again.")
                while collect_flower != "yes" and collect_flower != "no" :
                    pick_flower = input("Do you want to pick it up? : ").lower()
                    if pick_flower == "yes" :
                        backpack.append("flower")
                        print("🌼 Flower added to backpack!")
                    elif pick_flower == "no" :
                        print("The flower stays in the meadow. Your goblin guide might eat it. If that happens, you can always find another flower elsewhere.")

    print("You wander around a bit farther, Professor Goblin chatting and munching beside you...")
    print("A beautiful feather drifts gently into your path.")
    print("'Oh look! A feather! Do ya want to collect it?'")

    collect_feather = input("Do you want to collect that feather? : ").lower()

    if collect_feather == "yes" :
        pick_feather = input("Do you want to pick it up? : ").lower()
        if pick_feather == "yes" :
            backpack.append("feather")
            print("✨Feather added to backpack!")
        elif pick_feather == "no" :
            print("The feather stays in the meadow. Your goblin guide might eat it. If that happens, you can always find another feather elsewhere.")
        else :
            print("Invalid input. Please try again.")
            while pick_feather != "yes" and pick_feather != "no" :
                pick_feather = input("Do you want to pick it up? : ").lower()
                if pick_feather == "yes" :
                    backpack.append("feather")
                    print("✨Feather added to backpack!")
                elif pick_feather == "no" :
                    print("The feather stays in the meadow. Your goblin guide might eat it. If that happens, you can always find another feather elsewhere.")

    elif collect_feather == "no" :
        print("'Okay!' (Casually eats feather)")
        print("You stare at him in complete disbelief, shake your head, and then contiue walking.")
    else :
        print("Invalid input. Please try again.")
        while collect_feather != "yes" and collect_feather != "no" :
            collect_feather = input("Do you want to pick it up? : ").lower()
        if collect_feather == "yes" :
            pick_feather = input("Do you want to pick up the feather? : ").lower()
            if pick_feather == "yes" :
                backpack.append("feather")
                print("✨Feather added to backpack!")
        elif collect_feather == "no" :
            print("The feather stays in the meadow. Your goblin guide might eat it. If that happens, you can always find another feather elsewhere.")
        else :
            print("Invalid input. Please try again.")
            while collect_feather != "yes" and collect_feather != "no" :
                pick_feather = input("Do you want to pick it up? : ").lower()
                if pick_feather == "yes" :
                    backpack.append("feather")
                    print("✨Feather added to backpack!")
                elif pick_feather == "no" :
                    print("The feather stays in the meadow. Your goblin guide might eat it. If that happens, you can always find another feather elsewhere.")

    print("Your backpack currently has", len(backpack), "items in it.")
    print("Your backpack contains :", backpack)

    print("Buzz...")
    print("'Wait...", username, ". 'Don't move...'")    # learn f strings for cleaner lines
    print("You and Professor Goblin spot a bee.")
    print("'It looks very protective...'")
    print("Do you still want to collect some honey?")

    collect_honey = input("Do you want to collect honey? : ").lower()

    if collect_honey == "yes" :
        print("Professor Goblin excitedly hands you an empty bottle.")
        print("You carefully collect the honey.")
        print("You have now collected honey in a bottle provided by Professor Goblin.")
        backpack.append("honey")
    elif collect_honey == "no" :
        print("You leave the bee alone.")
        print("Quick! Call Professor Goblin back! He has wandered off trying to convince a bee to trade honey for potatoes!")
    else :
        print("Invalid input. Please try again.")
        while collect_honey != "yes" and collect_honey != "no" :
            collect_honey = input("Do you want to collect honey? : ").lower()
            if collect_honey == "yes" :
                print("You have now collected honey in a bottle provided by Professor Goblin.")
                backpack.append("honey")
            elif collect_honey == "no" :
                print("You leave the bee alone.")
                print("Quick! Call Professor Goblin back! He has wandered off trying to convince a bee to trade honey for potatoes!")

    print("You and Professor Goblin continue wandering around the peaceful land.")
    print("You listen to the hum of nature, interrupted by the goblin's continuous sounds of chewing potato.")
    print("Something falls off the tree you both were standing under, bonking Professor Goblin on the head.")
    print("'Ow! Hey, look! An apple! You must be hungry. Collect it!'")

    collect_apple = input("Do you want to collect that apple? : ").lower()

    if collect_apple == "yes" :
        pick_apple = input("Do you want to pick up the apple : ").lower()
        if pick_apple == "yes" :
            backpack.append("apple")
            print("🍎 Apple added to backpack!")
        elif pick_apple == "no" :
            print("The apple stays in the meadow. Your goblin guide might try to make mashed apple-and-potato salad. Do not eat it. If this happens, try to find another apple elsewhere.")
        else :
            print("Invalid input. Please try again.")
            while pick_apple != "yes" and pick_apple != "no" :
                pick_apple = input("Do you want to pick the apple up? : ").lower()
                if pick_apple == "yes" :
                    backpack.append("apple")
                    print("🍎 Apple added to backpack!")
                elif pick_apple == "no" :
                    print("The apple stays in the meadow. Your goblin guide might try to make mashed apple-and-potato salad. Do not eat it. If this happens, try to find another apple elsewhere.")
    elif collect_apple == "no" :
        print("(Goblin grins and sits down to make some apple-and-potato salad)")
    else :
        print("Invalid input. Please try again.")
        while collect_apple != "yes" and collect_apple != "no" :
            collect_apple = input("Do you want to pick the apple up? : ").lower()
        if collect_apple == "yes" :
            pick_apple = input("Do you want to pick up the apple? : ").lower()
            if pick_apple == "yes" :
                backpack.append("apple")
                print("🍎 Apple added to backpack!")
        elif collect_apple == "no" :
            print("The apple stays in the meadow. Your goblin guide might try to make mashed apple-and-potato salad. Do not eat it. If this happens, try to find another apple elsewhere.")
        else :
            print("Invalid input. Please try again.")
            while collect_apple != "yes" and collect_apple != "no" :
                pick_apple = input("Do you want to pick the apple up? : ").lower()
                if pick_apple == "yes" :
                    backpack.append("apple")
                    print("🍎 Apple added to backpack!")
                elif pick_apple == "no" :
                    print("The apple stays in the meadow. Your goblin guide might try to make mashed apple-and-potato salad. Do not eat it. If this happens, try to find another apple elsewhere.")
    print("Your backpack currently has", len(backpack), "items in it.")
    print("Your backpack contains :", backpack)

    print("Professor Goblin smiles proudly.")
    print("'See? I told ya adventures are just walking around until nature throws snacks at ya.'")

elif activity == "visit village" :
    print("You will miss those pretty items...for now.")
    print("Anyways...to the village!")

    print("As you enter the village, it is bustling with life.")
    print("Villagers wave as children chase chickens through the streets.")
    print("You glance away for only a second...")
    print("Professor Goblin is gone.")
    print("'...Where did he go now?'")
    print("You find him attempting to trade a potato for more potatoes.")
    print("Deciding this is no longer your problem, you quietly back away. \nWhat do you want to do?")
    print("1. Visit the blacksmith ⚒️ \n2. Visit the farmer 🌾 \n3. Visit the florist 🌼 \n4. Go to Professor Goblin 🥔")

    visit = input("Whom do you want to visit? : ").lower()
    if visit == "blacksmith" :
        print("The grindstone screeches as the blacksmith sharpens the sword.")
        print("The blacksmith wipes sweat from his forehead.")
        print("I'm a bit busy. Come back later, please.")
        print("He proceeds to give his diamond sword a terracotta handle. You eyebrows rise, and you back out of the blacksmith's.")
    elif visit == "farmer" :
        print("As you reach the farm, the farmer smiles. 'Hey there!'")
        print("'We have fresh carrots and wheat. 2 carrots for a feather.'")
        print("'Oh! I think i have a feather. Just give me a moment.' You check your backpack.")
        print(backpack)
        if "feather" in backpack :
            print("'Here! a feather.'")
            print("The farmer gives you two fresh carrots, takes the feather, smiles and and waves goodbye as you leave.")
            backpack.remove("feather")
            backpack.append("carrot")
            backpack.append("carrot")
            print("You have", len(backpack), "items in your inventory.")
        elif "feather" not in backpack :
            print("'Sorry! I don't have a feather on me right now. I'll try to get one, and come back later. Bye!'")
            print("The farmer smiles and waves. 'That's okay. Goodbye!'")
    elif visit == "florist" :
        print("'Hey there! Do you have any flowers on you? I can give you 5 coins for 1 flower!'")
        if "flower" in backpack :
            sell_flower = input("do you want to sell your flower for 5 coins in return? : ").lower()
            if sell_flower == "yes" :
                print("'Yeah! I have a flower. Here!' You hand the flower over to the florist.")
                print("'Oh, wow! This flower is beautiful! Here, here's 5 coins.' She drops the coins into your hand, which you put into your pocket.")
                backpack.remove("flower")
                coins = coins + 5
                print("'Thank you! See you later!'")
                print("You have", coins, "coins.")
            elif sell_flower == "no" :
                print("'Sorry! I'm not willing to sell my flower.'")
                print("'Oh! That's alright! See you later!' She waves as you exit her store.")
            else :
                print("Invalid input. Please try again.")
                while sell_flower != "yes" and sell_flower != "no" :
                    sell_flower = input("do you want to sell your flower for 5 coins in return? : ").lower()
                    if sell_flower == "yes" :
                        print("'Yeah! I have a flower. Here!' You hand the flower over to the florist.")
                        print("'Oh, wow! This flower is beautiful! Here, here's 5 coins.' She drops the coins into your hand, which you put into your pocket.")
                        coins = coins + 5
                        print("'Thank you! See you later!'")
                    elif sell_flower == "no" :
                        print("'Sorry! I'm not willing to sell my flower.'")
                        print("'Oh! That's alright! See you later!' She waves as you exit her store.")
        elif "flower" not in backpack :
            print("'Sorry! I don't have a flower right now! If I get one, I'll be sure to come back here!'")
            print("'Oh! That's okay! See you later!'")
    elif visit == "professor goblin" :
        print("'Hey, Professor Goblin! What do you have here?'")
        print("'Sup',", username, "! I have a potato farm here. You can buy one potato for 2! Isn't that a great bargain?!'")
        print("'Err...Professor? That's not how bargaining works.'")
        print("'You know what? Never mind.'")
        print("'I'll give you three coins for 3 potatoes.'")
        print("'Coins? What's that? Ain't potatoes a universal currency?'")
        print("'No! Coins are! Here, take 3 coins!'")
        print("'Ya sure?' He give you a bombastic sideye as he hands you 3 potatoes. 'Yep, I'm sure!'")
        print("You let out a long-suffering sigh when Professor Goblin sits down right on his potatoes and starts eating a poisonous potato.")
        print("'No professor! Don't eat that! It's bad for you!'")
        print("You snatch away the potato, and leave him to mourn the loss of his poisonous potato as you wander around the village.")
        coins = coins - 3
        print("You have", coins, "coins.")
        print("You have", len(backpack), "items in your inventory.")
    else :
        print("Invalid input. Please try again.")
        while visit != "blacksmith" and visit != "farmer" and visit != "florist" and visit != "professor goblin" :
            visit = input("Whom do you want to visit? : ").lower()
            if visit == "blacksmith" :
                print("The grindstone screeches as the blacksmith sharpens the sword.")
                print("The blacksmith wipes sweat from his forehead.")
                print("I'm a bit busy. Come back later, please.")
                print("He proceeds to give his diamond sword a terracotta handle. You eyebrows rise, and you back out of the blacksmith's.")
            elif visit == "farmer" :
                print("As you reach the farm, the farmer smiles. 'Hey there!'")
                print("'We have fresh carrots and wheat. 2 carrots for a feather.'")
                print("'Oh! I think i have a feather. Just give me a moment.' You check your backpack.")
                print(backpack)
                if "feather" in backpack :
                    print("'Here! a feather.'")
                    print("The farmer gives you two fresh carrots, takes the feather, smiles and and waves goodbye as you leave.")
                    backpack.remove("feather")
                    backpack.append("2 carrots")
                elif "feather" not in backpack :
                    print("'Sorry! I don't have a feather on me right now. I'll try to get one, and come back later. Bye!'")
                    print("The farmer smiles and waves. 'That's okay. Goodbye!'")
            elif visit == "florist" :
                print("'Hey there! Do you have any flowers on you? I can give you 5 coins for 1 flower!'")
                if "flower" in backpack :
                    sell_flower = input("do you want to sell your flower for 5 coins in return? : ").lower()
                    if sell_flower == "yes" :
                        print("'Yeah! I have a flower. Here!' You hand the flower over to the florist.")
                        print("'Oh, wow! This flower is beautiful! Here, here's 5 coins.' She drops the coins into your hand, which you put into your pocket.")
                        coins = coins + 5
                        backpack.remove("flower")
                        print("'Thank you! See you later!'")
                    elif sell_flower == "no" :
                        print("'Sorry! I'm not willing to sell my flower.'")
                        print("'Oh! That's alright! See you later!' She waves as you exit her store.")
                    else :
                        print("Invalid input. Please try again.")
                        while sell_flower != "yes" and sell_flower != "no" :
                            sell_flower = input("do you want to sell your flower for 5 coins in return? : ").lower()
                            if sell_flower == "yes" :
                                print("'Yeah! I have a flower. Here!' You hand the flower over to the florist.")
                                print("'Oh, wow! This flower is beautiful! Here, here's 5 coins.' She drops the coins into your hand, which you put into your pocket.")
                                coins = coins + 5
                                print("'Thank you! See you later!'")
                            elif sell_flower == "no" :
                                print("'Sorry! I'm not willing to sell my flower.'")
                                print("'Oh! That's alright! See you later!' She waves as you exit her store.")
                elif "flower" not in backpack :
                    print("'Sorry! I don't have a flower right now! If I get one, I'll be sure to come back here!'")
                    print("'Oh! That's okay! See you later!'")
            elif visit == "professor goblin" :
                print("'Hey, Professor Goblin! What do you have here?'")
                print("'Sup',", username, "! I have a potato farm here. You can buy one potato for 2! Isn't that a great bargain?!'")
                print("'Err...Professor? That's not how bargaining works.'")
                print("'You know what? Never mind.'")
                if coins >= 3:
                    coins -= 3
                    backpack.append("potato")
                    backpack.append("potato")
                    backpack.append("potato")
                    print("🥔 You bought 3 potatoes!")
                else:
                    print("Looks like you don't have enough coins yet!")
                print("'I have coins though! I'll pay 1 coin for 1 potato! How's that?'")
                print("'Coins? What's that? Ain't potatoes a universal currency?'")
                print("'No! Coins are! Here, take 3 coins!'")
                print("'Ya sure?' He give you a bombastic sideye as he hands you 3 potatoes. 'Yep, I'm sure!'")
                print("You let out a long-suffering sigh when Professor Goblin sits down right on his potatoes and starts eating a poisonous potato.")
                print("'No professor! Don't eat that! It's bad for you!'")
                print("You snatch away the potato, and leave him to mourn the loss of his poisonous potato as you wander around the village.")\
                # rn player can choose only 1 place to visit. learn loops better, then fix
else :
    print("Invalid input. Please try again.")
    while activity != "explore meadow" and activity != "visit village" :
        activity = input("What do you want to do? : ").lower()
        if activity == "explore meadow" :
            print("You might find flowers...")
            print("You might find some feathers...")
            print("You may also discover honey!")
            print("Go collect them!")
        elif activity == "visit village" :
            print("You will miss those pretty items...for now.")
            print("Anyways...to the village!")

# too much repetition everywhere. fix later when learnt functions n stuff

# psst -> master plan : maybe ya can take this project till years later and and eventually add more features, when ya learn how to make
# actual blocks, try making a simple mincraft game (its a bit wild, but like consistency is key. ya can do it!!)

# wild idea : nether -> erupting volcanoes if triggered a designated pressure plate

# FUTURE IDEAS
# add health + add hunger
# save game
# random chance of finding items
# different flowers with different values
# npc friendship system (iron golem, etc)
# shops that restock daily
# inventory limit + crafting system
# weather + day/night cycle