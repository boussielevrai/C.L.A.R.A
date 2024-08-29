import speech_recognition as sr
import openai

# Créez un nouvel objet recognizer
recognizer = sr.Recognizer()

# Ajustez le bruit ambiant pour améliorer la reconnaissance
with sr.Microphone() as source:
    print("Veuillez parler...")
    recognizer.adjust_for_ambient_noise(source)  # Ajustement pour le bruit ambiant

    # Écoutez l'audio
    audio = recognizer.listen(source, timeout=20)  # Attendre jusqu'à une pause

try:
    # Reconnaissance de la parole
    texte = recognizer.recognize_google(audio, language='fr-FR')
    print("Vous avez dit : ", texte)
except sr.UnknownValueError:
    print("Je n'ai pas pu comprendre ce que vous avez dit.")
except sr.RequestError as e:
    print("Erreur avec le service de reconnaissance vocale; {0}".format(e))


# Example: reuse your existing OpenAI setup
from openai import OpenAI

texte = "hi"
# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": truc}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)

import pyttsx3
engine = pyttsx3.init()
engine.say(completion.choices[0].message)
engine.runAndWait()
