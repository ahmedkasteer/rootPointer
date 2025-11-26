x = input("Enter your fav color for e.g Red: ")
match x:
    case "Orange":
        print("Vibrant")
    case "Blue":
        print("Royal")
    case "Red":
        print("Watermelon")
    case "Purple":
        print("Grapes")
    case "Black":
        print("Majestic")
    case "Yellow":
        print("Jolly human")
    case "Pink":
        print("Bubblegum")
    case _:
        print("Sorry, bad choice of color")
