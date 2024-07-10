# # Create a JSON file in Python

# import json

# # Create a dictionary to store the data
# data = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }

# # Convert the dictionary to a JSON string
# json_data = json.dumps(data)

# # Write the JSON string to a file
# with open("data.json", "w") as f:
#     f.write(json_data)


def traducir_palabra(palabra):
    # Diccionario de palabras en inglés y su traducción al español
    diccionario = {
        "hello": "hola",
        "goodbye": "adiós",
        "thank you": "gracias",
        "please": "por favor",
        "yes": "sí",
        "no": "no",
        "good morning": "buenos días",
        "good afternoon": "buenas tardes",
        "good evening": "buenas noches",
        "how are you": "cómo estás",
        "I'm fine": "estoy bien",
        "what's your name": "cómo te llamas",
        "my name is": "me llamo"
    }

    # Verificar si la palabra está en el diccionario
    if palabra.lower() in diccionario:
        return diccionario[palabra.lower()]
    else:
        return "Lo siento, no conozco esa palabra."

# Ejemplo de uso
palabra_ingles = input("Ingresa una palabra en inglés: ")
traduccion = traducir_palabra(palabra_ingles)
print(f"La traducción al español es: {traduccion}")