#!/bin/bash

# declare and print STRING variable
STRING="Harmonic Layer Filler"
echo $STRING

pd-extended -noaudio open "./hhf-pd.pd" &
python hhf-gui.py
killall python
killall pd-extended
killall pd
exit
