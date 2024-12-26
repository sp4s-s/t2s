import subprocess
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

command = 'ffmpeg -i aiml.mkv -ab 160k -ar 44100 -vn audio.wav'
subprocess.call(command, shell=True)

