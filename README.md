# rassberipi-ai

```
sudo apt update && sudo apt dist-upgrade -y
sudo apt install portaudio19-dev
sudo apt install python3-pyaudio python3-pip python3-virtualenv espeak flac -y
sudo apt install alsa-utils
```
## Create Enviorment

```

mkdir chatgpt
cd chatgpt
virtualenv -p python3 chatgpt
source chatgpt/bin/activate
wget https://raw.githubusercontent.com/betapinet/rassberipi-ai/refs/heads/main/chat-gpt.py

```

## Install Packeages

```

pip install speechrecognition
pip install SpeechRecognition pyaudio
pip install pyttsx3
pip install openai==0.28

```

```
nano chat-gpt.py  # Change API

python3 chat-gpt.py

```



