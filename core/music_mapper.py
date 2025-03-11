import json
import numpy as np
import os
from pathlib import Path

def eeg_to_music_parameters(input_file):
    """
    Convert EEG wave strengths to musical parameters.

    Parameters:
    input_file (str): Path to input JSON file containing EEG data
    
    Returns:
    dict: The generated music parameters
    
    Raises:
    FileNotFoundError: If the input file doesn't exist
    """
    # Check if input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    # Read the input JSON file
    with open(input_file, 'r') as f:
        eeg_data = json.load(f)

    # Initialize output dictionary
    music_data = {
        "interval_length": eeg_data["interval_length"],
        "musical_parameters": {}
    }

    # Process each interval
    for interval, wave_strengths in eeg_data["wave_strengths"].items():
        # Convert string percentages to float
        delta = float(wave_strengths[0])
        theta = float(wave_strengths[1])
        alpha = float(wave_strengths[2])
        beta = float(wave_strengths[3])
        gamma = float(wave_strengths[4])

        # Calculate musical parameters

        # Pitch (MIDI number)
        pitch = 60 + (delta * -10) + (gamma * 10) 
        pitch = round(np.clip(pitch, 0, 127))

        # Step (intervals)
        step = 2 + (beta * 5)
        step = round(step, 1)

        # Duration
        duration = 0.5 + (delta * 0.1) - (beta * 0.3)
        duration = round(max(0.1, duration), 2) 

        # Store the results
        music_data["musical_parameters"][interval] = [
            str(pitch),
            str(step),
            str(duration)
        ]

    # Create output directory if it doesn't exist
    output_dir = Path('output/json')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create output filename based on input filename
    output_file = 'output/json/music_parameters.json'

    # Save to output JSON file
    with open(output_file, 'w') as f:
        json.dump(music_data, f, indent=2)

    print(f"Conversion complete. Music parameters saved to: {output_file}")
    return music_data
