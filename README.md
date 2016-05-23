
##House-Harmonic-Filler

The *House Harmonic Filler* is a temptative model for chord variation that could be used in contexts of live electronic music performance. Based on corpus analysis of MIDI files, it provides a framework for variation and extension of chord progressions, generating MIDI data that is sent out to your preferred device or DAW.

<p align="center">
  <img src="/doc/img-hhf.png"/>
</p>

####Installation

To run the **House-Harmonic-Filler** you need the latests stable Pd-vanilla distribution (0.46.7). You can download it from Miller Puckette's website (http://msp.ucsd.edu/software.html), of from the Pd main site (http://puredata.info). Beware that Pd-extended is now obsolete. For ease of use, we have included with this download all the externals needed, so downloading this repository is all you need to do to start using the program, once you have Pd installed.

####Description

The program offers simple manipulation of MIDI loops. You can use it in standalone mode (in which case, the program uses an internal synthesiser to produce sounds) and more interestingly, as a *slave* MIDI instrument sending data to your preferred device or Digital Audio Workstation. 

It also has *MIDI learn* fuctions, in case you want to control its parameter with a hardware controller or an external interface. The midi learn function is represented by the **red dots** next to each parameter. To assign a MIDI CC to a parameter, simply move the controller you want to assign and then hit on the red dot. The last-used CC should be automatically assigned and remembered for future sessions.

#####Harmony

The *HARMONY* section is the core of the application. We have previously analysed a collection of MIDI loops in terms of harmonic rhythm and chord progressions. In the current version, we have used limited resources publicly available on the internet. We have selected homophonic MIDI chord loops under tags of deep house piano, classic house piano and deep house chords. You could alternatively analyise your own folder with MIDI files using the patch named *analysis-corpus.pd* also provided with this repository, although this feature is still experimental.   

House harmonic loops normally consist of sequences of 2 or 4 bars, with a tendency to have a single chord per bar. 8-bar loops are less frequent, and in most cases, they result from a repetition of a 4-bar pattern with some small variation toward the end of the second half, so we have limited the performance of the *House Harmonic Filler* to 4-bar loops.

<p align="center">
  <img src="/doc/img-harmony.png"/>
</p>

Each dot in the two-dimensional plot represents one of such 4-bar MIDI loop in the analysed corpus, which serves as the reference musical material on which variations are performed in real-time. They are organized following a double classification of diatonic-chromatic (measured as the number of semitones present on each file) and minor-major (calculated as the distance with theoretical scales and modes). You could select a different progression by clicking on each dot, or alternatively by clicking on the *next* and *previous* buttons above. The loops are analyised relatively, so you could transpose each midi loop to any of the twelve pitch classes with the *key* wheel.

#####Keyboard

Selected loops are represented on a simple 4-bar display in the top of the program. What you see is a two-layer representation, with the master pattern (light-gray) and the slave pattern with the variations on top of it (dark-gray). You will see here the variations you perform in the *RHYTHM* and *KEYBOARD* sections. Harmony progresses in time displaying a certain harmonic rhythm, which is the pace at which chord-changes structure time. This tends to be regular, especially in the styles we are studying, with chords changing at every bar.

<p align="center">
  <img src="/doc/img-loop.png"/>
</p>

Since the analyisis on pitch and rhythm are carried independently, you can use any master rhythmic pattern with any chord progression. To change the master pattern you can use the *pattern* control.

To perform chord variations over the rhythmic master pattern you can use the controls under the *KEYBOARD* section:

- The *density* control changes the number of events in the chord loop. A **light-red mark** indicates the position with the original density, so you can retrieve the original master pattern by aligning the parameter to this position.
- The *legato* sets the relative duration of the events. Setting it to its maximum will make the chords last until the next attack.
- The *octave* parameter transposes the chord progressions up or down.
- Moving the *spread* you will open the position of the chords (leaving more space between the same notes of the chord).
- while the *register* control affects the inversion of the chords, slighlty folding them up or down.
- *mute* and *volume* controls mute and set the volume of the keyboard layer.

<p align="center">
  <img src="/doc/img-chords.png"/>
</p>

#####Bass

<p align="center">
  <img src="/doc/img-bass.png"/>
</p>


#####Transport and Storage
The *TRANSPORT* section offers basic transport options. Besides *playing* and setting the *tempo* of the loop, this is the section where you set the main behaviour of the program:

- *int-synth* enables a small synthesiser for testing without needing an external midi synthesiser.
- *ext-sync* sets the program to operate as a slave of an external midi devide. When activated, the playback and tempo options are disabled, and the program expect midi transport information on a midi in port. This is useful to integrate this program within any DAW.

<p align="center">
  <img src="/doc/img-transport.png"/>
</p>

Last, a *MEMORY* section lets you store and recall up to 7 presets. Transport instructions (tempo, play) are not stored with the memories.

<p align="center">
  <img src="/doc/img-memory.png"/>
</p>


*(Tested on on Ubuntu 15.10 and OSX El Capitan)*
