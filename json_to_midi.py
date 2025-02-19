import json
from mido import Message, MidiFile, MidiTrack

def json_to_midi(json_file: str):
    with open(json_file, 'r') as f:
        data = json.load(f)

    interval_length = int(data['interval_length'])
    musical_parameters = data['musical_parameters']

    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    for key, params in musical_parameters.items():
        note = int(params[0])
        duration = float(params[1])
        velocity = int(float(params[2]) * 127)  # Convert to MIDI velocity (0-127)

        track.append(Message('note_on', note=note, velocity=velocity, time=0))
        track.append(Message('note_off', note=note, velocity=velocity, time=int(duration * 480)))  # 480 ticks per beat
    
    output_file = 'midi_out.mid'

    midi.save(output_file)