
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
import librosa
import soundfile as sf

# ========== Configurações ==========
AUDIO_PATH = 'audio.wav'  # arquivo WAV mono
CORTE_PB = 1000           # Hz
CORTE_PA = 3000           # Hz
CORTE_BB = (1000, 3000)   # Hz

# ========== Leitura do Áudio ==========
signal, sample_rate = librosa.load(AUDIO_PATH, sr=None)
tempo = np.linspace(0, len(signal)/sample_rate, num=len(signal))

print(f"\nÁudio carregado: {AUDIO_PATH}")
print(f"Taxa de amostragem: {sample_rate} Hz | Duração: {len(signal)/sample_rate:.2f} s")

# ========== Funções ==========
def butter_filter(signal, sample_rate, tipo='low', cutoff_low=1000, cutoff_high=None, ordem=5):
    nyq = 0.5 * sample_rate
    if tipo == 'low':
        b, a = butter(ordem, cutoff_low / nyq, btype='low')
    elif tipo == 'high':
        b, a = butter(ordem, cutoff_low / nyq, btype='high')
    elif tipo == 'band':
        b, a = butter(ordem, [cutoff_low / nyq, cutoff_high / nyq], btype='band')
    else:
        raise ValueError("Tipo de filtro inválido")
    return lfilter(b, a, signal)

def salva_audio(nome, sinal, sr):
    sf.write(nome, sinal, sr)
    print(f"Áudio exportado como: {nome}")

def dashboard(signal, sample_rate, pb, pa, bb):
    tempo = np.linspace(0, len(signal)/sample_rate, num=len(signal))
    freq = np.fft.fftfreq(len(signal), d=1/sample_rate)

    fft_original = np.fft.fft(signal)
    fft_pb = np.fft.fft(pb)
    fft_pa = np.fft.fft(pa)
    fft_bb = np.fft.fft(bb)

    fig, axs = plt.subplots(4, 2, figsize=(15, 12))
    fig.suptitle("📊 Análise Completa de Sinais – Tempo vs Frequência", fontsize=16)

    # Sinal original
    axs[0, 0].plot(tempo, signal)
    axs[0, 0].set_title("Sinal Original (Tempo)")
    axs[0, 0].set_xlabel("Tempo [s]")

    axs[0, 1].plot(freq[:len(freq)//2], np.abs(fft_original)[:len(freq)//2])
    axs[0, 1].set_title("Espectro Original")
    axs[0, 1].set_xlabel("Frequência [Hz]")

    # Passa-Baixa
    axs[1, 0].plot(tempo, pb)
    axs[1, 0].set_title("Passa-Baixa (Tempo)")

    axs[1, 1].plot(freq[:len(freq)//2], np.abs(fft_pb)[:len(freq)//2])
    axs[1, 1].set_title("Espectro Passa-Baixa")

    # Passa-Alta
    axs[2, 0].plot(tempo, pa)
    axs[2, 0].set_title("Passa-Alta (Tempo)")

    axs[2, 1].plot(freq[:len(freq)//2], np.abs(fft_pa)[:len(freq)//2])
    axs[2, 1].set_title("Espectro Passa-Alta")

    # Passa-Banda
    axs[3, 0].plot(tempo, bb)
    axs[3, 0].set_title("Passa-Banda (Tempo)")
    axs[3, 0].set_xlabel("Tempo [s]")

    axs[3, 1].plot(freq[:len(freq)//2], np.abs(fft_bb)[:len(freq)//2])
    axs[3, 1].set_title("Espectro Passa-Banda")
    axs[3, 1].set_xlabel("Frequência [Hz]")

    for ax in axs.flat:
        ax.grid(True)

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.show()

# ========== Aplicar Filtros ==========
pb = butter_filter(signal, sample_rate, tipo='low', cutoff_low=CORTE_PB)
pa = butter_filter(signal, sample_rate, tipo='high', cutoff_low=CORTE_PA)
bb = butter_filter(signal, sample_rate, tipo='band', cutoff_low=CORTE_BB[0], cutoff_high=CORTE_BB[1])

# ========== Salvar os áudios filtrados ==========
salva_audio("saida_passa_baixa.wav", pb, sample_rate)
salva_audio("saida_passa_alta.wav", pa, sample_rate)
salva_audio("saida_passa_banda.wav", bb, sample_rate)

# ========== Visualização ==========
dashboard(signal, sample_rate, pb, pa, bb)
