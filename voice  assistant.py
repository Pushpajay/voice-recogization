import speech_recognition as  sr
import webbrowser


sr.Microphone(device_index=1)

r=sr.Recognizer()

r.energy_threshold=5000

with   sr.Microphone() as   source:
    print("Speak!")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said:{}".format(text))
        url='https://google.com/?hl=en_GB'
        search_url=url+text
        webbrowser.open(search_url)
    except:
        print("can't recognize")
