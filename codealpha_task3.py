def get_bot_response(user_input):
    """Determines the appropriate reply using rule-based logic."""
    cleaned_input = user_input.lower().strip()
    
    if cleaned_input == "hello":
        return "Hi!"
    elif cleaned_input == "how are you":
        return "I'm fine, thanks!"
    elif cleaned_input == "bye":
        return "Goodbye!"
    else:
        return "I'm still learning! Try saying 'hello', 'how are you', or 'bye'."

def run_chatbot():
    """Handles the main loop and user input/output."""
    print("Chatbot started! Type 'bye' to exit.")
    
    while True:
        user_message = input("You: ")
        
        reply = get_bot_response(user_message)
        
        print(f"Bot: {reply}")
        
        if user_message.lower().strip() == "bye":
            break

if __name__ == "__main__":
    run_chatbot()