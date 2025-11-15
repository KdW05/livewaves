import soundcard as sc
import numpy as np

speakers = sc.all_speakers()
default_speaker = sc.default_speaker()
print(default_speaker)