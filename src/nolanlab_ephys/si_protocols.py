protocols = {

    'kilosort4A': {
        'preprocessing': {},
        'sorting': {
            'sorter_name': 'kilosort4',
            'do_correction': False,
            'use_binary': False,
        },
        'preprocessing_for_analyzer': {
            'common_reference': {},
            'bandpass_filter': {},
        },
    },

    'mountainsort5A': {
        'preprocessing': {
            'bandpass_filter': {},
            'whiten': {},
        },
        'sorting': {
            'sorter_name': 'mountainsort5',
            'do_correction': False,
            'use_binary': False,
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
    }


}


generic_postprocessing = {
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