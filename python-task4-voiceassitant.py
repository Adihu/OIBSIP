import datetime
import importlib
import webbrowser

try:
  pyttsx3 = importlib.import_module("pyttsx3")
except ImportError:
  pyttsx3 = None

try:
  sr = importlib.import_module("speech_recognition")
except ImportError:
  sr = None

# Initialize the text-to-speech engine when the package is available.
engine = pyttsx3.init() if pyttsx3 is not None else None


def speak(text):
  """Converts text to speech."""
  print(f"JARVIS: {text}")
  if engine is not None:
    engine.say(text)
    engine.runAndWait()


def listen_command():
  """Listens to microphone input and converts it to text."""
  if sr is None:
    speak("Speech recognition is not installed. Please install the SpeechRecognition package.")
    return ""

  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("\nListening...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    try:
      audio = recognizer.listen(source, timeout=5)
      command = recognizer.recognize_google(audio).lower()
      print(f"You said: {command}")
      return command
    except sr.WaitTimeoutError:
      speak("I didn't hear anything. Please try again.")
    except sr.UnknownValueError:
      speak("Sorry, I could not understand what you said.")
    except sr.RequestError:
      speak("Speech recognition service is offline.")
    return ""


def run_assistant():
  """Main loop for handling voice commands."""
  speak("Hello! I am JARVIS. How can I assist you today?")

  while True:
    command = listen_command()

    if not command:
      continue

    if "time" in command:
      now = datetime.datetime.now().strftime("%I:%M %p")
      speak(f"The current time is {now}")

    elif "date" in command:
      today = datetime.date.today().strftime("%B %d, %Y")
      speak(f"Today's date is {today}")

    elif "search" in command:
      search_query = command.replace("search", "").strip()
      if search_query:
        url = f"https://www.google.com/search?q={search_query}"
        speak(f"Searching Google for {search_query}")
        webbrowser.open(url)
      else:
        speak("What would you like me to search for?")

    elif "open youtube" in command:
      speak("Opening YouTube")
      webbrowser.open("https://www.youtube.com")

    elif "exit" in command or "stop" in command or "bye" in command:
      speak("Goodbye! Have a great day.")
      break

    else:
      speak("Command not recognized. You can ask for time, date, or search.")


if __name__ == "__main__":
  run_assistant()