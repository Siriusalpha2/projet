#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Tutorial Two 1
# Generated: Mon Mar 16 10:54:14 2015
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import sip
import sys

from distutils.version import StrictVersion
class tutorial_two_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Tutorial Two 1")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Tutorial Two 1")
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

        self.settings = Qt.QSettings("GNU Radio", "tutorial_two_1")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.radio = radio = 0
        self.frequency = frequency = 1000

        ##################################################
        # Blocks
        ##################################################
        self.tabQT = Qt.QTabWidget()
        self.tabQT_widget_0 = Qt.QWidget()
        self.tabQT_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabQT_widget_0)
        self.tabQT_grid_layout_0 = Qt.QGridLayout()
        self.tabQT_layout_0.addLayout(self.tabQT_grid_layout_0)
        self.tabQT.addTab(self.tabQT_widget_0, "Time")
        self.tabQT_widget_1 = Qt.QWidget()
        self.tabQT_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabQT_widget_1)
        self.tabQT_grid_layout_1 = Qt.QGridLayout()
        self.tabQT_layout_1.addLayout(self.tabQT_grid_layout_1)
        self.tabQT.addTab(self.tabQT_widget_1, "Frequency")
        self.top_layout.addWidget(self.tabQT)
        self._radio_options = (0, 1, 2, 3, 4, )
        self._radio_labels = ("Cosinus signal", "Jungle", "Breathe", "Desert", "Battle", )
        self._radio_group_box = Qt.QGroupBox("radio")
        self._radio_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._radio_button_group = variable_chooser_button_group()
        self._radio_group_box.setLayout(self._radio_box)
        for i, label in enumerate(self._radio_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._radio_box.addWidget(radio_button)
        	self._radio_button_group.addButton(radio_button, i)
        self._radio_callback = lambda i: Qt.QMetaObject.invokeMethod(self._radio_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._radio_options.index(i)))
        self._radio_callback(self.radio)
        self._radio_button_group.buttonClicked[int].connect(
        	lambda i: self.set_radio(self._radio_options[i]))
        self.top_layout.addWidget(self._radio_group_box)
        self._frequency_layout = Qt.QVBoxLayout()
        self._frequency_tool_bar = Qt.QToolBar(self)
        self._frequency_layout.addWidget(self._frequency_tool_bar)
        self._frequency_tool_bar.addWidget(Qt.QLabel("frequency"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._frequency_counter = qwt_counter_pyslot()
        self._frequency_counter.setRange(20, 20000, 100)
        self._frequency_counter.setNumButtons(2)
        self._frequency_counter.setValue(self.frequency)
        self._frequency_tool_bar.addWidget(self._frequency_counter)
        self._frequency_counter.valueChanged.connect(self.set_frequency)
        self._frequency_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._frequency_slider.setRange(20, 20000, 100)
        self._frequency_slider.setValue(self.frequency)
        self._frequency_slider.setMinimumWidth(200)
        self._frequency_slider.valueChanged.connect(self.set_frequency)
        self._frequency_layout.addWidget(self._frequency_slider)
        self.top_layout.addLayout(self._frequency_layout)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        
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
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabQT_layout_0.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabQT_layout_1.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_wavfile_source_3 = blocks.wavfile_source("/home/raph/projet/desert.wav", True)
        self.blocks_wavfile_source_2 = blocks.wavfile_source("/home/raph/projet/seabattle_loop.wav", True)
        self.blocks_wavfile_source_1 = blocks.wavfile_source("/home/raph/projet/BreathingInMask.wav", True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/raph/projet/jungle.wav", True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=5,
        	num_outputs=1,
        	input_index=radio,
        	output_index=0,
        )
        self.audio_sink_0 = audio.sink(samp_rate, "", True)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, frequency, 0.1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_wavfile_source_1, 0), (self.blks2_selector_0, 2))
        self.connect((self.blocks_wavfile_source_3, 0), (self.blks2_selector_0, 3))
        self.connect((self.blocks_wavfile_source_2, 0), (self.blks2_selector_0, 4))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blks2_selector_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blks2_selector_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tutorial_two_1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_radio(self):
        return self.radio

    def set_radio(self, radio):
        self.radio = radio
        self.blks2_selector_0.set_input_index(int(self.radio))
        self._radio_callback(self.radio)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.analog_sig_source_x_0.set_frequency(self.frequency)
        Qt.QMetaObject.invokeMethod(self._frequency_counter, "setValue", Qt.Q_ARG("double", self.frequency))
        Qt.QMetaObject.invokeMethod(self._frequency_slider, "setValue", Qt.Q_ARG("double", self.frequency))

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
    tb = tutorial_two_1()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
