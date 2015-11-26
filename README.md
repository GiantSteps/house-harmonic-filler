# house-harmonic-filler

### Dependencies.
The current prototype is implemented in the Pd-Extended/Gem environment, and is delivered with a collection of original MIDI loops. 

**It depends on the "pd-symbolic" set of abstractions, which you can download from http://github.com/angelfaraldo/pd-symbolic.**

### Blah blah
The house-harmonic-filler is a temptative model for chord variation that could be used in contexts of live electronic music performance. Despite harmony not being a prominent aspect of many electronic popular music genres, it is still prevalent in those evolving directly from the song tradition, such as electro-pop and disco variants. Furthermore, certain sub-styles of house, especially so-called deep house, make use of chord loops borrowed from what we could call a black-american tradition, such as soul, rhythm-and-blues or even jazz, using extended chords other than simple triads (especially major and minor 7ths and 9ths, but also 13ths, suspensions and alterations). Deep house tracks often favour instrumental timbres (as opposed to synthesized ones), such as pianos, vibraphones as well as an extensive use of vocals.

I refer to the current protopype as the *House Harmonic Filler* inspired by the nomenclature by Moore (2012, pp. 20 ff.). According to Moore, popular music styles can be differentiated and characterized by observing four basic textural functional layers, namely the explicit beat layer, the functional bass layer, the melodic layer and the harmonic filler layer.

##### Chord Shuttles
House harmonic loops normally consist of sequences of 2 or 4 bars, with a tendency to have a single chord per bar. 8-bar loops are less frequent, and in most cases, they result from a repetition of a 4-bar pattern with some small variation toward the end of the second half.

Currently, the House Harmonic Filler is limited to operating with 2-bar loops or shuttles. According to Tagg (2014), a chord shuttle consists in an ongoing oscillation between two chords, normally of equal duration and importance. This particular behaviour is present in many of the chord loops analysed, each one lasting for a bar, and normally avoiding quintal jumps between their roots. Intervals of second, fourth and third (from most to less frequent) seem to be the most common jumps, favouring subdominant relations between the chords. These tonal relations tend to be ambivalent, and most of the times it is not possible to determine which chord has a tonic feel, effect which is potentiated by the endless looping mechanism. This is the reason why I have tried to avoid the tonal-functional connotations implied by classic tonal harmony (cfr. Piston, 1941), and where possible, I have interpreted the sequences as ambiguously as possible, considering both chords of the shuttle as potential tonics (I). Chord shuttles have a strong presence in other popular music styles (especially blues and its derivatives).

I will reserve the term chord loop for cyclical sequences of more than two chords, normally four (Tagg, 2014), which are excluded from this study, and will be considered in due time.

#####Usage
The application takes a single MIDI chord loop, which serves as the reference musical material on which variations are performed in real-time. As already discussed, loops are limited to two bars in length, although this will be expanded to lengthier excerpts in the near future. The loop is analyzed in terms of rhythm, duration, chord progression and scale, in order to extract different layers of information and manipulation.

###### Rhythmic Variation
Harmony is a complex musical category that can not be considered in isolation from other musical parameters. In relation to rhythm, harmony progresses in time displaying a certain harmonic rhythm, which is the pace at which chord-changes structure time. This tends to be regular, especially in the styles we are studying, with chords changing at every bar. However the harmonic loops we are presenting have a clear motivic identity (call this hook, vamp or riff, the underlying concept is that of a harmonic-rhythmic-melodic compound recognizable as a unit and characteristic of a piece of music).

This surface rhythmic layer is processed according to an Agnostic Density Transformer, based on the fact that syncopated onsets, as challenges to regularity, are the most definitive elements of a rhythmic pattern, as opposed to onsets that reinforce the beat’s regularity, which we consider to be least important on the definition of a rhythmic pattern.
This strategy for rhythmic variation maintains the original's rhythmic feel, while adding or subtracting elements in real-time. Therefore, the user can make the pattern more dense or sparse, while always being able to return to the original rhythmic pattern.

###### Duration
The Density Agnostic Transformer only takes information (and possibility of variation) about the onsets (i.e. the position of the attacks). Whether this might be sufficient to model percussive instruments, where the location of a hit might be enough to replicate a pattern, manipulation of sounds that can be prolongated on time (as most pitched-instruments do, to different extents and by different techniques), need to take care of the duration of the sounds. In the current prototype, we have treated duration as a separate layer of the onset positions (density). We have analysed the duration of each note according to its position on the metrical grid, and assigned zeroth order probabilities to each step position. The overall duration of the pattern can be adjusted by a so-called legato control, which is the result of combining the onsets layer (density) with the zeroth order probability of the durations per step, resulting in a continuum going from legato (all notes ending at the moment of a new attack) to an imperfect stacatto (all notes having the duration of the minimum step size, a 16th note in the current implementation).

###### Register Expansion
A register expansion control allows variations in the vertical layout of the chord, from closed position (all notes of the chord contained within the same octave) to higher and lower expansion to up to 4 octaves.

###### Visualization and Synchronization
The real-time interaction is limited to a very simple interface with a series of sliders controlling the parameters just described. A second window provides visualization information about the live transformations on the MIDI Loop. This window presents a two-bar length grid quantized at 16th notes, with a three-layer box system on top. The layer at the background represents a metronome progressing along the sequence beats in sync with the tempo set by the user. The middle-ground layer represents the original pattern: each box represents a chord event, labelled with its chord name, where start- and end-points, as well as duration are represented by the rectangles position and horizontal length. Similarly, the forefront layer displays the modifications on real-time requested by the user.

The House Harmonic Filler offers MIDI-learn functionality and master/slave synchronization, so it could be integrated with any regular DAW for testing.

!["The graphic interface"](/vis/hhf.png?raw=true)


# TO-BE-DONE-VERY-SOON!

###### Harmonic Variation
The chord structure proper can be modified following two different and complementary strategies:
By changing the so-called color or tension of each chord, that is, by modifying the number of notes in the chord while keeping the same function and root. This is a technique characteristic of jazz-derived styles, present in deep house music, by which one can pile up thirds (to make chords of 7th, 9th, 11th and 13th) or added notes (6th, 9th, 4th). The chord saturation control, offers a range of variation from the so-called power-chord at one extreme (the highest reduction of a chord, by which even the major/minor typology is omitted) to chromatic additions on the other end (adding notes that do not belong to the current scale). However, most of the interactive range of the color control, deals with addition of tensions according to the detected scale or possible derivatives, when a defective pitch-class set is present (i.e. groups of notes consisting of six or less notes).

The other approach is borrowed from both classic and modern music theory, and is based on the assumption that certain chords can temporarily substitute other chords, maintaining the original tonal function. There is extensive literature on rules of chord substitution; we refer the reader to two works already mentioned in this report for brief and extensive surveys on this issue (Moore, 1992; Piston, 1941).

The substitution distance control proceeds from very tonal substitutions at one extreme to chromatic substitution on the other, although this might not be idiomatic of the styles in consideration.

###### Overall Activity Control
I plan to offer an *Overall Activity Control* which simultaneously influences the amount of variation of the tonal parameters just described, resulting in a sort of voice leading control according to the color, substitution and register parameters, from a single change per chord on one extreme, to changes in the vertical configuration of the chord at every new onset.
Again, the activity control will follow a model based on the theory behind the agnostic density transformer (Lerdahl and Jakendoff, 1983) by which less rhythmically-significant steps are modified first.
