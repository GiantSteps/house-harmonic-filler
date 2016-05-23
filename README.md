
##House-Harmonic-Filler

The *House Harmonic Filler* is a temptative model for chord variation that could be used in contexts of live electronic music performance. Based on corpus analysis of MIDI files, it provides a framework for variation and extension of chord progressions, generating MIDI data that is sent out to the preferred MIDI device or DAW.

!["The graphic interface"](/doc/img-hhf.png?raw=true)

####Installation

To run the **House-Harmonic-Filler** you need the latests stable Pd-vanilla distribution (0.46.7). You can download it from Miller Puckette's website (http://msp.ucsd.edu/software.html), of from the Pd main site (http://puredata.info). Beware that Pd-extended is now obsolete. For ease of use, we have included with this download all the externals needed, so downloading this repository is all you need to do to start using the program, once you have Pd installed.

####Description

House harmonic loops normally consist of sequences of 2 or 4 bars, with a tendency to have a single chord per bar. 8-bar loops are less frequent, and in most cases, they result from a repetition of a 4-bar pattern with some small variation toward the end of the second half. Currently, the House Harmonic Filler operates with 4-bar loops. For the current study, we have used limited resources publicly available on the internet. We have selected homophonic MIDI chord loops under tags of deep house piano, classic house piano and deep house chords. However, you could analyize your own corpus of MIDI files with the analysis patch provided.


#####Harmony
It takes a single MIDI chord loop, which serves as the reference musical material on which variations are performed in real-time. As already discussed, loops are limited to two bars in length, although this will be expanded to lengthier excerpts in the near future. The loop is analyzed in terms of rhythm, duration, chord progression and scale, in order to extract different layers of information and manipulation.
!["The graphic interface"](/doc/img-harmony.png?raw=true)


#####Keyboard

