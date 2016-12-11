import pygame.midi
import sys
import Tkinter as tk
import keypress
import threading
import Queue

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
			#print(rawkey)
			if str(rawkey[0][0][0]) == "144":
				q.put(rawkey[0][0][1])
				#keypress.keys(str(rawkey[0][0][1]))
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

def quitprogram():
	pygame.quit()
	sys.exit()

## INITIALISE
pygame.init()
pygame.midi.init()
root = tk.Tk()
root.geometry('330x30')
root.resizable(0,0)
root.title("TowerMidi")
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
devdrop.pack(side='left')

## BUTTONS
quitbutton = tk.Button(root, text="QUIT", command=quitprogram)
quitbutton.pack(side = 'right',)

startbutton = tk.Button(root, text="START", state='disabled', command=callback)
startbutton.pack(side = 'right')

root.mainloop()
