from nltk.chat.util import Chat, reflections

script = [
    [
        r"mi nombre es (.*)",
        ["hola %1, como estas ?",]
    ],
    [
        r"(.*) como estas?",
        ["estoy bien. Gracias por preguntar π",]
    ],
    [
        r"yo (.*) bien|(.*)bien",
        ["me alegra saberlo π","que bueno π",]
    ],
    [
        r"hola|hi|que tal",
        ["Hola", "hi", "que tal",]
    ],
    [
        r"(.*) edad?",
        ["Digamos que puedo tomar una πΊ",]
        
    ],
    [
        r"(.*) creado ?| (.*) creador (.*)",
        ["Me ha creado Crecencio usando Python π»",]
    ],
    [
    r"bye|adios",
    ["Bye, cuidate mucho ππ» ","un placer hablar contigo π"]
    ],
        
    [
        r"(.*)",
        ["No sΓ© que decirte π...",]    
    ],
]

def demo_chat():
        print("""\n\nHola, soy UASD-Chatbot π€ 
                \nComenzemos una conversaciΓ³n. 
                \nMe dices tu nombre?""") 
        demo_chat = Chat(script, reflections)
        demo_chat.converse()

demo_chat()