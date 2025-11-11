protocols = {

    'kilosort4A': {
        'preprocessing': {
            'detect_and_remove_bad_channels': {'seed': 1205},
            'phase_shift': {},
        },
        'sorting': {
            'sorter_name': 'kilosort4',
            'do_correction': False,
            'use_binary_file': False,
        },
        'preprocessing_for_analyzer': {
            'detect_and_remove_bad_channels': {'seed': 1205},
            'phase_shift': {},
            'common_reference': {},
            'bandpass_filter': {},
        },
    },

    'mountainsort5A': {
        'preprocessing': {
            # 'bandpass_filter': {},
            # 'whiten': {'dtype': 'float'},
        },
        'sorting': {
            'sorter_name': 'mountainsort5',
            'scheme': '2',
        },
        'preprocessing_for_analyzer': {
            'common_reference': {},
            'bandpass_filter': {},
        },
    },

    'mountainsort5B': {
        'preprocessing': {
            # 'bandpass_filter': {},
            # 'whiten': {'dtype': 'float'},
        },
        'sorting': {
            'sorter_name': 'mountainsort5',
            'scheme': '3',
        },
        'preprocessing_for_analyzer': {
            'common_reference': {},
            'bandpass_filter': {},
        },
    },

    'mountainsort4A': {
        'preprocessing': {
        },
        'sorting': {
            'sorter_name': 'mountainsort4',
        },
        'preprocessing_for_analyzer': {
            'common_reference': {},
            'bandpass_filter': {},
        },
    },

    'herdingspikesA': {
        'preprocessing': {
            'bandpass_filter': {},
            'common_reference': {},
     #       'whiten': {'dtype': 'float'},
        },
        'sorting': {
            'sorter_name': 'herdingspikes',
        },
        'preprocessing_for_analyzer': {
            'bandpass_filter': {},
            'common_reference': {},
        },
    },

    'spykingcircus2A': {
        'preprocessing': {
        },
        'sorting': {
            'sorter_name': 'spykingcircus2',
            'apply_motion_correction': False,
        },
        'preprocessing_for_analyzer': {
            'bandpass_filter': {},
            'common_reference': {},
        },
    },

    'tridesclous2A': {
        'preprocessing': {
        },
        'sorting': {
            'sorter_name': 'tridesclous2',
        },
        'preprocessing_for_analyzer': {
            'bandpass_filter': {},
            'common_reference': {},
        },
    },


}

generic_postprocessing = {
    'unit_locations': {},
    'random_spikes': {},
    'noise_levels': {},
    'waveforms': {},
    'templates': {},
    'spike_amplitudes': {'peak_sign': 'both'},
    'isi_histograms': {},
    'spike_locations': {'spike_retriver_kwargs': {'peak_sign': 'both'}},
    'correlograms': {},
    'template_similarity': {'method': 'l2'},
    'quality_metrics': {'metric_names': ['num_spikes', 'firing_rate', 'presence_ratio', 'snr', 'isi_violation', 'rp_violation', 'sliding_rp_violation', 'amplitude_cutoff', 'amplitude_median', 'amplitude_cv', 'synchrony', 'firing_range', 'drift', 'sd_ratio'], 'metric_params': {'snr': {'peak_sign': 'both'}, 'amplitude_cutoff': {'peak_sign': 'both'}, 'amplitude_median': {'peak_sign': 'both'}}},
    'template_metrics': {'include_multi_channel_metrics': True, 'peak_sign': 'both'},
}