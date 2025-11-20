import numpy as np

class BaseSignal:
    def __init__(self):
        self.signal = np.array([], dtype=float)

    def normalize_signal(self):
        if np.max(np.abs(self.signal)) != 0:
            self.signal /= np.max(np.abs(self.signal))

    def amplify_signal(self, gain: float):
        self.signal *= gain
    
    def pad_signal(self, pad_value: float, pad_amount: int, pad_position: int):
        padded_signal = np.concatenate([self.signal[:pad_position], np.array([pad_value for i in range(pad_amount)]), self.signal[pad_position:]])
        self.signal = padded_signal

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
    def __init__(self, signals = None, label: str = "", composition_method: str = "cut", normalize: bool = True) -> None:
        super().__init__()
        self.signals_obj_array = signals if signals is not None else []
        self.label = label
        self.normalize = normalize

        self.match_signal_lengths(composition_method)
        self.sum_signals()

    def sum_signals(self):
        temp_list = np.array([x.signal for x in self.signals_obj_array])
        self.signal = temp_list.sum(axis=0)
        
        if self.normalize:
            self.normalize_signal()
    
    def match_signal_lengths(self, composition_method):
        signal_lengths = [len(x.signal) for x in self.signals_obj_array]
        #TODO Optimize by early return if all signal lengths are the same
        match composition_method:
            case "pad after": # Pads every signal with 0 at end of signal to match longest signal length
                matching_length = np.max(signal_lengths)
                pad_amounts = [(matching_length - current_signal_length) for current_signal_length in signal_lengths]
                for i, signal_obj in enumerate(self.signals_obj_array):
                    signal_obj.pad_signal(pad_value=0, pad_amount=pad_amounts[i], pad_position=-1)
                # for i, v in enumerate(pad_amounts):
                #     self.signals_obj_array[i].signal.pad_signal(pad_value=0, pad_amount=v, pad_position=-1)

            case "pad before": # Pads every signal with 0 at beginning of signal to match longest signal length
                matching_length = np.max(signal_lengths)
                pad_amounts = [(matching_length - current_signal_length) for current_signal_length in signal_lengths]
                for i, signal_obj in enumerate(self.signals_obj_array):
                    signal_obj.pad_signal(pad_value=0, pad_amount=pad_amounts[i], pad_position=0)
                # for i, v in enumerate(pad_amounts):
                #     self.signals_obj_array[i].signal.pad_signal(pad_value=0, pad_amount=v, pad_position=0)
                       

            case "cut": # Changes all signals lengths to the shortest signal 
                matching_length = np.min(signal_lengths)
                for i, signal_obj in enumerate(self.signals_obj_array):
                    signal_obj.signal = signal_obj.signal[:matching_length]

            case "match": 
                #TODO changes all signals lengths to the longest signal 
                pass

    def add_signal(self, new_signal_obj, composition_method = "cut"):
        self.signals_obj_array = np.concatenate([self.signals_obj_array, new_signal_obj])
        self.match_signal_lengths(composition_method)
  
        self.sum_signals()




    

    