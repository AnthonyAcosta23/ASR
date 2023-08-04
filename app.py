import speech_recognition as sr
import pyttsx3
import pyaudio


def listen_to_agent():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to agent...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        agent_input = recognizer.recognize_google(audio)
        print(f"Agent: {agent_input}")
        return agent_input

    except sr.UnknownValueError:
        print("Could not understand agent. Please try again.")
        return listen_to_agent()

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""


def talk_to_agent(response):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(response)
    engine.runAndWait()


if __name__ == "__main__":
    def main():
        while True:
            agent_input = listen_to_agent()

            # Your logic here to process the agent_input and generate the appropriate response.
            # For simplicity, let's just echo the agent's input.

            if agent_input.lower() == 'exit':
                talk_to_agent("Goodbye!")
                break
            else:
                response = f"You said: {agent_input}"
                talk_to_agent(response)


    main()