import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
	_fields_ = [("wVk", ctypes.c_ushort),
				("wScan", ctypes.c_ushort),
				("dwFlags", ctypes.c_ulong),
				("time", ctypes.c_ulong),
				("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
	_fields_ = [("uMsg", ctypes.c_ulong),
				("wParamL", ctypes.c_short),
				("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
	_fields_ = [("dx", ctypes.c_long),
				("dy", ctypes.c_long),
				("mouseData", ctypes.c_ulong),
				("dwFlags", ctypes.c_ulong),
				("time",ctypes.c_ulong),
				("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
	_fields_ = [("ki", KeyBdInput),
				("mi", MouseInput),
				("hi", HardwareInput)]

class Input(ctypes.Structure):
	_fields_ = [("type", ctypes.c_ulong),
				("ii", Input_I)]

def PressKey(hexKeyCode):
	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
	x = Input( ctypes.c_ulong(1), ii_ )
	ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
	x = Input( ctypes.c_ulong(1), ii_ )
	ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def setqwerty():
	global key_y
	global key_z
	key_y = 0x15
	key_z = 0x2C

def setqwertz():
	global key_y
	global key_z
	key_y = 0x2C
	key_z = 0x15

def keys(note):
	if note == '36':
		PressKey(0x02)
		ReleaseKey(0x02)
	elif note == '37':
		PressKey(0x2A)
		PressKey(0x02)
		time.sleep(0.05)
		ReleaseKey(0x02)
		ReleaseKey(0x2A)
	elif note == '38':
		PressKey(0x03)
		ReleaseKey(0x03)
	elif note == '39':
		PressKey(0x2A)
		PressKey(0x03)
		time.sleep(0.05)
		ReleaseKey(0x03)
		ReleaseKey(0x2A)
	elif note == '40':
		PressKey(0x04)
		ReleaseKey(0x04)
	elif note == '41':
		PressKey(0x05)
		ReleaseKey(0x05)
	elif note == '42':
		PressKey(0x2A)
		PressKey(0x05)
		time.sleep(0.05)
		ReleaseKey(0x05)
		ReleaseKey(0x2A)
	elif note == '43':
		PressKey(0x06)
		ReleaseKey(0x06)
	elif note == '44':
		PressKey(0x2A)
		PressKey(0x06)
		time.sleep(0.05)
		ReleaseKey(0x06)
		ReleaseKey(0x2A)
	elif note == '45':
		PressKey(0x07)
		ReleaseKey(0x07)
	elif note == '46':
		PressKey(0x2A)
		PressKey(0x07)
		time.sleep(0.05)
		ReleaseKey(0x07)
		ReleaseKey(0x2A)
	elif note == '47':
		PressKey(0x08)
		ReleaseKey(0x08)
	elif note == '48':
		PressKey(0x09)
		ReleaseKey(0x09)
	elif note == '49':
		PressKey(0x2A)
		PressKey(0x09)
		time.sleep(0.05)
		ReleaseKey(0x09)
		ReleaseKey(0x2A)
	elif note == '50':
		PressKey(0x0A)
		ReleaseKey(0x0A)
	elif note == '51':
		PressKey(0x2A)
		PressKey(0x0A)
		time.sleep(0.05)
		ReleaseKey(0x0A)
		ReleaseKey(0x2A)
	elif note == '52':
		PressKey(0x0B)
		ReleaseKey(0x0B)
	elif note == '53':	
		PressKey(0x10)
		ReleaseKey(0x10)
	elif note == '54':
		PressKey(0x2A)
		PressKey(0x10)
		time.sleep(0.05)
		ReleaseKey(0x10)
		ReleaseKey(0x2A)
	elif note == '55':	
		PressKey(0x11)
		ReleaseKey(0x11)
	elif note == '56':
		PressKey(0x2A)
		PressKey(0x11)
		time.sleep(0.05)
		ReleaseKey(0x11)
		ReleaseKey(0x2A)
	elif note == '57':	
		PressKey(0x12)
		ReleaseKey(0x12)
	elif note == '58':
		PressKey(0x2A)
		PressKey(0x12)
		time.sleep(0.05)
		ReleaseKey(0x12)
		ReleaseKey(0x2A)
	elif note == '59':	
		PressKey(0x13)
		ReleaseKey(0x13)
	elif note == '60':	
		PressKey(0x14)
		ReleaseKey(0x14)
	elif note == '61':
		PressKey(0x2A)
		PressKey(0x14)
		time.sleep(0.05)
		ReleaseKey(0x14)
		ReleaseKey(0x2A)
	elif note == '62':	
		PressKey(key_y)
		ReleaseKey(key_y)
	elif note == '63':
		PressKey(0x2A)
		PressKey(key_y)
		time.sleep(0.05)
		ReleaseKey(key_y)
		ReleaseKey(0x2A)
	elif note == '64':	
		PressKey(0x16)
		ReleaseKey(0x16)
	elif note == '65':	
		PressKey(0x17)
		ReleaseKey(0x17)
	elif note == '66':
		PressKey(0x2A)
		PressKey(0x17)
		time.sleep(0.05)
		ReleaseKey(0x17)
		ReleaseKey(0x2A)
	elif note == '67':	
		PressKey(0x18)
		ReleaseKey(0x18)
	elif note == '68':
		PressKey(0x2A)
		PressKey(0x18)
		time.sleep(0.05)
		ReleaseKey(0x18)
		ReleaseKey(0x2A)
	elif note == '69':	
		PressKey(0x19)
		ReleaseKey(0x19)
	elif note == '70':
		PressKey(0x2A)
		PressKey(0x19)
		time.sleep(0.05)
		ReleaseKey(0x19)
		ReleaseKey(0x2A)
	elif note == '71':	
		PressKey(0x1E)
		ReleaseKey(0x1E)
	elif note == '72':	
		PressKey(0x1F)
		ReleaseKey(0x1F)
	elif note == '73':
		PressKey(0x2A)
		PressKey(0x1F)
		time.sleep(0.05)
		ReleaseKey(0x1F)
		ReleaseKey(0x2A)
	elif note == '74':	
		PressKey(0x20)
		ReleaseKey(0x20)
	elif note == '75':
		PressKey(0x2A)
		PressKey(0x20)
		time.sleep(0.05)
		ReleaseKey(0x20)
		ReleaseKey(0x2A)
	elif note == '76':	
		PressKey(0x21)
		ReleaseKey(0x21)
	elif note == '77':	
		PressKey(0x22)
		ReleaseKey(0x22)
	elif note == '78':
		PressKey(0x2A)
		PressKey(0x22)
		time.sleep(0.05)
		ReleaseKey(0x22)
		ReleaseKey(0x2A)
	elif note == '79':	
		PressKey(0x23)
		ReleaseKey(0x23)
	elif note == '80':
		PressKey(0x2A)
		PressKey(0x23)
		time.sleep(0.05)
		ReleaseKey(0x23)
		ReleaseKey(0x2A)
	elif note == '81':	
		PressKey(0x24)
		ReleaseKey(0x24)
	elif note == '82':
		PressKey(0x2A)
		PressKey(0x24)
		time.sleep(0.05)
		ReleaseKey(0x24)
		ReleaseKey(0x2A)
	elif note == '83':	
		PressKey(0x25)
		ReleaseKey(0x25)
	elif note == '84':	
		PressKey(0x26)
		ReleaseKey(0x26)
	elif note == '85':
		PressKey(0x2A)
		PressKey(0x26)
		time.sleep(0.05)
		ReleaseKey(0x26)
		ReleaseKey(0x2A)
	elif note == '86':	
		PressKey(key_z)
		ReleaseKey(key_z)
	elif note == '87':
		PressKey(0x2A)
		PressKey(key_z)
		time.sleep(0.05)
		ReleaseKey(key_z)
		ReleaseKey(0x2A)
	elif note == '88':	
		PressKey(0x2D)
		ReleaseKey(0x2D)
	elif note == '89':	
		PressKey(0x2E)
		ReleaseKey(0x2E)
	elif note == '90':
		PressKey(0x2A)
		PressKey(0x2E)
		time.sleep(0.05)
		ReleaseKey(0x2E)
		ReleaseKey(0x2A)
	elif note == '91':	
		PressKey(0x2F)
		ReleaseKey(0x2F)
	elif note == '92':
		PressKey(0x2A)
		PressKey(0x2F)
		time.sleep(0.05)
		ReleaseKey(0x2F)
		ReleaseKey(0x2A)
	elif note == '93':	
		PressKey(0x30)
		ReleaseKey(0x30)
	elif note == '94':
		PressKey(0x2A)
		PressKey(0x30)
		time.sleep(0.05)
		ReleaseKey(0x30)
		ReleaseKey(0x2A)
	elif note == '95':	
		PressKey(0x31)
		ReleaseKey(0x31)
	elif note == '96':	
		PressKey(0x32)
		ReleaseKey(0x32)





