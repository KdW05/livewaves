import numpy as np

class BaseSignal:
    def __init__(self):
        self.signal = np.array([], dtype=float)

    def normalize(self):
        if np.max(np.abs(self.signal)) != 0:
            self.signal /= np.max(np.abs(self.signal))

    def amplify(self, gain: float):
        self.signal *= gain

class PureSignal(BaseSignal):
    def __init__(self, sampling_rate: int, frequency: float, initial_phase: float = 0.0, duration: float = 1.0, label: str = "") -> None:
        super().__init__()
        self.sampling_rate = sampling_rate
        self.frequency = frequency
        self.current_phase = initial_phase
        self.label = label

        self.generate(duration)

    def generate(self, duration: float):
        n_samples = int(self.sampling_rate * duration)
        time = np.arange(n_samples) / self.sampling_rate

        phase = 2*np.pi*self.frequency*time + self.current_phase
        new_signal_segment = np.sin(phase)

        self.current_phase =  (phase[-1] + 2*np.pi*self.frequency/self.sampling_rate) % (2*np.pi)
        self.signal = np.concatenate([self.signal, new_signal_segment])
        self.normalize()
        
    def extend_duration(self, duration: float):
        self.generate(duration)

    
class CompositeSignal(BaseSignal):
    def __init__(self, signals = None, label: str = "") -> None:
        super().__init__()
        self.signals_array = signals if signals is not None else []
        self.sum_signals()

    def sum_signals(self):
        temp_array = np.array([x.signal for x in self.signals_array])
        self.signal = temp_array.sum(axis=0)
        self.normalize()
        

    def add_signal(self, new_signal: np.ndarray, composition_method = "sum"):
        self.signals_array = np.concatenate([self.signals_array, new_signal])
        
        match composition_method:
            case "sum":   
                self.sum_signals()





    

    