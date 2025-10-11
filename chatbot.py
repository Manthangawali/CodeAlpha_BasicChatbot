def chatbot_reply(user_input):

    user_input = user_input.lower()  

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

print("Chatbot: Hello! Type something to chat with me.")

while True:
    
    user_message = input("You:") 
    response = chatbot_reply(user_message)  
    print("Chatbot:", response)

    if user_message.lower() == "bye":
        break
