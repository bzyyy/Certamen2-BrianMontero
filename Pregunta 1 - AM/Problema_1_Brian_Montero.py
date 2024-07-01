#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Problema_1_Brian_Montero
# Author: Brian Montero
# GNU Radio version: 3.10.7.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import Problema_1_Brian_Montero_epy_block_0_0 as epy_block_0_0  # embedded python block
import Problema_1_Brian_Montero_epy_block_0_0_0 as epy_block_0_0_0  # embedded python block
import Problema_1_Brian_Montero_epy_block_0_0_1 as epy_block_0_0_1  # embedded python block
import Problema_1_Brian_Montero_epy_block_0_0_2 as epy_block_0_0_2  # embedded python block
import sip



class Problema_1_Brian_Montero(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Problema_1_Brian_Montero", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Problema_1_Brian_Montero")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Problema_1_Brian_Montero")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.volumen = volumen = 0.1
        self.samp_rate = samp_rate = 48e3
        self.modulacion = modulacion = 0.02
        self.choose = choose = 0

        ##################################################
        # Blocks
        ##################################################

        self._volumen_range = Range(0.1, 1.5, 0.1, 0.1, 200)
        self._volumen_win = RangeWidget(self._volumen_range, self.set_volumen, "volumen", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._volumen_win)
        self._modulacion_range = Range(0.01, 1, 0.01, 0.02, 200)
        self._modulacion_win = RangeWidget(self._modulacion_range, self.set_modulacion, "modulacion", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._modulacion_win)
        # Create the options list
        self._choose_options = [0, 1, 2, 3]
        # Create the labels list
        self._choose_labels = ['Pedro', 'Discurso Sam', 'Un violinista en tu tejado', 'Discruso 300']
        # Create the combo box
        self._choose_tool_bar = Qt.QToolBar(self)
        self._choose_tool_bar.addWidget(Qt.QLabel("choose" + ": "))
        self._choose_combo_box = Qt.QComboBox()
        self._choose_tool_bar.addWidget(self._choose_combo_box)
        for _label in self._choose_labels: self._choose_combo_box.addItem(_label)
        self._choose_callback = lambda i: Qt.QMetaObject.invokeMethod(self._choose_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._choose_options.index(i)))
        self._choose_callback(self.choose)
        self._choose_combo_box.currentIndexChanged.connect(
            lambda i: self.set_choose(self._choose_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._choose_tool_bar)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            128, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0_2 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                3e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                3e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                3e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                3e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self.high_pass_filter_0_2 = filter.fir_filter_fff(
            1,
            firdes.high_pass(
                1,
                samp_rate,
                30,
                10,
                window.WIN_HAMMING,
                6.76))
        self.high_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.high_pass(
                1,
                samp_rate,
                30,
                10,
                window.WIN_HAMMING,
                6.76))
        self.high_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.high_pass(
                1,
                samp_rate,
                30,
                10,
                window.WIN_HAMMING,
                6.76))
        self.high_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.high_pass(
                1,
                samp_rate,
                30,
                10,
                window.WIN_HAMMING,
                6.76))
        self.epy_block_0_0_2 = epy_block_0_0_2.am_demod(mod_index=modulacion)
        self.epy_block_0_0_1 = epy_block_0_0_1.am_demod(mod_index=modulacion)
        self.epy_block_0_0_0 = epy_block_0_0_0.am_demod(mod_index=modulacion)
        self.epy_block_0_0 = epy_block_0_0.am_demod(mod_index=modulacion)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('D:\\Universidad\\2024-1\\LABCOM\\Certamen2\\prueba_audio_1', True)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_selector_0_0 = blocks.selector(gr.sizeof_float*1,choose,0)
        self.blocks_selector_0_0.set_enabled(True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_float*1,choose,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(volumen)
        self.band_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                18e3,
                22e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                13e3,
                17e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                7e3,
                11e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                3e3,
                7e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(48000, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.epy_block_0_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.epy_block_0_0_0, 0))
        self.connect((self.band_pass_filter_0_0_0, 0), (self.epy_block_0_0_1, 0))
        self.connect((self.band_pass_filter_0_1, 0), (self.epy_block_0_0_2, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_selector_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_0_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.epy_block_0_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.epy_block_0_0_1, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.epy_block_0_0_2, 0), (self.low_pass_filter_0_2, 0))
        self.connect((self.high_pass_filter_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.high_pass_filter_0, 0), (self.blocks_selector_0_0, 1))
        self.connect((self.high_pass_filter_0_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.high_pass_filter_0_0, 0), (self.blocks_selector_0_0, 0))
        self.connect((self.high_pass_filter_0_1, 0), (self.blocks_selector_0, 2))
        self.connect((self.high_pass_filter_0_1, 0), (self.blocks_selector_0_0, 2))
        self.connect((self.high_pass_filter_0_2, 0), (self.blocks_selector_0, 3))
        self.connect((self.high_pass_filter_0_2, 0), (self.blocks_selector_0_0, 3))
        self.connect((self.low_pass_filter_0, 0), (self.high_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.high_pass_filter_0_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.high_pass_filter_0_1, 0))
        self.connect((self.low_pass_filter_0_2, 0), (self.high_pass_filter_0_2, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Problema_1_Brian_Montero")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_volumen(self):
        return self.volumen

    def set_volumen(self, volumen):
        self.volumen = volumen
        self.blocks_multiply_const_vxx_0.set_k(self.volumen)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 3e3, 7e3, 1e3, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, 7e3, 11e3, 1e3, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(1, self.samp_rate, 13e3, 17e3, 1e3, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(1, self.samp_rate, 18e3, 22e3, 1e3, window.WIN_HAMMING, 6.76))
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, 30, 10, window.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0.set_taps(firdes.high_pass(1, self.samp_rate, 30, 10, window.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_1.set_taps(firdes.high_pass(1, self.samp_rate, 30, 10, window.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_2.set_taps(firdes.high_pass(1, self.samp_rate, 30, 10, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 3e3, 1e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 3e3, 1e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, 3e3, 1e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_2.set_taps(firdes.low_pass(1, self.samp_rate, 3e3, 1e3, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_modulacion(self):
        return self.modulacion

    def set_modulacion(self, modulacion):
        self.modulacion = modulacion
        self.epy_block_0_0.mod_index = self.modulacion
        self.epy_block_0_0_0.mod_index = self.modulacion
        self.epy_block_0_0_1.mod_index = self.modulacion
        self.epy_block_0_0_2.mod_index = self.modulacion

    def get_choose(self):
        return self.choose

    def set_choose(self, choose):
        self.choose = choose
        self._choose_callback(self.choose)
        self.blocks_selector_0.set_input_index(self.choose)
        self.blocks_selector_0_0.set_input_index(self.choose)




def main(top_block_cls=Problema_1_Brian_Montero, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
