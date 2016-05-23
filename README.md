
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
!["The graphic interface"](/doc/img-harmony.png?raw=true)


#####Keyboard

As explained above, harmony is a complex musical category that can not be considered in isolation from other musical parameters. In relation to rhythm, harmony progresses in time displaying a certain harmonic rhythm, which is the pace at which chord-changes structure time. This tends to be regular, especially in the styles we are studying, with chords changing at every bar. However the harmonic loops we are presenting have a clear motivic identity (call this hook, vamp or riff, the underlying concept is that of a harmonic-rhythmic-melodic compound recognizable as a unit and characteristic of a piece of music).



!["The graphic interface"](/doc/img-bass.png?raw=true)


!["The graphic interface"](/doc/img-chords.png?raw=true)


!["The graphic interface"](/doc/img-loop.png?raw=true)


#####Transport and Storage
We have pl

<center>!["The graphic interface"](/doc/img-transport.png?raw=true)


!["The graphic interface"](/doc/img-memory.png?raw=true)


*(Tested on on Ubuntu 15.10 and OSX El Capitan)*
