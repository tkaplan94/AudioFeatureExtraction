import librosa.display


def find_zerocrossings(sample):
    print("Zero Crossings")
    print("-----------------------------------------------")
    zero_crossings = librosa.zero_crossings(sample, pad=False)
    print("type:  ", end='')
    print(type(zero_crossings))
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
    print("type:  ", end='')
    print(type(decibels))
    print("print: ", end='')
    print(decibels)
    print("sum:   ", end='')
    print(sum(decibels))
    print("avg:   ", end='')
    print(sum(decibels) / len(decibels))
    print()


def find_tempogram(sample):
    print("Tempogram")
    print("-----------------------------------------------")
    tempogram = librosa.feature.tempogram(sample)
    print("type:  ", end='')
    print(type(tempogram))
    print("print: ")
    print(tempogram)
    print("sum:   ")
    print(sum(tempogram))
    print("avg:   ")
    print(sum(tempogram) / len(tempogram))
    print()


def find_fouriertempogram(sample):
    print("Fourier Tempogram")
    print("-----------------------------------------------")
    ftempogram = librosa.feature.fourier_tempogram(sample)
    print("type:  ", end='')
    print(type(ftempogram))
    print("print: ")
    print(ftempogram)
    print("sum:   ")
    print(sum(ftempogram))
    print("avg:   ")
    print(sum(ftempogram) / len(ftempogram))
    print()


audio_path =
data, sampling_rate = librosa.load(audio_path, sr=44100)

# DISPLAY: Waveform
# plt.figure(figsize=(10, 5))
# librosa.display.waveplot(data, sr=sampling_rate)
# plt.show()

# DISPLAY: Spectrogram
# plt.figure(figsize=(10, 5))
# X = librosa.stft(data)
# Xdb = librosa.amplitude_to_db(abs(X))
# librosa.display.specshow(Xdb, sr=sampling_rate, x_axis='time', y_axis='hz')
# plt.colorbar()
# plt.show()

# ANALYZE: call functions with 'data' as argument
print()
