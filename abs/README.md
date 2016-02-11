##pdmus

*pdmus* is a collection of pd abstractions for manipulation of music at a symbolic level. By **symbolic** we refer to representations of music that are not audio or signal based. These include for example, pitch, chords, keys and rhythmic patterns, but also other commonplace representations such as MIDI, text or lists.

This library depends on the following externals and/or libraries:

*arraysize  cyclone  ggee  hcs  iemlib  jasch_lib  list-abs  mrpeach  pddp  zexy*

Although most objects will work with both pd-extended and pd-vanilla, we suggest you to use a recent pd-vanilla distribution and download/install the dependencies via the deken plugin (https://github.com/pure-data/deken). External objects are always instantiated as such in the patches (e.g. [zexy/listfind]) , so you don't need to declare any library in advance.
