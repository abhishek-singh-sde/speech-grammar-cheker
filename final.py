import pyaudio
import wave

chunk_size = 1024
format = pyaudio.paInt16
channels = 2
fs = 44100
file_name = input("Give a name to your output file (it will get stored in your python folder\n")
out_file_name = file_name + ".wav"

p = pyaudio.PyAudio()

stream = p.open(format=format,
                channels=channels,
                rate=fs,
                input=True,
                frames_per_buffer=chunk_size)

print("Recording Started. Press Ctrl+C when you are done to save")

frames = []
try:
    while True:
        data = stream.read(chunk_size)
        frames.append(data)
except KeyboardInterrupt:
    pass

print("The recording has been completed")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(out_file_name, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

import speech_recognition as sr
r=sr.Recognizer()
recorded_audio=sr.AudioFile(out_file_name)
with recorded_audio as source:
    audio=r.record(source)


text1=r.recognize_google(audio)
#text1=r.recognize_sphinx(audio)
print(text1)

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("start-maximized")

#Use the path of your chromedriver.exe file here

driver = webdriver.Chrome(options=options, executable_path=(r"C:\Users\Abhishek\AppData\Local\Programs\Python\Python37\chromedriver_win32\chromedriver.exe"))
driver.get("https://www.onlinecorrection.com/")


z=driver.find_element_by_class_name("clear-on-click")
z.click()
z.send_keys(text1)
p=driver.find_element_by_id("fbut")
p.click()