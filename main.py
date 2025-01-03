from neuralintents import GenericAssistant, BasicAssistant
import speech_recognition
import pyttsx3 as tts
import sys

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = ['Clean room', 'Finish ML project', 'Cry']


def create_note():
    global recognizer

    speaker.say("What do you want to write onto your note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_amazon(audio)
                note = note.lower()

                speaker.say("Choose a filename!")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_amazon(audio)
                filename = filename.lower()
            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"The note has successfully been created: {filename}")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Sorry, I could not understand you, please try again!")
            speaker.runAndWait()


def add_todo():
    global recognizer

    speaker.say("What would you like to add to your todo?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_amazon(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                speaker.say(f"I have successfully added {item} to the to do list!")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Sorry, I could not understand you, please try again!")
            speaker.runAndWait()


def show_todos():
    speaker.say("The items on your to do list are the following:")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def hello():
    speaker.say("Hello, what can I do for you?")
    speaker.runAndWait()

def quit():
    speaker.say("Goodbye")
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todo": show_todos,
    "exit": quit
}

assistant = BasicAssistant('intents.json')
#assistant.train_model()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio =  recognizer.listen(mic)

            message = recognizer.recognize_amazon(audio)
            message = message.lower()

 #       assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()