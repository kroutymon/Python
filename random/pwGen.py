import secrets

# Wird erst gemoked
pw = ""

# Quelle
character = "QWERTZUIOPASDFGHJKLYXCVBNMqwertzuiopasdfghjklyxcvbnm,.-;:_1234567890@!?"

# Input
length = int(input("enter passwordlength:"))

for _ in range(length):
    pw = pw + secrets.choice(character)

print(pw)
