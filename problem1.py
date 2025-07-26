import random
import string

print("Welcome to Muskan's Password Generator!")

# Step1: Ask user for desired password length
length = int(input("Enter desired password length (e.g., 8, 10, 12): "))

# Step2: Define character sets
letters = string.ascii_letters
# a-z + A-Z
digits = string.digits
# 0-9
symbols = string.punctuation

# Step3: Combine all characters into one pool
all_characters = letters + digits + symbols

# Step4: Randomly generate the password 
password = ''.join(random.choice(all_characters) for _ in range(length))

# Step5: Display the result
print("Your generated password is: ", password)

