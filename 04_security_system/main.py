known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "George", "Harry"]

try:
    while True:
        print("Hi! My name is Travis.")
        name = input("What is your name? ").strip().capitalize()

        if name in known_users:
            print(f"Hello, {name}!")
            remove = input("Would you like to be removed from the system (y/n)?").strip().lower()

            if remove == "y":
                known_users.remove(name)
            elif remove == "n":
                print("No problem, I didn't want you to leave anyway!")

        else:
            print(f"Hmmm, I don't think I have met you yet {name}")
            add_user = input("Would you like to be added to the system (y/n)?").strip().lower()

            if add_user == "y":
                known_users.append(name)
            elif remove == "n":
                print("No worries, see you around!")

except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ... terminating app, please wait.")

print("\nGoodbye!")
