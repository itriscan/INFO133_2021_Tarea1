import numpy as np
import scipy.io.wavfile as waves

archivo = 'audiodeballenancpq.wav'
fsonido, sonido = waves.read(archivo)

print(fsonido)

print(sonido)