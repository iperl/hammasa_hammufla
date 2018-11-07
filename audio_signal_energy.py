import numpy as np
import matplotlib.pyplot as plt
import essentia
import essentia.standard


def audio_signal_energy(path):
    # path = '/home/illy/gdrive/aniproj/media_archive/BASS_DRUMS.mp3' # optional path
    # load audio with 44100Hz sample rate downmixed to mono
    loader = essentia.standard.MonoLoader(filename=path)
    audio = loader()  # load from loader to np ndarray
    # take only the first N seconds of the audio
    audio = audio[np.arange(44100*35)]
    audio = audio/np.max(np.abs(audio))
    F = 44100  # [Hz]
    dT = 1/F
    N = int(len(audio))
    T = np.linspace(0, (N-1)*dT, N)
    # plt.plot(T, audio)
    # plt.show()

    lenframe = int(512)
    i = 0
    Evec = np.array([])
    while True:
        k = i*lenframe
        if k+lenframe > audio.size:
            Evec = np.append(Evec, 0.0*np.ones(audio.size-k))
            break
        frame = audio[np.arange(k, k+lenframe-1)]
        # integral over the squer of the value
        E = np.trapz(frame**2)/(lenframe)
        Evec = np.append(Evec, [E]*np.ones(lenframe))
        i += 1
    Evec = Evec/np.max(Evec)  # normelize
    indxs = np.where(Evec >= 0.05)  # threshold of 15%
    oneszeros = np.arange(Evec.size)*0.0
    oneszeros[indxs] += 1
    plt.plot(T, audio)
    plt.plot(T, oneszeros)
    plt.show()
    return(oneszeros)

if __name__ == "__main__":
    audioPath = '/home/illy/gdrive/aniproj/media_archive/50_BPM_Metronome.mp3'
    audio_signal_energy(audioPath)
