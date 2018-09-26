import crypt
'''
This is only for cracking passwords encrpyted with the crypt algorithm.
For cracking passwords encryted with SHA-512 we can use the hashlib library

'''




class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'to continue
    FAIL = '\033[91m'
    ENDC = '\033[0m'
 	BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




def testPass(cryptPass):
	salt=cryptPass[0:2]
	dictFile=open('dictionary.txt','r')
	for word in dictFile.readlines():
		word=word.strip('\n')
		cryptWord=crypt.crypt(word,salt)
		if(cryptWord==cryptPass):
			print bcolors.OKGREEN "[+] password found: "+word+"\n" bcolors.ENDC
			return

		print bcolors.FAIL "[-] password not found. \n" bcolors.ENDC
		return

def main():
	passFile=open("passwords.txt","r")
	for line in passFile.readlines():
		if ':' in line :
			user= line.split(':')[0]
			cryptPass=line.split(':')[1].strip(' ')
			print bcolors.HEADER "[*] Cracking password for "+user
			testPass(cryptPass)

if __main__=="__main__":
	main()




