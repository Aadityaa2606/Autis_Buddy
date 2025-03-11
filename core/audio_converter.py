def convert_midi_to_mp3(midi_path: str, mp3_path: str) -> None:
    """
    Convert MIDI file to MP3 using FluidSynth.
    
    Args:
        midi_path (str): Path to the input MIDI file
        mp3_path (str): Path where the output MP3 file will be saved
    
    Raises:
        FileNotFoundError: If the input MIDI file doesn't exist
        Exception: If FluidSynth fails to convert the file
    """
    import os
    from midi2audio import FluidSynth
    
    # Check if input file exists
    if not os.path.exists(midi_path):
        raise FileNotFoundError(f"MIDI file not found: {midi_path}")
    
    try:
        # Create FluidSynth instance
        fs = FluidSynth("/usr/share/sounds/sf2/FluidR3_GM.sf2")
        
        # Convert MIDI to MP3
        fs.midi_to_audio(midi_path, mp3_path)
        
        # Verify output file was created
        if not os.path.exists(mp3_path):
            raise Exception("Conversion completed but output file wasn't created")
    
    except Exception as e:
        raise Exception(f"MIDI to MP3 conversion failed: {str(e)}")
