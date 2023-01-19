import wave
import numpy as np

frequency = 1000
duration = 100
fs = 44100

sine_wave = np.array([np.sin(2 * np.pi * frequency * x/fs) for x in range(duration*fs)])
scaled_sine_wave = (2 ** 15 - 1) * sine_wave #for scaling the amplitud

wf=wave.open("typewriterSoundEffect.wav", "w")
wf.setparams((1, 2, fs, 0, "NONE", "Not compressed"))
wf.writeframes(scaled_sine_wave.astype(np.int16))
wf.close()

print("sring")
