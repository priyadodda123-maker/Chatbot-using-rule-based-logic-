def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi there!")
        elif user == "how are you":
            print("Chatbot: I'm fine, thank you!")
        elif user == "what is your name":
            print("Chatbot: I am a simple chatbot.")
        elif user == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
output:
Chatbot: Hello! Type 'bye' to exit.
You: Hii
Chatbot: Sorry, I don't understand.
You: Hello
Chatbot: Hi there!
You:Bye
Chatbot:Goodbye!
