import sounddevice as sd
import numpy as np
import matplotlib.pyplot as  plt
import matplotlib.animation as animation
import signal_maker as sm
import signal_functions as sf

BLOCKSIZE: int = 1024
SAMPLING_RATE: int = 44100
GAIN: float = 0.3

stream = sd.OutputStream(samplerate=SAMPLING_RATE, blocksize=BLOCKSIZE, channels=1)
stream.start()

A_note = sm.PureSignal(SAMPLING_RATE, 440, 0.0, 3, "A")
Csharp_note = sm.PureSignal(SAMPLING_RATE, 554.37, 0.0, 3, "Csharp")
E_note = sm.PureSignal(SAMPLING_RATE, 659.26, 0.0, 3, "E")

Amajor_chord = sm.CompositeSignal(np.array([A_note, Csharp_note, E_note]))

sf.plot_fft(Amajor_chord.signal, SAMPLING_RATE)

exit()
stream.write(np.ascontiguousarray(Amajor_chord.signal, dtype='float32'))

