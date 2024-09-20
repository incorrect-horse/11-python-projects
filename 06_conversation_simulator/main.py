from random import choice

questions = [
    "Why is the sky blue? ",
    "Why is the Earth round? ",
    "Why do birds sing? ",
    "Why is there a face on the moon? ",
    "Where did all of the dinosaurs go? "
]

question = choice(questions)
answer = input(question).strip().lower()

try:
    while answer != "because":
        answer = input("Why? ").strip().lower()
except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ... terminating app, please wait.")

print("Oh... Okay")
print("\nGoodbye!")
