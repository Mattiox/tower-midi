from pykeyboard import PyKeyboard
import time


def setqwerty():
	global key_y
	global key_z
	key_y = "y"
	key_z = "z"

def setqwertz():
	global key_y
	global key_z
	key_y = "z"
	key_z = "y"

k = PyKeyboard()

def keys(note):
	global key_y
	global key_z
	if note == '36':
		k.type_string('1')
	elif note == '37':
		k.press_key(k.shift_key)
		k.press_key('1')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('1')
	elif note == '38':
		k.type_string('2')
	elif note == '39':
		k.press_key(k.shift_key)
		k.press_key('2')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('2')
	elif note == '40':
		k.type_string('3')
	elif note == '41':
		k.type_string('4')
	elif note == '42':
		k.press_key(k.shift_key)
		k.press_key('4')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('4')
	elif note == '43':
		k.type_string('5')
	elif note == '44':
		k.press_key(k.shift_key)
		k.press_key('5')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('5')
	elif note == '45':
		k.type_string('6')
	elif note == '46':
		k.press_key(k.shift_key)
		k.press_key('6')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('6')
	elif note == '47':
		k.type_string('7')
	elif note == '48':
		k.type_string('8')
	elif note == '49':
		k.press_key(k.shift_key)
		k.press_key('8')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('8')
	elif note == '50':
		k.type_string('9')
	elif note == '51':
		k.press_key(k.shift_key)
		k.press_key('9')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('9')
	elif note == '52':
		k.type_string('0')
	elif note == '53':	
		k.type_string('q')
	elif note == '54':
		k.press_key(k.shift_key)
		k.press_key('q')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('q')
	elif note == '55':	
		k.type_string('w')
	elif note == '56':
		k.press_key(k.shift_key)
		k.press_key('w')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('w')
	elif note == '57':	
		k.type_string('e')
	elif note == '58':
		k.press_key(k.shift_key)
		k.press_key('e')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('e')
	elif note == '59':	
		k.type_string('r')
	elif note == '60':	
		k.type_string('t')
	elif note == '61':
		k.press_key(k.shift_key)
		k.press_key('t')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('t')
	elif note == '62':	
		k.type_string(key_y)
	elif note == '63':
		k.press_key(k.shift_key)
		k.press_key(key_y)
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key(key_y)
	elif note == '64':	
		k.type_string('u')
	elif note == '65':	
		k.type_string('i')
	elif note == '66':
		k.press_key(k.shift_key)
		k.press_key('i')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('i')
	elif note == '67':	
		k.type_string('o')
	elif note == '68':
		k.press_key(k.shift_key)
		k.press_key('o')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('o')
	elif note == '69':	
		k.type_string('p')
	elif note == '70':
		k.press_key(k.shift_key)
		k.press_key('p')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('p')
	elif note == '71':	
		k.type_string('a')
	elif note == '72':	
		k.type_string('s')
	elif note == '73':
		k.press_key(k.shift_key)
		k.press_key('s')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('s')
	elif note == '74':	
		k.type_string('d')
	elif note == '75':
		k.press_key(k.shift_key)
		k.press_key('d')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('d')
	elif note == '76':	
		k.type_string('f')
	elif note == '77':	
		k.type_string('g')
	elif note == '78':
		k.press_key(k.shift_key)
		k.press_key('g')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('g')
	elif note == '79':	
		k.type_string('h')
	elif note == '80':
		k.press_key(k.shift_key)
		k.press_key('h')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('h')
	elif note == '81':	
		k.type_string('j')
	elif note == '82':
		k.press_key(k.shift_key)
		k.press_key('j')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('j')
	elif note == '83':	
		k.type_string('k')
	elif note == '84':	
		k.type_string('l')
	elif note == '85':
		k.press_key(k.shift_key)
		k.press_key('l')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('l')
	elif note == '86':	
		k.type_string(key_z)
	elif note == '87':
		k.press_key(k.shift_key)
		k.press_key(key_z)
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key(key_z)
	elif note == '88':	
		k.type_string('x')
	elif note == '89':	
		k.type_string('c')
	elif note == '90':
		k.press_key(k.shift_key)
		k.press_key('c')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('c')
	elif note == '91':	
		k.type_string('v')
	elif note == '92':
		k.press_key(k.shift_key)
		k.press_key('v')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('v')
	elif note == '93':	
		k.type_string('b')
	elif note == '94':
		k.press_key(k.shift_key)
		k.press_key('b')
		time.sleep(0.05)
		k.release_key(k.shift_key)
		k.release_key('b')
	elif note == '95':	
		k.type_string('n')
	elif note == '96':	
		k.type_string('m')











