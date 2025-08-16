import random
import re

class SimpleChatbot:
    def __init__(self):
        self.name = "ChatBot"
        self.user_name = ""
        
        # Predefined responses for different categories
        self.greetings = [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Hey! Nice to meet you!",
            "Greetings! How are you doing?"
        ]
        
        self.farewells = [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! It was nice chatting with you!",
            "Farewell! Come back anytime!"
        ]
        
        self.how_are_you_responses = [
            "I'm doing great! Thanks for asking. How about you?",
            "I'm functioning perfectly! How are you feeling?",
            "All systems running smoothly! What about you?",
            "I'm here and ready to chat! How's your day going?"
        ]
        
        self.name_responses = [
            f"Nice to meet you! I'm {self.name}, your friendly chatbot.",
            f"My name is {self.name}. What's your name?",
            f"I'm {self.name}! Pleased to make your acquaintance.",
            f"You can call me {self.name}. I'm here to help!"
        ]
        
        self.help_responses = [
            "I can chat with you about various topics, answer simple questions, or just have a friendly conversation!",
            "I'm here to help! You can ask me questions, tell me about your day, or just chat.",
            "I can assist you with basic conversations, provide simple information, or just be a friendly companion!",
            "Feel free to ask me anything! I can discuss topics, help with simple questions, or just chat casually."
        ]
        
        self.weather_responses = [
            "I don't have access to real-time weather data, but I hope it's nice where you are!",
            "I can't check the weather, but you could try a weather app or website for current conditions.",
            "Weather talk! I wish I could tell you the forecast, but I don't have that capability.",
            "I'm not connected to weather services, but I hope you're having pleasant weather!"
        ]
        
        self.default_responses = [
            "That's interesting! Can you tell me more?",
            "I'm not sure I understand completely. Could you rephrase that?",
            "Hmm, that's something to think about. What do you think?",
            "I see! What else would you like to talk about?",
            "That's a good point! Tell me more about your thoughts on this.",
            "I'm still learning! Can you help me understand better?"
        ]

    def preprocess_input(self, user_input):
        """Clean and prepare user input for processing"""
        return user_input.lower().strip()

    def get_response(self, user_input):
        """Generate response based on user input using if-elif-else logic"""
        processed_input = self.preprocess_input(user_input)
        
        # Greeting patterns
        if any(word in processed_input for word in ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']):
            return random.choice(self.greetings)
        
        # Farewell patterns
        elif any(word in processed_input for word in ['bye', 'goodbye', 'see you', 'farewell', 'exit', 'quit']):
            return random.choice(self.farewells)
        
        # How are you patterns
        elif any(phrase in processed_input for phrase in ['how are you', 'how do you do', 'how are things', 'what\'s up']):
            return random.choice(self.how_are_you_responses)
        
        # Name-related queries
        elif any(phrase in processed_input for phrase in ['what is your name', 'what\'s your name', 'who are you', 'your name']):
            return random.choice(self.name_responses)
        
        # User sharing their name
        elif 'my name is' in processed_input or 'i am' in processed_input:
            # Extract name using simple pattern matching
            if 'my name is' in processed_input:
                name_part = processed_input.split('my name is')[1].strip()
                if name_part:
                    self.user_name = name_part.split()[0].capitalize()
                    return f"Nice to meet you, {self.user_name}! How can I help you today?"
            elif 'i am' in processed_input:
                name_part = processed_input.split('i am')[1].strip()
                if name_part and not any(word in name_part for word in ['good', 'bad', 'fine', 'okay', 'sad', 'happy', 'tired']):
                    self.user_name = name_part.split()[0].capitalize()
                    return f"Hello {self.user_name}! It's great to meet you!"
            return "Nice to meet you! What would you like to chat about?"
        
        # Help requests
        elif any(word in processed_input for word in ['help', 'assist', 'support', 'what can you do']):
            return random.choice(self.help_responses)
        
        # Weather queries
        elif any(word in processed_input for word in ['weather', 'temperature', 'rain', 'sunny', 'cloudy']):
            return random.choice(self.weather_responses)
        
        # Time queries
        elif any(word in processed_input for word in ['time', 'date', 'day', 'today']):
            return "I don't have access to current time/date information, but you can check your device's clock!"
        
        # Compliments to the bot
        elif any(word in processed_input for word in ['good', 'great', 'awesome', 'cool', 'nice', 'smart']) and any(word in processed_input for word in ['you', 'bot', 'chatbot']):
            return "Thank you! That's very kind of you to say. I'm just trying to be helpful!"
        
        # Questions about AI/chatbots
        elif any(word in processed_input for word in ['robot', 'ai', 'artificial', 'computer', 'machine']):
            return "Yes, I'm a chatbot! I'm a simple rule-based program designed to have conversations with people like you."
        
        # Emotional expressions
        elif any(word in processed_input for word in ['sad', 'unhappy', 'depressed', 'down']):
            return "I'm sorry to hear you're feeling down. Sometimes talking can help. What's on your mind?"
        
        elif any(word in processed_input for word in ['happy', 'excited', 'great', 'wonderful', 'fantastic']):
            return "That's wonderful! I'm glad to hear you're feeling positive. What's making you happy?"
        
        elif any(word in processed_input for word in ['tired', 'sleepy', 'exhausted']):
            return "It sounds like you might need some rest. Make sure to take care of yourself!"
        
        # Age questions
        elif 'how old' in processed_input or 'age' in processed_input:
            return "I don't have an age in the traditional sense - I'm just a computer program! How old are you?"
        
        # Favorite things
        elif 'favorite' in processed_input or 'favourite' in processed_input:
            return "I don't have personal preferences since I'm a chatbot, but I'd love to hear about your favorites!"
        
        # Thank you
        elif any(word in processed_input for word in ['thank', 'thanks', 'appreciate']):
            return "You're welcome! I'm happy to help. Is there anything else you'd like to talk about?"
        
        # Yes/No responses
        elif processed_input in ['yes', 'yeah', 'yep', 'sure', 'absolutely']:
            return "Great! What would you like to discuss?"
        
        elif processed_input in ['no', 'nah', 'nope', 'not really']:
            return "Okay, no problem! Feel free to ask me anything else."
        
        # Default response for unrecognized input
        else:
            return random.choice(self.default_responses)

    def chat(self):
        """Main chat loop"""
        print("=" * 50)
        print(f"Welcome to {self.name}!")
        print("Type 'quit', 'exit', or 'bye' to end the conversation")
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    print(f"{self.name}: Please say something!")
                    continue
                
                # Check for exit commands
                if any(word in user_input.lower() for word in ['quit', 'exit', 'bye', 'goodbye']):
                    print(f"{self.name}: {random.choice(self.farewells)}")
                    break
                
                # Get and display response
                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"{self.name}: Sorry, I encountered an error. Let's keep chatting!")

# Example of how to extend the chatbot with more specific responses
def demo_chatbot():
    """Demonstrate the chatbot functionality"""
    print("Starting Chatbot Demo...")
    print("\nTry these sample inputs:")
    print("- Hello!")
    print("- How are you?")
    print("- What's your name?")
    print("- My name is Alex")
    print("- What can you do?")
    print("- How's the weather?")
    print("- I'm feeling happy today")
    print("- Thank you")
    print("- Goodbye")
    print("\n" + "=" * 50)
    
    # Create and start the chatbot
    bot = SimpleChatbot()
    bot.chat()

if __name__ == "__main__":
    demo_chatbot()