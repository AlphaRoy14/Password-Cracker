import zipfile
import optparse
from threading import Thread 
import sys,os

class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
	# BOLD = '\033[1m'
	# UNDERLINE = '\033[4m'

def extractFile(zFile,password):
	try:
		zFile.extractall(pwd=password)
		print bcolors.OKGREEN + " [+] found password : " + password + "\n" + bcolors.ENDC
		# Thread.interrupt_main()
		os._exit(1) #exiting from threading is a bit weird. 
		# sys.exit()
	except:
		pass

def main():
	parser=optparse.OptionParser("usage: %prog "+"-f <zipfile> -d <dictionary>")
	parser.add_option('-f',dest="zname",type='string',help='specify the zipped file')
	parser.add_option('-d',dest="dname",type='string',help='specify the directory file')
	(options,args)=parser.parse_args()
	if(options.zname==None)|(options.dname==None):
		print parser.usage
		exit(0)
	else:
		zname=options.zname
		dname=options.dname

	zFile=zipfile.ZipFile(zname)
	passFile=open(dname,'r')
	for line in passFile.readlines():
		password=line.strip("\n")
		t=Thread(target=extractFile,args=(zFile,password))
		t.start()

if __name__=="__main__":
	main()




