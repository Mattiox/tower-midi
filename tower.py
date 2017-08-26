import pygame.midi
import sys
import Tkinter as tk
import tkMessageBox
import threading
import Queue
import os

if os.name == "nt":
	import winkeypress as keypress
else:
	import keypress

q = Queue.Queue()

## FUNCTIONS
def worker():
	while True:
		item = q.get()
		keypress.keys(str(item))
		q.task_done()

def midiloop():
	if root.poll:
		keys = []
		if inp.poll():
			rawkey = inp.read(1000)
			#print(rawkey[0][0][2]) <-- VELOCITY
			# check channel 144 - 160, 16 channels
			if int(rawkey[0][0][0]) > 144 and int(rawkey[0][0][0]) < 161:
				wrongChannel(rawkey[0][0][0])
			# checks channel 1 keydown and velocity is more than 0
			if int(rawkey[0][0][0]) == 144 and int(rawkey[0][0][2]) > 0:
				q.put(rawkey[0][0][1])
		pygame.time.wait(1)
		root.after(0, midiloop)
	else:
		return

def callback():
	global inp
	msgoutputlabel.config(text = "Running...")
	startbutton.config(state = 'disabled')
	devdrop.config(state = 'disabled')
	qwertybutton.config(state = 'disabled')
	qwertzbutton.config(state = 'disabled')
	root.update()
	print("Device: " + selecteddevice)
	inp = pygame.midi.Input(int(selecteddevice))
	midiloop()

def enablebutton(dev):
	global selecteddevice
	startbutton.config(state = 'normal')
	selecteddevice = dev[0]
	
def setqwerty():
	qwertzbutton.config(state = 'normal', bg='#ff5050')
	qwertybutton.config(state = 'disabled', bg='#99ff66')
	keypress.setqwerty()

def setqwertz():
	qwertybutton.config(state = 'normal', bg='#ff5050')
	qwertzbutton.config(state = 'disabled', bg='#99ff66')
	keypress.setqwertz()

def wrongChannel(channel):
	tkMessageBox.showinfo("Warning - TowerMidi", "Your Midi keyboard is NOT set to channel 1. (Detected channel: " + str(channel - 143) + " ) \n See your manual to set it to 1 and restart TowerMidi.")

def noDevices():
	tkMessageBox.showinfo("No devices detected! - TowerMidi", "Didn't detect any MIDI devices, your Midi keyboard must be on, connected to PC and detected by your OS.")

def quitProgram():
	pygame.quit()
	sys.exit()

## INITIALISE
pygame.init()
pygame.midi.init()
root = tk.Tk()
root.geometry('350x90')
root.resizable(0,0)
root.title("TowerMidi - by Mattio")
root.poll = True

## THREADING
t = threading.Thread(target=worker)
t.daemon = True
t.start()

## GET DEVICES AND LIST IN DROPDOWN
devicelist = []
for dev in range( 0, pygame.midi.get_count() ):
	if pygame.midi.get_device_info(dev)[2] == 1:
		devicelist.append(str(dev) + " " + pygame.midi.get_device_info(dev)[1])
		print pygame.midi.get_device_info(dev)
if not devicelist:
	noDevices()
	quitProgram()

devices = tk.StringVar(root)
devices.set('SELECT A MIDI DEVICE')
devdrop = tk.OptionMenu(root, devices, *devicelist, command=enablebutton)
devdrop.config(width=20)
devdrop.grid(row=0, column=0, sticky="W")

## BUTTONS
quitbutton = tk.Button(root, text=" QUIT ", command=quitProgram)
quitbutton.grid(row=1, column=1, sticky="E")

startbutton = tk.Button(root, text="START", state='disabled', command=callback)
startbutton.grid(row=0, column=1, sticky="E")

qwertybutton = tk.Button(root, text="QWERTY", state='disabled', bg='#99ff66',command=setqwerty)
qwertybutton.config(disabledforeground='black')
qwertybutton.grid(row=1, column=0, sticky="W")
keypress.setqwerty()

qwertzbutton = tk.Button(root, text="QWERTZ", bg='#ff5050', command=setqwertz)
qwertzbutton.config(disabledforeground='black')
qwertzbutton.grid(row=1, column=0, sticky="E")

msgoutputlabel = tk.Label(root, text="Select Keyboard and hit Start", anchor="w")
msgoutputlabel.grid(row=3, column=0, sticky="W")

root.mainloop()

