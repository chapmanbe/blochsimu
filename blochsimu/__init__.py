
#Copyright (c) 2014-2015, Koos C. J. Zevenhoven <koos.zevenhoven@aalto.fi>
#
#Permission to use, copy, modify, and/or distribute this software for any
#purpose with or without fee is hereby granted, provided that the above
#copyright notice and this permission notice appear in all copies.
#
#THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
#WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
#MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
#ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
#WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
#ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
#OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""
Created on Wed Nov 19 19:18:07 2014

Module for simulating the expectation of a spin-1/2 ensemble using the Bloch
equation (currently non-dissipative),

dM/dt = gamma M x B.

For documentation (for now), see the docstrings of Simulator, its constructor 
and its simulate(...) method.

@author: Koos Zevenhoven
"""
from .bloch import Simulator
