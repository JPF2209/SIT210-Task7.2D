#import libraries
import speech_recognition as sr
from gpiozero import LED
import RPi.GPIO
#Setting up LED
RPi.GPIO.setmode(RPi.GPIO.BCM)
led = LED(14)

#Setting up mic and recognizer
r = sr.Recognizer()
mic = sr.Microphone(device_index = 0, sample_rate = 44100, chunk_size = 512)

#While true
while True:
	#Listen out for audio
	with mic as source:
		audio = r.listen(source)
	#Turn into string
	w = r.recognize_google(audio).lower()
	#If I said yes, turn led on
	if w == "yes":
		led.on()
	#If i said no, turn led off
	elif w == "no":
		led.off()

	
