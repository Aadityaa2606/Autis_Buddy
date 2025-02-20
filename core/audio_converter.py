def convert_midi_to_mp3(midi_path: str, mp3_path: str) -> None:
    """
    Convert MIDI file to MP3 using FluidSynth.
    
    Args:
        midi_path (str): Path to the input MIDI file
        mp3_path (str): Path where the output MP3 file will be saved
    """
    from midi2audio import FluidSynth
    
    # Create FluidSynth instance
    fs = FluidSynth("/usr/share/sounds/sf2/FluidR3_GM.sf2")
    
    # Convert MIDI to MP3
    fs.midi_to_audio(midi_path, mp3_path)