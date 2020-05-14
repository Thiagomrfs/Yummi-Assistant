# Personal-Assistant
A voice-based personal assistant in python, Yummi will help you on doing tasks like opening an archive, opening a website, searching things and maybe telling you the time.

# Requirements
For this project we'll need some libraries to use speech recognition and search tools, they are:

### pyttsx3  
	# pip install pyttsx3==2.6  
With this library the assistant will be able to speak with us.  
*Due to some errors we'll be using the 2.6 version of this lib  
	  
### speech_recognition 
	# pip install speechRecognition  
With this library the assistant will hear us  

### wikipedia 
	# pip install wikipedia  
This library will help us to search things easily  

### pyAudio 
	# pip install pyAudio  
Because we´re using the Microphone Class we'll need to use the pyAudio lib  
* If you are using python 3.7+ you probably will have some problems installing this lib, so I recommend using a wheel, I downloaded a python 3.8 one, who is in support_files folder. To install it you'll need to use the alternative command.
> 	pip install *your whell here*

# Defalt commands
* Search Wikipedia
* Open *website*
* Open *archive*
* Time now
