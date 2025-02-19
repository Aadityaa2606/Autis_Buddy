from eeg_preprocessing import preprocess_eeg
from analysis.visualise_preprocessing import plot_wave_strengths
from eeg_music_mapper import eeg_to_music_parameters
from json_to_midi import json_to_midi

# Assuming the function preprocess_eeg takes a file path as an argument
file_path = '/home/aadityaa/Documents/Programming/capstone_project/Autis_Buddy/test_eeg.set'
results = preprocess_eeg(file_path)

plot_wave_strengths(results)

preprocessed_eeg_path = '/home/aadityaa/Documents/Programming/capstone_project/Autis_Buddy/test_eeg_wave_analysis.json'

eeg_to_music_parameters(preprocessed_eeg_path)

eeg_music_params_path = '/home/aadityaa/Documents/Programming/capstone_project/Autis_Buddy/music_parameters.json'

json_to_midi(eeg_music_params_path)