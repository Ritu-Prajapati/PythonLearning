# using pip install wikipedia
import wikipedia
result = wikipedia.page("World")
print(result.summary)

# using pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
engine.say("Hi I am Ritu")
engine.runAndWait()