Rhythmic Variation: Style Agnostic Density Transformer
As explained above, harmony is a complex musical category that can not be considered in isolation from other musical parameters. In relation to rhythm, harmony progresses in time displaying a certain harmonic rhythm, which is the pace at which chord-changes structure time. This tends to be regular, especially in the styles we are studying, with chords changing at every bar. However the harmonic loops we are presenting have a clear motivic identity (call this hook, vamp or riff, the underlying concept is that of a harmonic-rhythmic-melodic compound recognizable as a unit and characteristic of a piece of music).
This surface rhythmic layer is processed according to the Agnostic Density Transformer described in D4.1, section 2.1:
“It is based on the fact that syncopated onsets, as challenges to regularity, are the most definitive elements of a rhythmic pattern, as opposed to onsets that reinforce the beat’s regularity, which we consider to be least important on the definition of a rhythmic pattern.” (excerpted from D4.1, section 2.1)
This strategy for rhythmic variation maintains the original's rhythmic feel, while adding or subtracting elements in real-time. Therefore, the user can make the pattern more dense or sparse, while always being able to return to the original rhythmic pattern. We have expanded the rhythmic hierarchy from a single bar to operate on larger time units (sequences of 2, 4 or 8 bars).
Duration
The Density Agnostic Transformer only takes information (and possibility of variation) about the onsets (i.e. the position of the attacks). Whether this might be sufficient to model percussive instruments, where the location of a hit might be enough to replicate a pattern, manipulation of sounds that can be prolongated on time (as most pitched-instruments do, to different extents and by different techniques), need to take care of the duration of the sounds. In the current prototype, we have treated duration as a separate layer of the onset positions (density). We have analysed the duration of each note according to its position on the metrical grid, and assigned zeroth order probabilities to each step position. The overall duration of the pattern can be adjusted by a so-called legato control, which is the result of combining the onsets layer (density) with the zeroth order probability of the durations per step, resulting in a continuum going from legato (all notes ending at the moment of a new attack) to an imperfect stacatto (all notes having the duration of the minimum step size, a 16th note in the current implementation).
Harmonic Variation
We have opted for a theoretical model (rather than a Markov model) as a means to introduce harmonic variation for the following reasons: On the one hand, (1) the House Harmonic Filler takes one chord progression as a reference pattern, over which it performs variations, from similar to extremely dissimilar. The corpus we have used (40 loops) is far too small to provide us with a meaningful range of variations, which we have supplied by theoretical derivation. On the other hand, (2) two-step progressions are too short to allow for non-redundant Markovian processes, since a two-element 1st order Markov chain would already represent the whole harmonic sequence. (3) Furthermore, a step/bar-based probability (zeroth order Markov sequence) proves meaningless, since there is not a clear sense of a tonic, nor that of beginning or end, given the circularity of the loop.
Therefore, the chord structure proper can be modified following two different and complementary strategies:
By changing the so-called color or tension of each chord, that is, by modifying the number of notes in the chord while keeping the same function and root. This is a technique characteristic of jazz-derived styles, present in deep house music, by which one can pile up thirds (to make chords of 7th, 9th, 11th and 13th) or added notes (6th, 9th, 4th). The chord saturation control, offers a range of variation from the so-called power-chord at one extreme (the highest reduction of a chord, by which even the major/minor typology is omitted) to chromatic additions on the other end (adding notes that do not belong to the current scale). However, most of the interactive range of the color control, deals with addition of tensions according to the detected scale or possible derivatives, when a defective pitch-class set is present (i.e. groups of notes consisting of six or less notes).
The other approach is borrowed from both classic and modern music theory, and is based on the assumption that certain chords can temporarily substitute other chords, maintaining the original tonal function. There is extensive literature on rules of chord substitution; we refer the reader to two works already mentioned in this report for brief and extensive surveys on this issue (Moore, 1992; Piston, 1941). 
The substitution distance control proceeds from very tonal substitutions at one extreme to chromatic substitution on the other, although this might not be idiomatic of the styles in consideration.
Register Expansion
A register expansion control allows variations in the vertical layout of the chord, from closed position (all notes of the chord contained within the same octave) to higher and lower expansion to up to 4 octaves. Additionally, we provide a binary checkbox to allow chord inversions, which will let the lowest note of the chord aggregate be different from the lowest note in the original. We remind the reader that the intended use of the House Harmonic Filler is that of filling the mid-register harmonic layer, and that it normally should be used in conjunction with an existing or generated bass line. Being this the case, the actual lowest note of the chord might not necessarily be that of the chord generated with the current tool.
Overall Activity Control
Last, we offer an Overall Activity control which simultaneously influences the amount of variation of the tonal parameters just described, resulting in a sort of voice leading control according to the color, substitution and register parameters, from a single change per chord on one extreme, to changes in the vertical configuration of the chord at every new onset.
Again, the activity control follows a model based on the theory behind the agnostic density transformer (Lerdahl and Jakendoff, 1983) by which less rhythmically-significant steps are modified first.
 
A second window (Figure 23) provides visualization information about the live transformations on the MIDI Loop. This window presents a two-bar length grid quantized at 16th notes, with a three-layer box system on top. The layer at the background represents a metronome progressing along the sequence beats in sync with the tempo set by the user. The middle-ground layer represents the original pattern: each box represents a chord event, labeled with its chord name, where start- and end-points, as well as duration are represented by the rectangles position and horizontal length. Similarly, the forefront layer displays the modifications on real-time requested by the user. In the screenshot shown in Figure 23, density is set to 8 and legato to 0 (all 16th notes).



!["The graphic interface"](/doc/img-bass.png?raw=true)


!["The graphic interface"](/doc/img-chords.png?raw=true)


!["The graphic interface"](/doc/img-loop.png?raw=true)


!["The graphic interface"](/doc/img-transport.png?raw=true)


!["The graphic interface"](/doc/img-memory.png?raw=true)


*(Tested on on Ubuntu 15.10 and OSX El Capitan)*
