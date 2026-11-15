
import datetime
import subprocess
import json

def speak(message):
    print("\nJARVIS:", message)
    subprocess.run(
        ["termux-tts-speak", message],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def get_battery():
    try:
        result = subprocess.check_output(
            ["termux-battery-status"],
            text=True
        )
        data = json.loads(result)
        return data["percentage"]
    except Exception:
        return None

def process_command(command):

    if command in ["hello", "hi", "namaste"]:
        speak("Hello sir. JARVIS is ready.")

    elif command in ["time", "what time"]:
        now = datetime.datetime.now()
        speak("Current time is " + now.strftime("%I:%M %p"))

    elif command in ["date", "today"]:
        today = datetime.date.today()
        speak("Today's date is " + today.strftime("%d %B %Y"))

    elif command in ["battery", "battery status"]:
        level = get_battery()
        if level is not None:
            speak(f"Your battery is {level} percent.")
        else:
            speak("Battery information unavailable.")

    elif command in ["help", "commands"]:
        speak("Commands: hello, time, date, battery and exit.")

    elif command in ["exit", "shutdown"]:
        speak("Goodbye sir.")
        return False

    else:
        speak("Command not recognised. Please try again.")

    return True

def main():
    speak("JARVIS online. Awaiting your command.")

    while True:
        command = input("\nYOU: ").lower().strip()

        if not process_command(command):
            break

if __name__ == "__main__":
    main()

import datetime
import subprocess
import json

def speak(message):
    print("JARVIS:", message)
    subprocess.run(
        ["termux-tts-speak", message],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def battery():
    try:
        result = subprocess.check_output(
            ["termux-battery-status"],
            text=True
        )
        data = json.loads(result)
        return f"Battery is {data['percentage']} percent."
    except Exception:
        return "I cannot access battery information."

def jarvis():
    speak("Hello. JARVIS is online.")

    while True:
        command = input("\nYOU: ").lower().strip()

        if command == "hello":
            speak("Hello sir. How can I help you?")

        elif command == "time":
            now = datetime.datetime.now()
            speak("The time is " + now.strftime("%I:%M %p"))

        elif command == "date":
            today = datetime.date.today()
            speak("Today's date is " + today.strftime("%d %B %Y"))

        elif command == "battery":
            speak(battery())

        elif command == "help":
            speak("Available commands are hello, time, date, battery and exit.")

        elif command == "exit":
            speak("Shutting down. Goodbye.")
            break

        else:
            speak("Sorry. I don't understand that command.")

jarvis()

