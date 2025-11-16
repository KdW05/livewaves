import numpy as np

def create_sinesignal(sample_rate: int, frequency: float) -> np.ndarray:
    time = np.linspace(0, 1, sample_rate, endpoint=False)
    sine_wave = np.sin(2*np.pi * frequency * time)

    return normalize(sine_wave)

def create_cosinesignal(sample_rate: int, frequency: float) -> np.ndarray:
    time = np.linspace(0, 1, sample_rate, endpoint=False)
    cosine_wave = np.cos(2*np.pi * frequency * time)
    
    return normalize(cosine_wave)

def sum_signals(signals: np.ndarray) -> np.ndarray:
    return normalize(signals.sum(axis=0))
    

def normalize(signal: np.ndarray) -> np.ndarray:
    signal /= np.max(np.abs(signal))
    return signal

def amplify(signal: np.ndarray, gain: float) -> np.ndarray:
    return signal * gain

def change_duration(signal: np.ndarray, duration) -> np.ndarray:
    ...