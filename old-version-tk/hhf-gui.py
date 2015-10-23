#!/usr/bin/python

import OSC
import Tkinter
import threading

# OSC CLIENT
# ==========

c = OSC.OSCClient()
c.connect(('localhost', 7110))

def send_tempo(value):
    msg = OSC.OSCMessage()
    msg.setAddress("/tempo")
    msg.append(float(value))
    c.send(msg)


def send_density(value):
    msg = OSC.OSCMessage()
    msg.setAddress("/density")
    msg.append(float(value))
    c.send(msg)


def send_legato(value):
    msg = OSC.OSCMessage()
    msg.setAddress("/legato")
    msg.append(float(value))
    c.send(msg)


def send_saturation(value):
    msg = OSC.OSCMessage()
    msg.setAddress("/saturation")
    msg.append(float(value))
    c.send(msg)


def send_substitution(value):
    msg = OSC.OSCMessage()
    msg.setAddress("/substitution")
    msg.append(float(value))
    c.send(msg)


def send_activity(value):
    msg = OSC.OSCMessage()
    msg.setAddress("/activity")
    msg.append(float(value))
    c.send(msg)


def send_register(value):
    msg = OSC.OSCMessage()
    msg.setAddress("/register")
    msg.append(float(value))
    c.send(msg)


def send_inversion():
    msg = OSC.OSCMessage()
    msg.setAddress("/inversion")
    msg.append(v_inversion.get())
    c.send(msg)


def send_load():
    msg = OSC.OSCMessage()
    msg.setAddress("/load")
    msg.append("bang")
    c.send(msg)


def send_play():
    msg = OSC.OSCMessage()
    msg.setAddress("/play")
    if v_play.get() == "Play":
        msg.append(1)
        c.send(msg)
    if v_play.get() == "Stop":
        msg.append(0)
        c.send(msg)


def quit_pd():
    msg = OSC.OSCMessage()
    msg.setAddress("/quit")
    msg.append("bang")
    c.send(msg)
    window.destroy()


# OSC SERVER
# ==========

s = OSC.ThreadingOSCServer(('localhost', 7112))
s.addDefaultHandlers()


def receive_osc(addr, tags, stuff, source):
    print addr, stuff[0]
    if addr == "/tempo":
        v_tempo.set(stuff[0])
    if addr == "/density":
        v_density.set(stuff[0])
    if addr == "/legato":
        v_legato.set(stuff[0])
    if addr == "/saturation":
        v_saturation.set(stuff[0])
    if addr == "/substitution":
        v_substitution.set(stuff[0])
    if addr == "/activity":
        v_activity.set(stuff[0])
    if addr == "/register":
        v_register.set(stuff[0])
    if addr == "/inversion":
        v_inversion.set(stuff[0])
    if addr == "/play":
        v_play.set(stuff[0])


s.addMsgHandler("/tempo", receive_osc)
s.addMsgHandler("/density", receive_osc)
s.addMsgHandler("/legato", receive_osc)
s.addMsgHandler("/saturation", receive_osc)
s.addMsgHandler("/substitution", receive_osc)
s.addMsgHandler("/activity", receive_osc)
s.addMsgHandler("/register", receive_osc)
s.addMsgHandler("/inversion", receive_osc)
s.addMsgHandler("/play", receive_osc)


# GRAPHICAL USER INTERFACE
# ========================

window = Tkinter.Tk()

v_tempo = Tkinter.IntVar()
v_density = Tkinter.IntVar()
v_legato = Tkinter.DoubleVar()
v_saturation = Tkinter.DoubleVar()
v_substitution = Tkinter.DoubleVar()
v_activity = Tkinter.DoubleVar()
v_register = Tkinter.IntVar()
v_inversion = Tkinter.IntVar()
v_play = Tkinter.StringVar()

v_play.set("Play")
v_tempo.set(125)
v_legato.set(32)

# DECLARE WIDGETS
# ===============

window.title('House Harmonic Filler')

b_load = Tkinter.Button(text="Load MIDI File", width=15, command=send_load)
b_play = Tkinter.Button(textvariable=v_play, width=5, command=send_play)
b_quit = Tkinter.Button(text="Quit", width=10, command=quit_pd)

s_tempo = Tkinter.Scale(orient='horizontal',
                        length=300,
                        from_=40,
                        to=302,
                        showvalue='true',
                        variable=v_tempo,
                        command=send_tempo)

s_density = Tkinter.Scale(orient='horizontal',
                          length=300,
                          resolution=1,
                          from_=1,
                          to=33,
                          showvalue='true',
                          variable=v_density,
                          command=send_density)

s_legato = Tkinter.Scale(orient='horizontal',
                         length=300,
                         resolution=1,
                         from_=0,
                         to=33,
                         showvalue='false',
                         variable=v_legato,
                         command=send_legato)

s_saturation = Tkinter.Scale(orient='horizontal',
                             length=300,
                             resolution=0.01,
                             from_=0,
                             to=1,
                             showvalue='true',
                             variable=v_saturation,
                             command=send_saturation)

s_substitution = Tkinter.Scale(orient='horizontal',
                               length=300,
                               resolution=0.01,
                               from_=0,
                               to=1,
                               showvalue='true',
                               variable=v_substitution,
                               command=send_substitution)

s_activity = Tkinter.Scale(orient='horizontal',
                           length=300,
                           resolution=0.01,
                           from_=0,
                           to=1,
                           showvalue='true',
                           variable=v_activity,
                           command=send_activity)

s_register = Tkinter.Scale(orient='horizontal',
                           resolution=1,
                           length=180,
                           from_=1,
                           to=4,
                           showvalue='true',
                           variable=v_register,
                           command=send_register)

t_inversion = Tkinter.Checkbutton(text="Allow Inversions",
                                  offvalue=0,
                                  onvalue=1,
                                  variable=v_inversion,
                                  command=send_inversion)

l_density = Tkinter.Label(text='Density')
l_legato = Tkinter.Label(text='Legato')
l_saturation = Tkinter.Label(text='Chord Saturation')
l_substitution = Tkinter.Label(text='Substitution Distance')
l_activity = Tkinter.Label(text='Voicing Activity')
l_register = Tkinter.Label(text='Register Expansion')
l_tempo = Tkinter.Label(text='Tempo')


# VISUAL LAYOUT
# =============

b_load.grid(row=0, column=0, sticky='WS')
b_play.grid(row=0, column=1, sticky='WS')
b_quit.grid(row=0, column=1, sticky='ES')

l_tempo.grid(row=1, column=0, sticky='ES')
s_tempo.grid(row=1, column=1, sticky='W')

l_density.grid(row=2, column=0, sticky='ES')
s_density.grid(row=2, column=1, columnspan=2)

l_legato.grid(row=3, column=0, sticky='ES')
s_legato.grid(row=3, column=1, columnspan=2)

l_saturation.grid(row=4, column=0, sticky='ES')
s_saturation.grid(row=4, column=1, columnspan=2)

l_substitution.grid(row=5, column=0, sticky='ES')
s_substitution.grid(row=5, column=1, columnspan=2)

l_activity.grid(row=6, column=0, sticky='ES')
s_activity.grid(row=6, column=1, columnspan=2)

l_register.grid(row=7, column=0, sticky='ES')
s_register.grid(row=7, column=1, sticky='W')

t_inversion.grid(row=7, column=1, sticky='ES')


# ACTION
# ======

print "Starting OSCServer"
st = threading.Thread(target=s.serve_forever)
st.start()
window.mainloop()


