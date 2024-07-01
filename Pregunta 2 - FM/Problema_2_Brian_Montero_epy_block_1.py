import numpy as np
from gnuradio import gr

class FM_Modulator_Block(gr.sync_block):
    def __init__(self, fc1=5e3, fc2=10e3, fc3=15e3, fc4=20e3, sample_rate=48e3, kf=1.0):
        """
        Parameteros:
        - fc1, fc2, fc3, fc4: Frecuencias de portadora para cada una de las 4 señales.
        """
        gr.sync_block.__init__(
            self,
            name='FM Modulator Block',   # Nombre que se mostrará en GRC
            in_sig=[np.float32, np.float32, np.float32, np.float32],  # 4 entradas de señales de audio
            out_sig=[np.complex64]  # Salida de la señal combinada modulada en frecuencia
        )
        self.fc = [fc1, fc2, fc3, fc4]
        self.sample_rate = sample_rate
        self.kf = kf

    def work(self, input_items, output_items):
        """
        El trabajo del bloque: modula cada señal en frecuencia y suma las señales moduladas.
        """
        audio_signals = np.array(input_items)  # Convertir las señales de entrada en un array de numpy
        output = np.zeros(len(audio_signals[0]), dtype=np.complex64)  # Inicializar la salida

        t = np.arange(len(audio_signals[0])) / self.sample_rate  # Calcular el vector de tiempo

        for i in range(4):
            audio_signal = audio_signals[i]  # Obtener la señal de audio
            carrier_freq = self.fc[i]  # Obtener la frecuencia de la portadora
            # Modulación en frecuencia
            modulated_signal = np.exp(1j * (2 * np.pi * carrier_freq * t + self.kf * np.cumsum(audio_signal) / self.sample_rate))
            output += modulated_signal  # Sumar la señal modulada

        output_items[0][:] = output  # Escribir el resultado en el buffer de salida
        return len(output_items[0])  # Retornar el número de muestras procesadas
