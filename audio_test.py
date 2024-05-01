
import speech_recognition as sr
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
led = LED(14)

r = sr.Recognizer()
mic = sr.Microphone(device_index = 0, sample_rate = 44100, chunk_size = 512)

while True:
	with mic as source:
		audio = r.listen(source)
	w = r.recognize_google(audio).lower()
	if w == "yes":
		led.on()
	elif w == "no":
		led.off()

	
