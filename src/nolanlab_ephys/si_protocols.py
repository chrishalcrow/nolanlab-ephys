protocols = {

    'kilosort4A': {
        'preprocessing': {},
        'sorting': {
            'sorter_name': 'kilosort4',
            'do_correction': False,
            'use_binary_file': False,
        },
        'preprocessing_for_analyzer': {
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
    'spike_amplitudes': {},
    'spike_locations': {},
    'correlograms': {},
    'quality_metrics': {},
    'template_metrics': {'include_multi_channel_metrics': True},
}