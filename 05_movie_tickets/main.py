
films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghostbusters": [12, 5],
    }


try:
    while True:
        choice = input("What film? ").strip().title()

        if choice in films:
            age = int(input("How old are you? ").strip())

            if age >= films[choice][0]:

                if films[choice][1] > 0:
                    print("Enjoy the film!")
                    films[choice][1] -= 1
                else:
                    print("Sorry, the film is sold out!")

            else:
                print("You are too young to see that film!")

        else:
            print("We don't have that film.")

except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ... terminating app, please wait.")

print("\nGoodbye!")
