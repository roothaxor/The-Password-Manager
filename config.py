import os, sys, base64, time
from __files import version
os.system('cls')
banner = '''
		Configuration - The Password Manager v1.2.3
'''
print banner
print "\n\nPlease remember the password's, write it down on some note"
try:
	ions = raw_input('\nSet Main Password : ')
	panic = raw_input('\nSet Panic Password : ')
	cipher = raw_input('\nSet CipherKey (16 letters long) : ')
except KeyboardInterrupt:
	print "\n\n[+] Shutting down, try again [+]\n\n\n"
cont = '''file = os.path.realpath(__file__)
dirc = os.path.dirname(file).strip("__files")
##################### Config's ##########################
ionfdsnfdisncdscnso = '%s'
filedir = dirc+'jesus.db'
panicpassword = '%s'
cipherKey = '%s' '''%(ions,panic,cipher)

contb64 = base64.b64encode(cont)
for i in xrange(9):
	contb64 = base64.b64encode(contb64)

encc = '''import os, base64
encc = '%s'
enc = base64.b64decode(encc)
for i in xrange(9):
	enc = base64.b64decode(enc)
exec(enc)'''%(contb64)
file = os.getcwd()+r"\__files\author.py"
f = open(file, 'w')
f.write(encc)
f.close()
print "\nConfig done!!"
print "\nCreating new database, with your new cipherKey...."
time.sleep(3)
usr = os.environ['username']
ff = '''***** AES Encrypted Password Manager | User : %s *****

'''%(usr)
fill = open('jesus.db', 'w+')
fill.write(ff)
fill.close()
version.eecrypt()
print "\n\nDatabase setup complete. Enjoy %s"%(usr)
a = __file__
os.remove(a)