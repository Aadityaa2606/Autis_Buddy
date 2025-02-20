"""
Core Package
===========

Contains the main processing components for EEG analysis and music generation.

Components:
- EEG Processing
- Music Parameter Mapping
- MIDI Generation
"""

from core.eeg_processor import preprocess_eeg
from core.music_mapper import eeg_to_music_parameters
from core.midi_generator import json_to_midi

__all__ = [
    'preprocess_eeg',
    'eeg_to_music_parameters',
    'json_to_midi',
]

# Version of the core processing modules
__core_version__ = "0.1.0"

# Define the supported EEG file formats
SUPPORTED_FORMATS = ['.set', '.edf', '.bdf']

# Define the supported output formats
SUPPORTED_OUTPUTS = ['midi', 'json']
