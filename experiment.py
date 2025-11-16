import sounddevice as sd
import numpy as np
import matplotlib.pyplot as  plt
import matplotlib.animation as animation
import signal_maker

BLOCKSIZE: int = 1024
SAMPLING_RATE: int = 44100
GAIN: float = 0.3

stream = sd.OutputStream(samplerate=SAMPLING_RATE, blocksize=BLOCKSIZE, channels=1)


A_note = signal_maker.amplify(signal_maker.create_sinesignal(SAMPLING_RATE, 440), GAIN)
Csharp_note = signal_maker.amplify(signal_maker.create_sinesignal(SAMPLING_RATE, 554.37), GAIN)
E_note = signal_maker.amplify(signal_maker.create_sinesignal(SAMPLING_RATE, 659.26), GAIN)

Amajor_chord = signal_maker.sum_signals(np.array([A_note, Csharp_note, E_note]))
Amajor_chord = signal_maker.amplify(Amajor_chord, GAIN)

plt.figure(figsize=(17,4))
plt.plot(A_note)
ax = plt.gca()
ax.set_ylim([-3,3])
ax.set_xlim([0, 440])
# plt.show()
print(A_note[-1])

stream.start()
stream.write(np.ascontiguousarray(Amajor_chord, dtype='float32'))

