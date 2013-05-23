import sys
import getopt

def main(argv):

#Set default values for main config
	runs = 1
	dice = 3
	keep = 1
	printz = False
	fileout = "output.txt"

#Read the commandline arguements
	try:
		opts, args = getopt.getopt(argv, "hrkpno:e", ["help", "roll", "keep", "print", "number", "output"])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	if not opts:
		usage()
	for opt, index in opts:


#Functions to help people trying to learn how to use the command
def help():
	print "This is a program that is used to roll kep ten dice\n"
	print "Commands \n"
	print "-h --help    Display commands\n"
	print "-r --roll    Choose number of dice to roll\n"
	print "-k --keep    Choose number of dice to keep\n"
	print "-p --print   Output to stdout instead of file\n"
	print "-n --number  Choose the number of times to do rolld\n"
	print "-o --output  Choose file to output to\n"
	print "-e [e/r/n]   Set behaviour of exploding tens. (E)xploding, (R)eroll, (N)one \n"
def usage():
	print "You are not using the proper format for input\n"
	help()

#If we are calling main from not the cli we wish to skip 0th argument
if __name__ == "__main__":
	main(sys.argv[1:])
