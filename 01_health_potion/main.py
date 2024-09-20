import random

health = 50
difficulty = 3
potion = int(random.randint(25, 50) / difficulty)
health += potion
print(health)

try:
    pass
except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ... terminating app, please wait.")

print("Goodbye!")
