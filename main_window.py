#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Main Window
# Generated: Thu Mar  5 14:16:12 2015
##################################################

from gnuradio import eng_notation
from gnuradio import fcd
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class main_window(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Main Window")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.GridAdd(self.wxgui_scopesink2_0.win, 1, 2, 1, 1)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.GridAdd(self.wxgui_fftsink2_0.win, 1, 1, 1, 1)
		self.fcd_source_c_0 = fcd.source_c("bus/usb/002/009")
		self.fcd_source_c_0.set_freq_corr(-120)
		self.fcd_source_c_0.set_freq(89600000)
		    

		##################################################
		# Connections
		##################################################
		self.connect((self.fcd_source_c_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.fcd_source_c_0, 0), (self.wxgui_scopesink2_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = main_window()
	tb.Run(True)

