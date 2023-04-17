# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment No.2 - Problem 2

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 35)
print("")
print("\033[45m ♥ Welcome to our program! ♥ \033[0m".center(78))

# Ask the name of the user 
name = input("\n\033[033mGood day! What is your name? \033[0m")
print("\n\033[3;33mI hope you are doing well,", name + "!\033[0m")
print("")

print("\033[36m Let's get started! \033[0m".center(78, "~"))

# Ask the user to input the encrypted message
encrypted_message = input("\n\033[3;35mPlease enter the message you want to decrypt: \033[0m")
decrypted_message = ""
