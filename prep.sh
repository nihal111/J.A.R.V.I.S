#!/bin/bash

echo Hi! I'm J.A.R.V.I.S. Hold on! I'm setting myself up!

echo AIML is at my core! Installing AIML...
pip install aiml
echo AIML succesfully installed!
echo Installing SpeechRecognition
pip install SpeechRecognition
echo Installing PyAudio
pip install pyaudio
echo Setting up Volume Control
pip install pyalsaaudio
echo Setting up Offline Text to Speech Service
pip install pyttsx

echo Setting up Google Text to Speech service

pip install gTTS

echo Installing PyGame
echo Setting up Essentials...
sudo apt-get build-dep python-pygame
sudo apt-get install mercurial
pip install hg+http://bitbucket.org/pygame/pygame
echo J.A.R.V.I.S. Setup Complete! Run script.py to Activate!
