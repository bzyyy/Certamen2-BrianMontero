import numpy as np
from gnuradio import gr

class am_demod(gr.sync_block):
    def __init__(self, mod_index=1.0):
        gr.sync_block.__init__(
            self,
            name="AM Demod",
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.mod_index = mod_index

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        # AM demodulation: absolute value of the signal divided by the modulation index
        out[:] = np.abs(in0) / self.mod_index

        return len(output_items[0])
