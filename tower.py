import pygame.midi
import sys
import Tkinter as tk
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
			if str(rawkey[0][0][0]) == "144" and int(rawkey[0][0][2]) > 0:
				q.put(rawkey[0][0][1])
		pygame.time.wait(1)
		root.after(0, midiloop)
	else:
		return

def callback():
	global inp
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
	
def quitprogram():
	pygame.quit()
	sys.exit()

## INITIALISE
pygame.init()
pygame.midi.init()
root = tk.Tk()
root.geometry('350x60')
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

devices = tk.StringVar(root)
devices.set('SELECT A MIDI DEVICE')
devdrop = tk.OptionMenu(root, devices, *devicelist, command=enablebutton)
devdrop.config(width=20)
devdrop.grid(row=0, column=0, sticky="W")

## BUTTONS
quitbutton = tk.Button(root, text="QUIT", command=quitprogram)
quitbutton.grid(row=1, column=1, sticky="E")

startbutton = tk.Button(root, text="START", state='disabled', command=callback)
startbutton.grid(row=0, column=1, sticky="E")

if os.name == 'nt':
	qwertybutton = tk.Button(root, text="QWERTY", state='disabled', bg='#99ff66',command=setqwerty)
	qwertybutton.config(disabledforeground='black')
	qwertybutton.grid(row=1, column=0, sticky="W")
	keypress.setqwerty()

	qwertzbutton = tk.Button(root, text="QWERTZ", bg='#ff5050', command=setqwertz)
	qwertzbutton.config(disabledforeground='black')
	qwertzbutton.grid(row=1, column=0, sticky="E")
else:
	keypress.setqwerty()
root.mainloop()

