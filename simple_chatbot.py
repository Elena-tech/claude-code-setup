#!/usr/bin/env python3
"""
Simple Terminal Chatbot
A minimal chatbot with canned responses for demonstration purposes.
"""

def main():
    print("=" * 50)
    print("Welcome to Simple Chatbot!")
    print("=" * 50)
    print("Hello! I'm a simple chatbot. How are you today?")
    print("(Type 'quit' or 'exit' to end the conversation)\n")

    # Canned responses dictionary
    responses = {
        "hello": "Hello there! Nice to meet you!",
        "hi": "Hi! How can I help you today?",
        "hey": "Hey! What's up?",
        "how are you": "I'm doing great, thanks for asking! I'm just a simple chatbot.",
        "good": "That's wonderful to hear!",
        "bad": "I'm sorry to hear that. I hope things get better!",
        "fine": "Glad to hear you're doing fine!",
        "bye": "Goodbye! Have a great day!",
        "goodbye": "Goodbye! It was nice chatting with you!",
        "thanks": "You're welcome!",
        "thank you": "You're very welcome!",
        "help": "I can respond to: hello, hi, how are you, good, bad, bye, and more!",
    }

    while True:
        # Get user input
        user_input = input("You: ").strip().lower()

        # Check for exit commands
        if user_input in ["quit", "exit", "q"]:
            print("\nChatbot: Goodbye! Thanks for chatting with me!")
            break

        # Check if input is empty
        if not user_input:
            print("Chatbot: Please say something!\n")
            continue

        # Look for matching response
        response_found = False
        for keyword, response in responses.items():
            if keyword in user_input:
                print(f"Chatbot: {response}\n")
                response_found = True
                break

        # Default response if no match found
        if not response_found:
            print("Chatbot: I'm not sure how to respond to that. Try saying 'help' for suggestions!\n")

if __name__ == "__main__":
    main()
