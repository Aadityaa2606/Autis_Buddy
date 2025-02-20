"""
Autis Buddy
===========

A tool for converting EEG data to music for therapeutic purposes.

Main components:
- EEG Processing
- Music Parameter Mapping
- MIDI Generation
- Data Visualization
"""

__version__ = "0.1.0"
__author__ = "Aaditya"
__description__ = "EEG to Music conversion tool for therapeutic purposes"

# Import key components for easy access
from autis_buddy.core.eeg_processor import preprocess_eeg
from autis_buddy.core.music_mapper import eeg_to_music_parameters
from autis_buddy.core.midi_generator import json_to_midi
from autis_buddy.visualization.plots import create_all_visualizations
from autis_buddy.utils.config import config

# Define what should be available when using "from autis_buddy import *"
__all__ = [
    'preprocess_eeg',
    'eeg_to_music_parameters',
    'json_to_midi',
    'create_all_visualizations',
    'config',
]
