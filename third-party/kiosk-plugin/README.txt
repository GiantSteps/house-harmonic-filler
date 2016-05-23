KIOSK mode for Pure Data
========================


KIOSK mode allows you to enable one or more of the following features

    * hiding the main Pd-window
    * disabling the menu bar in the patch window
    * making a patch window to be shown at fullsreen
    * setting a window name for the patch window (independent of the patch name)
    * prevent closing of patch windows (using Alt-F4, clicking on the "Close
    * Window" icon, et al.)
    * quit Pd when a patch window is closed
    * disable the (right click) context menu
    * disable key-bindings (like Ctrl-N)
    * prevent scroll bars from appearing, even if the patch content does not fit
    * on a single window


you can enable/disable the parts you want to by editing a kiosk.cfg file.
this config file is searched for in the working directory of Pd, and (if not
found) in the plugin directory of the kiosk-plugin (usually
~/pd-externals/kiosk-plugin/)


INSTALLATION
------------
just copy this directoy to ~/pd-externals/kiosk-plugin/
it will be automatically used, the next time you start Pd

PREREQUISITES
-------------
gui-plugins only work with Pd>=0.43


AUTHOR
------
IOhannes m zmölnig
(though the fullscreen part was copied from András Murányi's "fullscreen"
plugin)
