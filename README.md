# python-musical

Python module for procedural music creation.

* Added sounddevice playback to `example_01.py` - which has the added benefit of being able to key-board interrupt playing (nice for debugging)
* pygame actually uses sounddevice under the hood (I think), so its best to just use this library straight-away
* This means that all audio creation will depend on wave-form synthesis explicitly.
* TODO: need to replace `play` with `play_sd` in `musical.audio`, which will require making sure the waveform is normalized so it doesn't sound like garbage.
    * Useful cookbook of soundfile examples: https://python-sounddevice.readthedocs.io/en/0.4.2/examples.html#play-a-sound-file