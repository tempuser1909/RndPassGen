import os

def generateRndPassword(spcEnabled, passLen=16):
	extraSpChar=''
	if(spcEnabled):
		extraSpChar='+=-_{}[]\\|\"\'\:\;?/><,.)(*&^%$#@!~'
	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	chars += '0123456789'
	chars += extraSpChar
	password = ''
	print len(chars)
	for i in range(passLen):
		j = ord(os.urandom(1))
		l = len(chars)
		password += chars[j % l]
	return password
def main():
	for i in range(15):
		print generateRndPassword(True,25)
main()