#install openai-whisper with pip
#install ffmpeg

import whisper
model = whisper.load_model("base")
rep = model.transcribe("audio.m4a")
print(rep)
