# Katelyn, Charles, and Shay
# Isalpha group project

# Prints message if it is exclusivley alphabetical. 
message = input("Enter your message:")
if message.isalpha():
    print(message)
# if the message only contains alphabetical values, 
# then the messaged will be displayed, otherwise
# the message will not be displayed. 

# Prints whether message is exlusivley alphabetical or not. 
msg_valid = str.isalpha(message)
print(msg_valid)

# If the messgae is exlusivley alphabetical, the output should be True. 
# If the message is not exclusivley alphabetical, the output should be False. 