import sounddevice as sd
import numpy as np
import matplotlib.pyplot as  plt
import matplotlib.animation as animation
import signal_maker as sm

BLOCKSIZE: int = 1024
SAMPLING_RATE: int = 44100
GAIN: float = 0.3

stream = sd.OutputStream(samplerate=SAMPLING_RATE, blocksize=BLOCKSIZE, channels=1)
stream.start()

A_note = sm.PureSignal(SAMPLING_RATE, 440, 0.0, 3, "A")
Csharp_note = sm.PureSignal(SAMPLING_RATE, 554.37, 0.0, 3, "Csharp")
E_note = sm.PureSignal(SAMPLING_RATE, 659.26, 0.0, 3, "E")

Amajor_chord = sm.CompositeSignal(np.array([A_note, Csharp_note, E_note]))

plt.figure(figsize=(17,4))
plt.plot(Amajor_chord.signal)
ax = plt.gca()
ax.set_ylim([-3,3])
ax.set_xlim([0, 1000])
# plt.show()


stream.write(np.ascontiguousarray(Amajor_chord.signal, dtype='float32'))

