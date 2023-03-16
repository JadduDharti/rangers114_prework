#message = input("Tell me something and I will repeat it back to you: ")
#print(message)

#name1 = input("Please Enter your name: ")
#print("Hello " + name1 + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

height = input("Enter your height in inches: ")
height = int(height)

if height >= 36:
    print("\n Ypu are tall enough to ride")
else:
    print("You'll able to ride when you are little older")
