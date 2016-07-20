# Copyright (C) 2015 ETH Zurich, Institute for Astronomy

'''
Created on Mar 26, 2015

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals

import numpy as np
from ivy.utils.struct import Struct
from hide.plugins import add_rfi

class TestAddRFIPlugin(object):
    
    def test_add_rfi(self):
        
        tod = np.zeros((300, 3600))
        
        params = Struct(strategy_step_size=1,
                        #bursts
                        max_rfi_count = 20,
                        coeff_freq = [0.179, 1.191],
                        coeff_time = [0.144, -1.754, 63.035],
                        sigma_range = 3.0,
                        amp_scale = 3,
                        amp_loc = 0,
                        #constant
                        rfi_freqs = [25, 120],
                        min_amp = 1.,
                        max_amp = 5.,
                        rfi_width = 8,
                        )
        
        ctx = Struct(params = params,
                     tod_vx = tod,
                     tod_vy = tod.copy())
        
        plugin = add_rfi.Plugin(ctx)
        plugin()
        
        assert np.sum(ctx.tod_vx - ctx.tod_vy) != 0