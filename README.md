
##House-Harmonic-Filler

The *House Harmonic Filler* is a temptative model for chord variation that could be used in contexts of live electronic music performance. Based on corpus analysis of MIDI files, it provides a framework for variation and extension of chord progressions, generating MIDI data that is sent out to the preferred MIDI device or DAW.

!["The graphic interface"](/doc/img-hhf.png?raw=true)

####Installation

To run the **House-Harmonic-Filler** you need the latests stable Pd-vanilla distribution (0.46.7). You can download it from Miller Puckette's website (http://msp.ucsd.edu/software.html), of from the Pd main site (http://puredata.info). Beware that Pd-extended is now obsolete. For ease of use, we have included with this download all the externals needed, so downloading this repository is all you need to do to start using the program, once you have Pd installed.

####Description
#####Harmony

House harmonic loops normally consist of sequences of 2 or 4 bars, with a tendency to have a single chord per bar. 8-bar loops are less frequent, and in most cases, they result from a repetition of a 4-bar pattern with some small variation toward the end of the second half. Currently, the House Harmonic Filler operates with 4-bar loops.


For the current study, we have used limited resources publicly available on the internet. We have selected homophonic MIDI chord loops under tags of deep house piano, classic house piano and deep house chords. However, you could analyize your own corpus of MIDI files with the analysis patch provided.



It takes a single MIDI chord loop, which serves as the reference musical material on which variations are performed in real-time. As already discussed, loops are limited to two bars in length, although this will be expanded to lengthier excerpts in the near future. The loop is analyzed in terms of rhythm, duration, chord progression and scale, in order to extract different layers of information and manipulation.

<p align="center">
  <img src="/doc/img-harmony.png"/>
</p>

#####Keyboard

As explained above, harmony is a complex musical category that can not be considered in isolation from other musical parameters. In relation to rhythm, harmony progresses in time displaying a certain harmonic rhythm, which is the pace at which chord-changes structure time. This tends to be regular, especially in the styles we are studying, with chords changing at every bar. However the harmonic loops we are presenting have a clear motivic identity (call this hook, vamp or riff, the underlying concept is that of a harmonic-rhythmic-melodic compound recognizable as a unit and characteristic of a piece of music).


<p align="center">
  <img src="/doc/img-bass.png"/>
</p>


!["The graphic interface"](/doc/img-bass.png?raw=true)


!["The graphic interface"](/doc/img-chords.png?raw=true)


!["The graphic interface"](/doc/img-loop.png?raw=true)


#####Transport and Storage
The *Transport* section offers basic transport options. Besides playing and setting the tempo of the loop, this is the section where you set the behaviour of the program:

- *int-synth* enables a small synthesiser for testing without needing an external midi synthesiser.
- *ext-sync* sets the program to operate as a slave of an external midi devide. When activated, the playback and tempo options are disabled, and the program expect midi transport information on a midi in port. This is useful to integrate this program within any DAW.

<p align="center">
  <img src="/doc/img-transport.png"/>
</p>

Last, a *Memory* section lets you store in memory and recall up to 7 presets. Transport instructions (tempo, play) are not stored with the memories.

<p align="center">
  <img src="/doc/img-memory.png"/>
</p>


*(Tested on on Ubuntu 15.10 and OSX El Capitan)*
