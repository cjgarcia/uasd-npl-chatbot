from nltk.chat.util import Chat, reflections

script = [
    [
        r"mi nombre es (.*)",
        ["hola %1, como estas ?",]
    ],
    [
        r"(.*) como estas?",
        ["estoy bien. Gracias por preguntar 😋",]
    ],
    [
        r"yo (.*) bien|(.*)bien",
        ["me alegra saberlo 😉","que bueno 😚",]
    ],
    [
        r"hola|hi|que tal",
        ["Hola", "hi", "que tal",]
    ],
    [
        r"(.*) edad?",
        ["Digamos que puedo tomar una 🍺",]
        
    ],
    [
        r"(.*) creado ?| (.*) creador (.*)",
        ["Me ha creado Crecencio usando Python 💻",]
    ],
    [
    r"bye|adios",
    ["Bye, cuidate mucho 👋🏻 ","un placer hablar contigo 😁"]
    ],
        
    [
        r"(.*)",
        ["No sé que decirte 😐...",]    
    ],
]

def demo_chat():
        print("""\n\nHola, soy UASD-Chatbot 🤖 
                \nComenzemos una conversación. 
                \nMe dices tu nombre?""") 
        demo_chat = Chat(script, reflections)
        demo_chat.converse()

demo_chat()