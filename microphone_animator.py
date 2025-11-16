import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

BLOCKSIZE: int = 64
SAMPLE_RATE: int = 48000
INTERVAL: float = BLOCKSIZE / SAMPLE_RATE
GAIN: float = 1


stream = sd.InputStream(samplerate=SAMPLE_RATE, blocksize=BLOCKSIZE, channels=1)

stream.start()

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

ax.set_xlim(0, BLOCKSIZE)
ax.set_ylim(-.1, .1)
ax.set_xlabel("Sample")
ax.set_ylabel("Amplitude")
ax.set_title("Live Microphone Waveform")

def animate(frame):
    audio_data, overflow = stream.read(BLOCKSIZE)
    samples: np.ndarray = audio_data.flatten()
    samples *= GAIN

    line.set_data(np.arange(BLOCKSIZE), samples)
    return line,


anim = animation.FuncAnimation(fig, animate, interval=INTERVAL, blit=True)

plt.show()
