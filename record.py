import sounddevice as sd
import numpy as np
import wavio

# Paramètres d'enregistrement
RATE = 16000  # Taux d'échantillonnage (16KHz)
CHANNELS = 1  # Mono
DTYPE = np.int16  # 16 bits
SECONDS = 10  # Durée de l'enregistrement, ici 5 secondes. Vous pouvez le modifier.

# Enregistrement
print("Enregistrement...")
audio = sd.rec(int(SECONDS * RATE), samplerate=RATE, channels=CHANNELS, dtype=DTYPE)

# Attendez que l'enregistrement soit terminé
sd.wait()

# Sauvegarde au format WAV
wavio.write("enregistrement.wav", audio, RATE, sampwidth=2)
print("Enregistrement terminé et sauvegardé dans 'enregistrement.wav'")