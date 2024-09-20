# Ask for name
name = input("\nWhat name? ")

# Ask for age
age = input("\nHow old? ")

# Ask for city
city = input("\nWhere live? ")

# Ask what enjoy
enjoy = input("\nWhat do? ")

# Create output
output = f"\nCongratulation, you are {name}, you are {age} \
years old, you live in {city} and you enjoy doing {enjoy}!!"

# print output
print(output)

try:
    pass
except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ... terminating app, please wait.")

print("\nGoodbye!")
