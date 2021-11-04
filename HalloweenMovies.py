print("Let's choose a Halloween movie to watch! Answer the following questions with Y for yes or N for no.")
scary = input("Do you want to be scared? Y/N: ")
if scary == "Y" or scary == "y":
    new = input("Do you want a newer movie rather than an older movie? ")

    if new == "Y" or new == "y":
        clap = input("Is clapping scarier than a tongue cluck? ")

        if clap == "Y" or clap == "y":
            print("You should watch The Conjuring (2017)")
        elif clap == "N" or clap == "n":
            print("You should watch Hereditary (2018)")
        else:
            print("Invalid input")

    elif new == "N" or new == "n":
        decade = input("Do you prefer the 80's to the 90's? ")

        if decade == "Y" or decade == "y":
            adaptation = input("Do you prefer film adaptations of books? ")

            if adaptation == "Y" or adaptation == "y":
                print("You should watch Children of the Corn (1984)")
            elif adaptation == "N" or adaptation == "n":
                print("You should watch Nightmare on Elm Street (1984)")
            else:
                print("Invalid input")

        elif decade == "N" or decade == "n":
            kids = input("Do you prefer child protagonists to teens/adults? ")
            
            if kids == "Y" or kids == "y":
                print("You should watch It (1990)")
            elif kids == "N" or kids == "n":
                print("You should watch The Blair Witch Project (1999)")
            else:
                print("Invalid input")

        else:
            print("Invalid input")

    else:
        print("Invalid input")


elif scary == "N" or scary == "n":
    disney = input("Do you want a Disney movie? ")

    if disney == "Y" or disney == "y":
        magic = input("Do you want a movie that includes magic? ")

        if magic == "Y" or magic == "y":
            family = input("Do you have a big family? ")

            if family == "Y" or family == "y":
                print("You should watch Halloweentown (1998)")
            elif family == "N" or family == "n":
                print("You should watch Twitches (2005)")
            else:
                print("Invalid input")

        elif magic == "N" or magic == "n":
            print("You should watch Haunted Mansion (2003)")

        else:
            print("Invalid input")

    elif disney == "N" or disney == "n":

        pg = input("Do you want a family-friendly movie? ")

        if pg == "Y" or pg == "y":
            ghosts = input("Do you prefer ghosts to witches? ")

            if ghosts == "Y" or ghosts == "y":
                print("You should watch Casper (1995)")
            elif ghosts == "N" or ghosts == "n":
                print("You should watch Hocus Pocus (1993)")
            else:
                print("Invalid input")

        elif pg == "N" or pg == "n":
            print("You should watch Scary Movie (2000)")

        else:
            print("Invalid input")

    else:
        print("Invalid input")

else:
    print("Invalid input")

