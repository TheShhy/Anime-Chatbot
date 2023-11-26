#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

# Define predefined responses
greetings = ["Hello, anime enthusiast!", "Hi there, fellow otaku!", "Hey, anime lover!", "Greetings, anime fan!"]
farewells = ["Goodbye, and keep watching anime!", "Farewell, until our next anime adventure!", "See you later, fellow otaku!", "Take care and enjoy your anime!"]
questions = {
    "What's your favorite anime?": ["I'm just a chatbot, so I don't have favorites.", "I haven't watched any anime, but I can help you find some recommendations!"],
    "Recommend me an anime.": ["Sure! How about trying 'My Hero Academia' or 'Attack on Titan'?", "I recommend 'One Piece' or 'Naruto' if you haven't watched them yet."],
    "Who is your favorite anime character?": ["I admire many anime characters, but I don't have a single favorite.", "There are so many great characters to choose from!"],
    "What's the best shonen anime?": ["There are many great shonen anime series, but 'Fullmetal Alchemist: Brotherhood' is a fan favorite.", "'My Hero Academia' is a popular shonen anime with a great story and characters."],
    "Recommend me a romance anime.": ["You might enjoy 'Your Lie in April' if you're looking for a touching romance anime.", "I recommend 'Toradora!' for a heartwarming romantic story."],
    "Who is the strongest anime character ever?": ["Debating the strongest anime character is a hot topic! Some say Saitama from 'One Punch Man' is unbeatable.", "Characters like Goku from 'Dragon Ball' and Alucard from 'Hellsing' are often considered incredibly powerful."],
    "What's your favorite anime genre?": ["I don't have personal preferences, but I can recommend anime from various genres! What are you in the mood for?"],
    "What's the longest-running anime series?": ["'One Piece' holds the record as one of the longest-running anime series with over 1000 episodes.", "'Naruto' and 'Detective Conan' are also among the longest-running anime."],
    "Tell me an anime with great music.": ["'Cowboy Bebop' is known for its fantastic jazz soundtrack.", "If you love music, 'Your Lie in April' combines beautiful music with a touching story."],
    "What's the most iconic anime opening song?": ["Many anime fans consider 'Cruel Angel's Thesis' from 'Neon Genesis Evangelion' to be one of the most iconic anime opening songs.", "'Tank!' from 'Cowboy Bebop' is another classic."],
    "What's the difference between anime and manga?": ["Anime refers to animated TV shows or movies, while manga are Japanese comic books or graphic novels. They often share the same stories but in different formats."],
    "What's the best anime movie?": ["'Spirited Away' by Studio Ghibli is widely regarded as one of the best anime movies ever made.", "'Your Name' and 'A Silent Voice' are also highly acclaimed."],
    "Do you have any anime trivia?": ["Sure! Did you know that 'Akira' is considered a landmark in anime history and played a major role in introducing anime to the Western world?"]
}

# Function to respond to user input
def anime_chatbot_response(user_input):
    user_input = user_input.lower()

    for greeting in greetings:
        if greeting.lower() in user_input:
            return random.choice(greetings)

    for farewell in farewells:
        if farewell.lower() in user_input:
            return random.choice(farewells)

    for question, responses in questions.items():
        if question.lower() in user_input:
            return random.choice(responses)

    return "I'm not quite sure what you mean. Let's talk more about anime!"

# Main chat loop
print("Anime ChatBot: Hello, anime enthusiast! How can I assist you today? (Type 'exit' to end)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Anime ChatBot: Sayonara! Enjoy your anime.")
        break

    response = anime_chatbot_response(user_input)
    print("Anime ChatBot:", response)


# In[ ]:




