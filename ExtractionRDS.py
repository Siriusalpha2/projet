#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Extraction du RDS
# Generated: Thu Apr  9 13:21:15 2015
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class ExtractionRDS(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Extraction du RDS")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 8
        self.transition = transition = 25e3
        self.samp_rate = samp_rate = 1e6
        self.quadrature = quadrature = 500e3
        self.frequency = frequency = 96.6
        self.echantillon = echantillon = 3
        self.cutoff = cutoff = 75e3

        ##################################################
        # Blocks
        ##################################################
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label="Volume",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_volume_sizer)
        self.tab = self.tab = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.tab.AddPage(grc_wxgui.Panel(self.tab), "Time")
        self.tab.AddPage(grc_wxgui.Panel(self.tab), "Frequency")
        self.tab.AddPage(grc_wxgui.Panel(self.tab), "Waterfall")
        self.tab.AddPage(grc_wxgui.Panel(self.tab), "pb")
        self.Add(self.tab)
        _frequency_sizer = wx.BoxSizer(wx.VERTICAL)
        self._frequency_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_frequency_sizer,
        	value=self.frequency,
        	callback=self.set_frequency,
        	label="Frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._frequency_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_frequency_sizer,
        	value=self.frequency,
        	callback=self.set_frequency,
        	minimum=87.5,
        	maximum=108,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_frequency_sizer)
        _echantillon_sizer = wx.BoxSizer(wx.VERTICAL)
        self._echantillon_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_echantillon_sizer,
        	value=self.echantillon,
        	callback=self.set_echantillon,
        	label="Echantillonnage",
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._echantillon_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_echantillon_sizer,
        	value=self.echantillon,
        	callback=self.set_echantillon,
        	minimum=1,
        	maximum=32,
        	num_steps=32,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_echantillon_sizer)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_f(
        	self.tab.GetPage(2).GetWin(),
        	baseband_freq=0,
        	dynamic_range=60,
        	ref_level=-45,
        	ref_scale=2.0,
        	sample_rate=50e3,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.tab.GetPage(2).Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_scopesink2_3 = scopesink2.scope_sink_f(
        	self.tab.GetPage(3).GetWin(),
        	title="Sous porteuse 57",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.tab.GetPage(3).Add(self.wxgui_scopesink2_3.win)
        self.wxgui_scopesink2_2 = scopesink2.scope_sink_f(
        	self.tab.GetPage(0).GetWin(),
        	title="RDS",
        	sample_rate=echantillon*1187.5,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.tab.GetPage(0).Add(self.wxgui_scopesink2_2.win)
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_f(
        	self.tab.GetPage(1).GetWin(),
        	title="19",
        	sample_rate=quadrature,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.tab.GetPage(1).Add(self.wxgui_scopesink2_1.win)
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
          
        self.rational_resampler_xxx_2 = filter.rational_resampler_fff(
                interpolation=int(50e3),
                decimation=int(quadrature),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=int(48e3),
                decimation=int(quadrature),
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_2 = filter.fir_filter_fff(500, firdes.low_pass(
        	1.1875*echantillon, quadrature, 2.2e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(2, firdes.low_pass(
        	1, samp_rate, cutoff, transition, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.band_pass_filter_3 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, quadrature, 18.5e3, 19.5e3, 1000, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_2 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, quadrature, 54e3, 60e3, 3e3, firdes.WIN_HAMMING, 6.76))
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
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.wxgui_waterfallsink2_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.band_pass_filter_2, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.band_pass_filter_3, 0))
        self.connect((self.band_pass_filter_2, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.band_pass_filter_3, 0), (self.blocks_multiply_xx_1, 3))
        self.connect((self.band_pass_filter_3, 0), (self.blocks_multiply_xx_1, 2))
        self.connect((self.band_pass_filter_3, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.band_pass_filter_2, 0), (self.wxgui_scopesink2_3, 0))
        self.connect((self.low_pass_filter_2, 0), (self.wxgui_scopesink2_2, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.wxgui_scopesink2_1, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_2, 0))



    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)

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
        self.wxgui_scopesink2_3.set_sample_rate(self.samp_rate)

    def get_quadrature(self):
        return self.quadrature

    def set_quadrature(self, quadrature):
        self.quadrature = quadrature
        self.band_pass_filter_2.set_taps(firdes.band_pass(1, self.quadrature, 54e3, 60e3, 3e3, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_3.set_taps(firdes.band_pass(1, self.quadrature, 18.5e3, 19.5e3, 1000, firdes.WIN_HAMMING, 6.76))
        self.wxgui_scopesink2_1.set_sample_rate(self.quadrature)
        self.low_pass_filter_2.set_taps(firdes.low_pass(1.1875*self.echantillon, self.quadrature, 2.2e3, 2e3, firdes.WIN_HAMMING, 6.76))

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self._frequency_slider.set_value(self.frequency)
        self._frequency_text_box.set_value(self.frequency)
        self.rtlsdr_source_0.set_center_freq(self.frequency*1e6, 0)

    def get_echantillon(self):
        return self.echantillon

    def set_echantillon(self, echantillon):
        self.echantillon = echantillon
        self.low_pass_filter_2.set_taps(firdes.low_pass(1.1875*self.echantillon, self.quadrature, 2.2e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.wxgui_scopesink2_2.set_sample_rate(self.echantillon*1187.5)
        self._echantillon_slider.set_value(self.echantillon)
        self._echantillon_text_box.set_value(self.echantillon)

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
    tb = ExtractionRDS()
    tb.Start(True)
    tb.Wait()
