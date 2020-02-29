# Voice Assistant

#### Created and Tested on Linux with Python 2.7

An attempt to make a very simple, Personal Assistant that understands speech as well as text input and is capable of performing tasks other than conversing.
This project is based on AIML 1.0 and uses pyaiml for using the AIML interpreter in python. AIML, is based on pattern matching and this project does not implement any sort of machine learning or language processing. All conversation is only for the hardcoded patterns, which are quite few. Can be easily extended to add AIML scripts of ALICE and other existing AIs.


- ### Tasks that the Bot can perform :

    - Tell the time 
    - Plays any song, first search result in youtube
    - Gives a brief system status.
    - Suggests Googling for all unrecognized interrogative questions
    - Changes Wallpaper.
    - Searches internet.
    - Launches Programs.
    
## Requirements:

Make sure you install these packages before moving forward to other python libraries-

`sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg libav-tools`

You can run `pip install -r requirements.txt` to install them all.

Individual packages listed as follows-

- ### AIML (For Pattern Recognition)
    `pip install aiml`

- ### Speech Recognition
    `pip install SpeechRecognition`

- ### PyAudio is required for microphone input
    `pip install pyaudio`

- ### alsaaudio: (For Volume Control, Linux only)
    `pip install pyalsaaudio`

- ### ttsx: (Offline Text to Speech Service)
    `pip install pyttsx`

- ### Optional for Google Text to Speech :
   + #### gTTS: (Google Text to Speech service)
      `pip install gTTS`

   + #### PyGame: (For audio playback with gTTS)
       `pip install pygame`

- ### argparse (For parsing arguments)
    `pip install argparse`

## Installation:

Clone this repository. Change directories to go to that directory. Run the script "script.py" **from the directory containing it**.
Run script as:

`python script.py` : for text mode (default) of input

`python script.py --voice` : for voice mode of input

`python script.py --voice --gtts` : for voice mode of input, with Google Text to Speech enabled

Voice mode may give a series of warnings for numerous reasons, but still might fuction properly.

## Contribution:

A lot can be done with this project. Core AI chatbot like functionality can be added. More python scripts can be associated. Pull requests for any such changes are accepted. Feel free to fork this project and make your own changes too.
