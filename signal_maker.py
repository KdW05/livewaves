import numpy as np

class PureSignal:
    def __init__(self, sampling_rate: int, frequency: float, initial_phase: float = 0.0, duration: float = 1.0, label: str = "") -> None:
        self.sampling_rate = sampling_rate
        self.frequency = frequency
        self.current_phase = 0.0
        self.label = label

        self.signal: np.ndarray = np.array([], dtype=float)
        self.generate(duration)

    def generate(self, duration: float):
        n_samples = int(self.sampling_rate * duration)
        time = np.arange(n_samples) / self.sampling_rate

        phase = 2*np.pi*self.frequency*time + self.current_phase
        new_signal_segment = np.sin(phase)

        self.current_phase =  (phase[-1] + 2*np.pi*self.frequency/self.sampling_rate) % (2*np.pi)
        self.signal = np.concatenate([self.signal, new_signal_segment])
        self.normalize()

    def normalize(self):
        self.signal /= np.max(np.abs(self.signal))
        
    def extend_duration(self, duration: float):
        self.generate(duration)

    def amplify(self, gain: float = 1.0):
        self.signal *= gain
    
class NonPureSignal:
    def __init__(self, signals: np.ndarray) -> None:
        self.signals_array = signals

        self.combined_signal = np.array([], dtype=float)
        self.sum_signals()
    
    def normalize(self):
        self.combined_signal /= np.max(np.abs(self.combined_signal))

    def sum_signals(self):
        temp_array = np.array([x.signal for x in self.signals_array])
        self.combined_signal = temp_array.sum(axis=0)
        self.normalize()
        

    def add_signal(self, signal: np.ndarray):
        self.signals_array = np.concatenate([self.signals_array, signal])
        self.sum_signals()





    

    