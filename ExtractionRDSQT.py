#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Extraction du RDSQT
# Generated: Thu May  7 14:46:27 2015
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import osmosdr
import sip
import sys

from distutils.version import StrictVersion
class ExtractionRDSQT(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Extraction du RDSQT")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Extraction du RDSQT")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
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

        self.settings = Qt.QSettings("GNU Radio", "ExtractionRDSQT")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 8
        self.transition = transition = 25e3
        self.samp_rate = samp_rate = 1e6
        self.quadrature = quadrature = 500e3
        self.frequency = frequency = 96.6
        self.echantillon = echantillon = 4
        self.cutoff = cutoff = 75e3

        ##################################################
        # Blocks
        ##################################################
        self._volume_layout = Qt.QVBoxLayout()
        self._volume_label = Qt.QLabel("volume")
        self._volume_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._volume_slider.setRange(0, 100, 101)
        self._volume_slider.setValue(self.volume)
        self._volume_slider.setMinimumWidth(200)
        self._volume_slider.valueChanged.connect(self.set_volume)
        self._volume_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._volume_layout.addWidget(self._volume_label)
        self._volume_layout.addWidget(self._volume_slider)
        self.top_layout.addLayout(self._volume_layout)
        self._frequency_layout = Qt.QVBoxLayout()
        self._frequency_label = Qt.QLabel("frequency")
        self._frequency_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._frequency_slider.setRange(87.5, 108, 205)
        self._frequency_slider.setValue(self.frequency)
        self._frequency_slider.setMinimumWidth(200)
        self._frequency_slider.valueChanged.connect(self.set_frequency)
        self._frequency_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._frequency_layout.addWidget(self._frequency_label)
        self._frequency_layout.addWidget(self._frequency_slider)
        self.top_layout.addLayout(self._frequency_layout)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(frequency*1e6, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(20, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=int(48e3),
                decimation=int(quadrature),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	1024, #size
        	quadrature, #samp_rate
        	"19x3", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(2, firdes.low_pass(
        	1, samp_rate, cutoff, transition, firdes.WIN_HAMMING, 6.76))
        self._echantillon_layout = Qt.QVBoxLayout()
        self._echantillon_label = Qt.QLabel("echantillon")
        self._echantillon_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._echantillon_slider.setRange(1, 32, 33)
        self._echantillon_slider.setValue(self.echantillon)
        self._echantillon_slider.setMinimumWidth(200)
        self._echantillon_slider.valueChanged.connect(self.set_echantillon)
        self._echantillon_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._echantillon_layout.addWidget(self._echantillon_label)
        self._echantillon_layout.addWidget(self._echantillon_slider)
        self.top_layout.addLayout(self._echantillon_layout)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.band_pass_filter_3 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, quadrature, 18.5e3, 19.5e3, 1000, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=quadrature,
        	audio_decimation=1,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.band_pass_filter_3, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.band_pass_filter_3, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.band_pass_filter_3, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.band_pass_filter_3, 0), (self.blocks_multiply_xx_1, 2))
        self.connect((self.blocks_multiply_xx_1, 0), (self.qtgui_time_sink_x_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ExtractionRDSQT")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))
        Qt.QMetaObject.invokeMethod(self._volume_slider, "setValue", Qt.Q_ARG("double", self.volume))

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_quadrature(self):
        return self.quadrature

    def set_quadrature(self, quadrature):
        self.quadrature = quadrature
        self.band_pass_filter_3.set_taps(firdes.band_pass(1, self.quadrature, 18.5e3, 19.5e3, 1000, firdes.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_1.set_samp_rate(self.quadrature)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.rtlsdr_source_0.set_center_freq(self.frequency*1e6, 0)
        Qt.QMetaObject.invokeMethod(self._frequency_slider, "setValue", Qt.Q_ARG("double", self.frequency))

    def get_echantillon(self):
        return self.echantillon

    def set_echantillon(self, echantillon):
        self.echantillon = echantillon
        Qt.QMetaObject.invokeMethod(self._echantillon_slider, "setValue", Qt.Q_ARG("double", self.echantillon))

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = ExtractionRDSQT()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
