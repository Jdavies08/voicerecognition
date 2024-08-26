import pyaudio
import vosk
import json
model = vosk.Model(lang = "en-gb")

recogniser = vosk.KaldiRecognizer(model,30000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1,rate=30000,input=True,frames_per_buffer=8192)
result = {"text":""}
while True:
    data = stream.read(8000)
    if recogniser.AcceptWaveform(data):
        result = json.loads(recogniser.Result())['text']
        print(result)
    if "shut down" in result:
        break