import os, sys, base64, time, socket, hashlib, admin
import _winreg as wreg
from string import ascii_lowercase, digits, ascii_uppercase
from Crypto import Random
from Crypto.Cipher import AES
from sys import platform as _platform
from termcolor import colored
if not admin.isUserAdmin():
	admin.runAsAdmin()
if _platform == 'win32':
    import colorama
    colorama.init()
def yellow(text):
    return colored(text, 'yellow', attrs=['bold'])

def green(text):
    return colored(text, 'green', attrs=['bold'])

def red(text):
    return colored(text, 'red', attrs=['bold'])

def cyan(text):
    return colored(text, 'cyan', attrs=['bold'])

os.system('cls')
banner = '''
		   Configuration - The Password Manager v1.3
'''
print yellow(banner)
try:
	tpmpswrd = raw_input('\nSet Main Vault Password : ')
	ciph = raw_input('\nSet CipherKey (16 letters long) : ')
	while len(ciph) != 16:
		print red("\n[!] Yo, CIPHER KEY NEEDS TO BE 16 KEY LONG, TRY AGAIN")
		ciph = raw_input('\nSet CipherKey (16 letters long) : ')
except KeyboardInterrupt:
	print red("\n\n[+] Shutting down, try again [+]\n\n\n")
cont = '''
tpmpswrd = '%s' #TPM's Vault Password
filename = 'jesus.db'
ciph = '%s' #Cipher Key '''%(tpmpswrd,ciph)

contb64 = base64.b64encode(cont)
for i in xrange(9):
	contb64 = base64.b64encode(contb64)

encc = '''import os, base64
x = 1337 * 1337 
xx = x + 1337 
xxx = xx / 1337 
xxxx = xxx - 1334
xxxxx = xxxx + 5
y = 1337 * 1337
yyyyy = x + 1337
xyyxy = xxx - 1334
xxxxy = xxxx = xxx - 1334
encc = '%s'
enc = base64.b64decode(encc)
for i in xrange(xxxxx):
	enc = base64.b64decode(enc)
exec(enc)'''%(contb64)
file = os.getcwd()+r"\author.py"
f = open(file, 'w')
f.write(encc)
f.close()

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:

    def __init__( self, key ):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))

def openfile():
    cipher = AESCipher(ciph)
    file = open('jesus.db','r')
    file = file.read()
    encrypted = cipher.encrypt(file)
    put = open('jesus.db','w')
    put.write(encrypted)
    put.close()

print green("\n[+] You are almost done !!")
print cyan("\n[!] Generating new database")
usr = socket.gethostname()
ff = '''         
              ***** AES Encrypted Vault | Owner : %s *****


'''%(usr)
fill = open('jesus.db', 'w+')
fill.write(ff)
fill.close()
openfile()
print green("\n[+] Database setup complete. Enjoy %s")%(usr)
print cyan("\n[!] Adding registry key to add Right-Click Option, Generate Password")
time.sleep(2)
dirrrr = os.getcwd().strip('_core')+"\Generate"
#Creating new key
key = wreg.CreateKey(wreg.HKEY_CLASSES_ROOT, "Directory\\background\\shell\\Generate Password ( TPM )")
#Creating new subkey 
wreg.SetValue(key, 'command', wreg.REG_SZ, dirrrr)
print wreg.QueryValue(key, 'command')
key.Close()
a = __file__
os.remove(a)
os.remove('admin.py')
sys.exit()
