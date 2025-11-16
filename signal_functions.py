import numpy as np
import matplotlib.pyplot as plt

def plot_signal_timedomain(signal: np.ndarray, sampling_rate: int, title="Signal in Time Domain"):
    t = np.arange(len(signal)) / sampling_rate
    plt.figure(figsize=(12, 4))
    plt.plot(t, signal)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_fft(signal: np.ndarray, sampling_rate: int, title="Signal its FFT"):
    N = len(signal)
    fft_vals = np.fft.fft(signal)
    fft_mag = np.abs(fft_vals) / N

    freqs = np.fft.fftfreq(N, 1/sampling_rate)

    idx = freqs >= 0
    freqs = freqs[idx]
    fft_mag = fft_mag[idx]

    plt.figure(figsize=(12, 4))
    plt.plot(freqs[::1], fft_mag[::1])
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title(title)
    plt.grid(True)
    plt.show()

