from pykeyboard import PyKeyboard
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

k = PyKeyboard()

def keys(note):
	global key_y
	global key_z
	if note == '36':
		k.type_string('1')
	elif note == '37':
		PressKey(0x2A)
		PressKey(0x02)
		time.sleep(0.05)
		ReleaseKey(0x02)
		ReleaseKey(0x2A)
	elif note == '38':
		k.type_string('2')
	elif note == '39':
		PressKey(0x2A)
		PressKey(0x03)
		time.sleep(0.05)
		ReleaseKey(0x03)
		ReleaseKey(0x2A)
	elif note == '40':
		k.type_string('3')
	elif note == '41':
		k.type_string('4')
	elif note == '42':
		PressKey(0x2A)
		PressKey(0x05)
		time.sleep(0.05)
		ReleaseKey(0x05)
		ReleaseKey(0x2A)
	elif note == '43':
		k.type_string('5')
	elif note == '44':
		PressKey(0x2A)
		PressKey(0x06)
		time.sleep(0.05)
		ReleaseKey(0x06)
		ReleaseKey(0x2A)
	elif note == '45':
		k.type_string('6')
	elif note == '46':
		PressKey(0x2A)
		PressKey(0x07)
		time.sleep(0.05)
		ReleaseKey(0x07)
		ReleaseKey(0x2A)
	elif note == '47':
		k.type_string('7')
	elif note == '48':
		k.type_string('8')
	elif note == '49':
		PressKey(0x2A)
		PressKey(0x09)
		time.sleep(0.05)
		ReleaseKey(0x09)
		ReleaseKey(0x2A)
	elif note == '50':
		k.type_string('9')
	elif note == '51':
		PressKey(0x2A)
		PressKey(0x0A)
		time.sleep(0.05)
		ReleaseKey(0x0A)
		ReleaseKey(0x2A)
	elif note == '52':
		k.type_string('0')
	elif note == '53':	
		k.type_string('q')
	elif note == '54':
		PressKey(0x2A)
		PressKey(0x10)
		time.sleep(0.05)
		ReleaseKey(0x10)
		ReleaseKey(0x2A)
	elif note == '55':	
		k.type_string('w')
	elif note == '56':
		PressKey(0x2A)
		PressKey(0x11)
		time.sleep(0.05)
		ReleaseKey(0x11)
		ReleaseKey(0x2A)
	elif note == '57':	
		k.type_string('e')
	elif note == '58':
		PressKey(0x2A)
		PressKey(0x12)
		time.sleep(0.05)
		ReleaseKey(0x12)
		ReleaseKey(0x2A)
	elif note == '59':	
		k.type_string('r')
	elif note == '60':	
		k.type_string('t')
	elif note == '61':
		PressKey(0x2A)
		PressKey(0x14)
		time.sleep(0.05)
		ReleaseKey(0x14)
		ReleaseKey(0x2A)
	elif note == '62':	
		PressKey(key_y)
		time.sleep(0.05)
		ReleaseKey(key_y)
	elif note == '63':
		PressKey(0x2A)
		PressKey(key_y)
		time.sleep(0.05)
		ReleaseKey(key_y)
		ReleaseKey(0x2A)
	elif note == '64':	
		k.type_string('u')
	elif note == '65':	
		k.type_string('i')
	elif note == '66':
		PressKey(0x2A)
		PressKey(0x17)
		time.sleep(0.05)
		ReleaseKey(0x17)
		ReleaseKey(0x2A)
	elif note == '67':	
		k.type_string('o')
	elif note == '68':
		PressKey(0x2A)
		PressKey(0x18)
		time.sleep(0.05)
		ReleaseKey(0x18)
		ReleaseKey(0x2A)
	elif note == '69':	
		k.type_string('p')
	elif note == '70':
		PressKey(0x2A)
		PressKey(0x19)
		time.sleep(0.05)
		ReleaseKey(0x19)
		ReleaseKey(0x2A)
	elif note == '71':	
		k.type_string('a')
	elif note == '72':	
		k.type_string('s')
	elif note == '73':
		PressKey(0x2A)
		PressKey(0x1F)
		time.sleep(0.05)
		ReleaseKey(0x1F)
		ReleaseKey(0x2A)
	elif note == '74':	
		k.type_string('d')
	elif note == '75':
		PressKey(0x2A)
		PressKey(0x20)
		time.sleep(0.05)
		ReleaseKey(0x20)
		ReleaseKey(0x2A)
	elif note == '76':	
		k.type_string('f')
	elif note == '77':	
		k.type_string('g')
	elif note == '78':
		PressKey(0x2A)
		PressKey(0x22)
		time.sleep(0.05)
		ReleaseKey(0x22)
		ReleaseKey(0x2A)
	elif note == '79':	
		k.type_string('h')
	elif note == '80':
		PressKey(0x2A)
		PressKey(0x23)
		time.sleep(0.05)
		ReleaseKey(0x23)
		ReleaseKey(0x2A)
	elif note == '81':	
		k.type_string('j')
	elif note == '82':
		PressKey(0x2A)
		PressKey(0x24)
		time.sleep(0.05)
		ReleaseKey(0x24)
		ReleaseKey(0x2A)
	elif note == '83':	
		k.type_string('k')
	elif note == '84':	
		k.type_string('l')
	elif note == '85':
		PressKey(0x2A)
		PressKey(0x26)
		time.sleep(0.05)
		ReleaseKey(0x26)
		ReleaseKey(0x2A)
	elif note == '86':	
		PressKey(key_z)
		time.sleep(0.05)
		ReleaseKey(key_z)
	elif note == '87':
		PressKey(0x2A)
		PressKey(key_z)
		time.sleep(0.05)
		ReleaseKey(key_z)
		ReleaseKey(0x2A)
	elif note == '88':	
		k.type_string('x')
	elif note == '89':	
		k.type_string('c')
	elif note == '90':
		PressKey(0x2A)
		PressKey(0x2E)
		time.sleep(0.05)
		ReleaseKey(0x2E)
		ReleaseKey(0x2A)
	elif note == '91':	
		k.type_string('v')
	elif note == '92':
		PressKey(0x2A)
		PressKey(0x2F)
		time.sleep(0.05)
		ReleaseKey(0x2F)
		ReleaseKey(0x2A)
	elif note == '93':	
		k.type_string('b')
	elif note == '94':
		PressKey(0x2A)
		PressKey(0x30)
		time.sleep(0.05)
		ReleaseKey(0x30)
		ReleaseKey(0x2A)
	elif note == '95':	
		k.type_string('n')
	elif note == '96':	
		k.type_string('m')











