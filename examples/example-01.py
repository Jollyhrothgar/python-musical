from musical.theory import Note
from musical.theory import Scale
from musical.theory import Chord
from musical.audio.playback import play
from musical.audio.playback import play_sd
from musical.audio.timeline import Hit
from musical.audio.timeline import Timeline
import sounddevice as sd

# Define key and scale
key = Note('G3')
scale = Scale(key, 'major')

# Grab progression chords from scale starting at the octave of our key
progression = Chord.progression(scale, base_octave=key.octave)

time_counter = 0.0 # Keep track of currect note placement time in seconds

timeline = Timeline()

# Add progression to timeline by arpeggiating chords from the progression
for index in [0, 2, 3, 1,    0, 2, 3, 4,    5, 4, 0]:
    chord = progression[index]
    root, third, fifth = chord.notes
    arpeggio = [root, third, fifth, third, root, third, fifth, third]
    for i, interval in enumerate(arpeggio):
        ts = float(i * 2) / len(arpeggio)
        timeline.add(time_counter + ts, Hit(interval, 1.0))
    time_counter += 2.0

# Strum out root chord to finish
chord = progression[0]
timeline.add(time_counter + 0.0, Hit(chord.notes[0], 4.0))
timeline.add(time_counter + 0.1, Hit(chord.notes[1], 4.0))
timeline.add(time_counter + 0.2, Hit(chord.notes[2], 4.0))
timeline.add(time_counter + 0.3, Hit(chord.notes[1].transpose(12), 4.0))
timeline.add(time_counter + 0.4, Hit(chord.notes[2].transpose(12), 4.0))
timeline.add(time_counter + 0.5, Hit(chord.notes[0].transpose(12), 4.0))

print("Rendering audio...")

data = timeline.render()

# Reduce volume to 50%
data = data * 0.5


print("Playing audio...")
play_sd(data, 44100)
# play(data)

print("Done!")
