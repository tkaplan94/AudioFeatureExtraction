import matplotlib.pyplot as plt
import librosa.display
import os
import glob


def find_zerocrossings(sample):
    print("Zero Crossings")
    print("-----------------------------------------------")
    zero_crossings = librosa.zero_crossings(sample, pad=False)
    print("shape: ", end='')
    print(zero_crossings.shape)
    print("print: ", end='')
    print(zero_crossings)
    print("sum:   ", end='')
    print(sum(zero_crossings))
    print("avg:   ", end='')
    print(sum(zero_crossings) / len(zero_crossings))
    print()


def find_decibels(sample):
    print("Amplitude to dB")
    print("-----------------------------------------------")
    decibels = librosa.amplitude_to_db(sample)
    print("shape: ", end='')
    print(decibels.shape)
    print("print: ", end='')
    print(decibels)
    print("sum:   ", end='')
    print(abs(sum(decibels)))
    print("avg:   ", end='')
    print(abs(sum(decibels) / len(decibels)))
    print()


def find_stft(sample):
    print("STFT")
    print("-----------------------------------------------")
    stft = librosa.stft(sample)
    print("shape: ", end='')
    print(stft.shape)

    print()


def find_fouriertempogram(sample):
    print("Fourier Tempogram")
    print("-----------------------------------------------")
    ftempogram = librosa.feature.fourier_tempogram(sample)
    print("shape: ", end='')
    print(ftempogram.shape)

    print()

directory =
data, sampling_rate = librosa.load(directory, sr=44100)

# # DISPLAY: Waveform
# fig = plt.figure(figsize=(10, 5))
# fig.canvas.set_window_title(os.path.basename(audio_path))
# librosa.display.waveplot(data, sr=sampling_rate)
# plt.show()

# # DISPLAY: Spectrogram
# fig = plt.figure(figsize=(10, 5))
# fig.canvas.set_window_title(os.path.basename(audio_path))
# X = librosa.stft(data)
# Xdb = librosa.amplitude_to_db(abs(X))
# librosa.display.specshow(Xdb, sr=sampling_rate, x_axis='time', y_axis='hz')
# plt.colorbar()
# plt.show()

# ANALYZE: call functions with 'data' as argument
print()
