import random


def clean_input(text):
    text = text.lower().strip()
    return text


greetings = [
    "Hey there! What's on your mind?",
    "Hello! Hope you're having a great day!",
    "Hi! How can I help you?",
]

farewells = [
    "Goodbye! Take care!",
    "See you later! Come back anytime.",
    "Bye! It was great chatting with you!",
]

how_are_you = [
    "I'm doing great, thanks for asking! How about you?",
    "I'm good! How are you today?",
]

name_responses = [
    "I'm ChatBot, your rule-based AI assistant!",
    "My name is ChatBot! Nice to meet you!",
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "What did the Python snake say? I'm ssssssso happy to meet you!",
    "Why was the computer cold? It left its Windows open!",
]

thanks_responses = [
    "You're welcome!",
    "Happy to help!",
    "No problem at all!",
]

default_responses = [
    "That's interesting! Tell me more.",
    "I see! Can you tell me more about that?",
    "Hmm, I'm not sure I understand. Can you rephrase that?",
    "Cool! I'd love to hear more.",
]


def get_response(user_input):
    text = clean_input(user_input)

    if not text:
        return "Please say something!"

    if "bye" in text or "goodbye" in text or "exit" in text or "quit" in text:
        return "EXIT"

    if "hello" in text or "hi" in text or "hey" in text or "howdy" in text:
        if "name" in text:
            return random.choice(name_responses)
        return random.choice(greetings)

    if "how are you" in text or "how do you do" in text:
        return random.choice(how_are_you)

    if "your name" in text or "who are you" in text or "call you" in text:
        return random.choice(name_responses)

    if "joke" in text or "funny" in text:
        return random.choice(jokes)

    if "thanks" in text or "thank you" in text:
        return random.choice(thanks_responses)

    return random.choice(default_responses)


def chat():
    print("Welcome to the Rule-Based AI Chatbot!")
    print("Type 'bye' or 'exit' to end the chat.")
    print()

    while True:
        user_input = input("You: ")

        response = get_response(user_input)

        if response == "EXIT":
            print("Bot:", random.choice(farewells))
            break

        print("Bot:", response)
        print()


if __name__ == "__main__":
    chat()
