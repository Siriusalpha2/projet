/* -*- c++ -*- */

#define TUTO_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "tuto_swig_doc.i"

%{
#include "tuto/my_qpsk_demod_cb.h"
%}


%include "tuto/my_qpsk_demod_cb.h"
GR_SWIG_BLOCK_MAGIC2(tuto, my_qpsk_demod_cb);
