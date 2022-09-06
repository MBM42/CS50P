# Ask user for user name
name = input ("What's your name? ")

# Remove whitespace from string and capitalize user's name
name = name.strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print ("hello,", name)
print (f"hello, {last}")