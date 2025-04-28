import sounddevice as sd
from scipy.io.wavfile import write 

fs = 44100  # Sample rate (44.1kHz = CD quality)
seconds = int(input("Enter the time duration in seconds: "))  

print("Recording... 🎙️")

# Record audio
record_voice = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='int16')
sd.wait()  # Wait until recording is finished

# Save the recorded audio to a WAV file
write("out.wav", fs, record_voice)

print("Finished 🎉\nPlease check 'out.wav' in your folder.")
