

def Dinnig_hall():
    print("\n Your in dinning hall")
    print("\n There is a door.")
    print("\n Which one you take?(1 or 2)")
    print("1)Eat some food  and go through the door.")
    print("2)Take some food and  go through the door.")
    answer = input(">").lower()
    if answer == "1":
        print("\n In that food chicken got bird flu.so you died")
        play_again()
    elif " 2 " in answer:
        print("/n Congratulations! now you got another food , eat and enjoy the party ")
        play_again()
    else:
        game_over()


def Honey_room():
    print("\n Now ur in honey room.\n there is a way ")
    print("\n choose one way(way 1 or way 2)")
    print("1)Eat some honey")
    print("2) Just go away")
    answer = input(">")
    if answer == "1":
        print("Good!You got energy.\n you got a Daimond. ")
        Dinnig_hall()
    elif answer == "2":
        print("You not have an energy now.\n so go and take  some energy")
        return start()
    else:
        game_over()


def Sweets_room():
    print("\n Now ur in sweets room.|n there is way")
    print("\n choose one way(way 1 or way 2)")
    print(" 1)Eat some sweets")
    print(" 2) Just go away")
    answer = input(">")
    if answer == "1":
        print("Good!You got energy.\n you got a Daimond. ")
        Dinnig_hall()
    elif answer == "2":
        print("You not have an energy now.\n so go and take  some energy")
        return start()
    else:
        game_over()


def Bridge_room():
    print(
        "\n There is a one old bridge.You have to cross that bridge.\n There is two paths(path1 or path2")
    print("1)There is a bicycle. take that and go cross the bridge . ")
    print("2)Just walk and cross the bridge.")
    answer = input(">")
    if answer == "1":
        print("Bridge was breaked you and bicyle weight is high . ")
        return start()
    elif answer == "2":
        print("Nice! you crossed bridge.you got 100 gold coins")
        Honey_room()
    else:
        game_over()


def Water_room():
    print(
        "\n There is filleed with water.You have to cross that water.\n There is two paths(path1 or path2")
    print("1)There is a boat. take that and go cross the water . ")
    print("2)Swim  and cross the water.")
    answer = input(">")
    if answer == "1":
        print("Nice!You crossed the water and you got 100 gold coins.")
        Honey_room()
    elif answer == "2":
        print(
            "You submerged in water But you have immunity.")
        Sweets_room()
    else:
        game_over()


def Fire_room():
    print(
        "\n In the room fire is there.\n There is two paths(path1 or path2")
    print("1)Take the jocket run fast . ")
    print("2)Take the jocket and go slowly.")
    answer = input(">")
    if answer == "1":
        print("Nice!You are safe and you got 100 gold coins.")
        Sweets_room()
    elif answer == "2":
        print("You lost! your jocket was damaged.")
        return start()
    else:
        game_over()


def Dragon_room():
    print(
        "\n In that room dragon is there.Dragon was Eating. \n Which one you choose(1 or 2)")
    print("1)Kill the dragon.")
    print("2)Just go silently.")
    answer = input(">")
    if answer == "1":
        print("You lost!dragon was killed you and you die.")
        return start()
    elif answer == "2":
        print("Nice! you escaped and got energy drink.")
        Bridge_room()
    else:
        game_over()


def Lion_room():
    print(
        "\n In that room lion is there.Lion was sleeping and it was so hungry. \n Which one you choose(1 or 2)")
    print("1)Go slowly")
    print("2)Just run away.")
    answer = input(">")
    if answer == "1":
        print("You  escaped and you got 100$.")
        Bridge_room()
    elif answer == "2":
        print("Nice! you escaped and got immunity power.")
        Water_room()
    else:
        game_over()


def Tiger_room():
    print(
        "\n In that room tiger is there.Tiger was sleeping and it was so hungry. \n Which one you choose(1 or 2)")
    print("1)Go slowly")
    print("2)Just run away.")
    answer = input(">")
    if answer == "1":
        print("You  escaped and you got immunity power.")
        Water_room()
    elif answer == "2":
        print("Nice! you escaped and got 100$.")
        Fire_room()
    else:
        game_over()


def Monster_room():
    print(
        "\n In that room monster is there.monster was Eating. \n Which one you choose(1 or 2)")
    print("1)Just go silently.")
    print("2)Kill the monster.")
    answer = input(">")
    if answer == "1":
        print("Nice! you escaped and got energy drink.")
        Fire_room()
    elif answer == "2":
        print("You lost!dragon was killed you and you died.")

        return start()
    else:
        game_over()


def Dogs_room():
    print(
        "\n In that room dogs are there.Dogs want to drink water.\n There is water. \n Which one you choose(1 or 2)")
    print("1)Take the water and go.")
    print("2)Go.")
    answer = input(">")
    if answer == "1":
        print("Nice! you are taken water when dogs are did not see u.")
        Dragon_room()
    elif answer == "2":
        print("Nice! You escaped from that")
        Lion_room()
    else:
        game_over()


def Cats_room():
    print(
        "\n In that room cats are there.cats want to drink milk.\n There is milk. \n Which one you choose(1 or 2)")
    print("1)Take the milk and go.")
    print("2)Go.")
    answer = input(">")
    if answer == "1":
        print("Nice! you are taken milk when cats are did not see u.")
        Monster_room()
    elif answer == "2":
        print("Nice! You escaped from that")
        Tiger_room()
    else:
        game_over()


def play_again():
    print(" Do you want to play ?(y or n)")
    answer = input(">").lower()
    if "y" in answer:
        start()
    else:
        exit()


def game_over(reason):
    print("\n"+reason)
    print("Game over")
    play_again()


def start():
    print("welcome to the game")
    print("ur in closed room")
    print("\n there is a door to your left and right, which one do you take? (left or right)")
    answer = input(">").lower()
    if "left" in answer:
        Dogs_room()
    elif "right" in answer:
        Cats_room()
    else:
        game_over("don't you no how to type something properly? ")


start()
