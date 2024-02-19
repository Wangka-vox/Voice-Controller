import pyaudio
import wave
import keyboard
import whisper
import os
import webbrowser

Frame_Per_Buffer = 3200
FORMAT = pyaudio.paInt16
CHANNEL = 1
FRAME_RATE = 16000
CHUNK = 3200

audio = pyaudio.PyAudio()

stream = audio.open(
    format=FORMAT,
    channels=CHANNEL,
    rate=FRAME_RATE,
    input=True,
    frames_per_buffer=CHUNK
)


# Recording audio
def start_recording():
    frames = []
    print("start recording")
    while keyboard.is_pressed('ctrl') and keyboard.is_pressed('i'):
        data = stream.read(CHUNK)
        frames.append(data)
    # Save recorded audio to a file
    wf = wave.open("recorded_audio.wav", "wb")
    wf.setnchannels(CHANNEL)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(FRAME_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

print("standby...")
keyboard.wait('ctrl+i')
start_recording()

# Terminate the PyAudio object and stop streaming
stream.stop_stream()
stream.close()
audio.terminate()


# Transcribe audio

model = whisper.load_model("base")
result = model.transcribe("recorded_audio.wav", fp16=False)
text = result["text"]
print(text)


# registing webbrowser



#open application
if text.__contains__('steam') or text.__contains__('Steam'):
    os.startfile('C:\Program Files (x86)\Steam\Steam.exe')
elif text.__contains__('Elden Ring') or text.__contains__('elden ring'):
    os.startfile('D:\SteamLibrary\steamapps\common\ELDEN RING\Game\eldenring.exe')
elif text.__contains__('Discord') or text.__contains__('discord'):
    os.startfile(r'C:\Users\VO DINH QUANG\Desktop\Discord')
elif text.__contains__('Google') or text.__contains__('google'):
    os.startfile(r'C:\Users\Public\Desktop\Google Chrome')
