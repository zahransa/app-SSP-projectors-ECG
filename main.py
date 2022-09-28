
# Copyright (c) 2021 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#


# set up environment
import os
import json
import mne
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image


# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load brainlife config.json
with open('config.json','r') as config_f:
    config = json.load(config_f)

# == LOAD DATA ==
fname = config['fif']
raw = mne.io.read_raw_fif(fname, verbose=False)


# ecg_projs, ecg_events = mne.preprocessing.compute_proj_ecg(raw, n_grad=1, n_mag=1, n_eeg=0,
#                                                          average=True)
ecg_projs, ecg_events = mne.preprocessing.compute_proj_ecg(raw, None, config['tmin'], config['tmax'], config['n_grad'],
            config['n_mag'], config['n_eeg'], config['l_freq'], config['h_freq'], config['average'], config['filter_length'], -1, None, None, None, [],
            config['avg_ref'], config['no_proj'], config['event_id'], config['ecg_l_freq'], config['ecg_h_freq'], config['tstart'],
            config['qrs_threshold'], config['filter_method'], None, config['copy'], config['return_drop_log'], config['meg'])


# ecg_projs, ecg_events = mne.preprocessing.compute_proj_ecg(raw, config['tmin'], config['tmax'], config['n_grad'],
#                         config['n_mag'], config['n_eeg'], config['l_freq'], config['h_freq'], config['average'], config['filter_length'], config['ch_name'],
#                        config['avg_ref'], config['no_proj'], config['event_id'], config['ecg_l_freq'], config['ecg_h_freq'], config['tstart'],
#                        config['qrs_threshold'], config['filter_method'], config['iir_params'], config['copy'], config['return_drop_log'], config['meg'])



mne.write_proj('out_dir/heartbeat-proj.fif', ecg_projs)
