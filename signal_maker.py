import numpy as np

class BaseSignal:
    def __init__(self):
        self.signal = np.array([], dtype=float)

    def normalize_signal(self):
        if np.max(np.abs(self.signal)) != 0:
            self.signal /= np.max(np.abs(self.signal))

    def amplify_signal(self, gain: float):
        self.signal *= gain

class PureSignal(BaseSignal):
    def __init__(self, sampling_rate: int, frequency: float, 
                 amplitude: float, initial_phase: float = 0.0, 
                 duration: float = 1.0, label: str = "",
                 normalize: bool = True) -> None:
        
        super().__init__()
        self.sampling_rate = sampling_rate
        self.frequency = frequency
        self.amplitude = amplitude
        self.initial_phase = initial_phase
        self.label = label
        self.normalize = normalize

        self.generate_signal(duration)

    def generate_signal(self, duration: float):
        n_samples = int(self.sampling_rate * duration)
        time = np.arange(n_samples) / self.sampling_rate

        generated_signal = self.amplitude * np.sin(2*np.pi*self.frequency*time + self.initial_phase)
        self.signal = generated_signal

        if self.normalize:
            self.normalize_signal()
        
    def change_duration(self, duration: float):
        if duration < 0:
            raise Exception("Duration cannot be lower than 0")
        self.generate_signal(duration)

    
class CompositeSignal(BaseSignal):
    def __init__(self, signals = None, label: str = "", normalize: bool = True) -> None:
        super().__init__()
        self.signals_array = signals if signals is not None else []
        self.label = label
        self.normalize = normalize
        self.sum_signals()

    def sum_signals(self):
        temp_array = np.array([x.signal for x in self.signals_array])
        self.signal = temp_array.sum(axis=0)
        
        if self.normalize:
            self.normalize_signal()
        

    def add_signal(self, new_signal, composition_method = "match max"):
        self.signals_array = np.concatenate([self.signals_array, new_signal])
        
        match composition_method:
            case "pad after":  
                #TODO add padding after signal 
                pass
            case "pad before":
                #TODO add padding before signal
                pass
            case "match min":
                #TODO change self.signals_array to match smallest signal length
                pass
            case "match max":
                #TODO change self.signals_array to match largest signal length
                pass
        
        self.sum_signals()




    

    