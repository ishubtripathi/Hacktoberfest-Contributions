import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Text to be converted to speech
text = "Hello, this is a minimal example of pyttsx3."

# Convert text to speech
engine.say(text)

# Play the speech
engine.runAndWait()
