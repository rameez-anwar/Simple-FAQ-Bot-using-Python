class SimpleChatbot:
    def __init__(self, faq_database):
        self.faq_database = faq_database

    def get_response(self, user_query):
        # Tokenize user's query
        user_tokens = set(user_query.lower().split())

        # Iterate through FAQ entries and find the one with the most common words
        best_match_question, best_match_count = None, 0

        for question, answer in self.faq_database.items():
            faq_tokens = set(question.lower().split())
            common_tokens = user_tokens.intersection(faq_tokens)

            if len(common_tokens) > best_match_count:
                best_match_count = len(common_tokens)
                best_match_question = question

        # Return the answer to the best-matching question
        if best_match_question is not None:
            return self.faq_database[best_match_question]
        else:
            return "I'm sorry, I didn't understand your question. Please try asking in a different way."

# Example FAQ database
faq_database = {
    "What are your business hours?": "Our business hours are from 9 AM to 5 PM, Monday to Friday.",
    "How can I contact customer support?": "You can contact our customer support at support@rameez.com.",
    "Do you offer international shipping?": "Yes, we offer international shipping to many countries."
}

# Initialize the chatbot with the FAQ database
chatbot = SimpleChatbot(faq_database)

# Example interaction with the chatbot
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = chatbot.get_response(user_input)
    print("Chatbot:", response)
