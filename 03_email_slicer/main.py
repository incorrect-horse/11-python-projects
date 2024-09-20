email = input("Enter email address: ").strip()
# email = "user123@email.com"

# at_split = email.find("@")
at_split = email.index("@")
username = email[:at_split]
domain = email[(at_split + 1):]
output = f"Your username is '{username}' and your server domain is '{domain}'"

print(output)

try:
    pass
except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ... terminating app, please wait.")

print("\nGoodbye!")
