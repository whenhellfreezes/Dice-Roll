import sys
import random
import getopt
import numpy as np
import matplotlib.pyplot as plt

#Constants
class Const:
	RUN = 1
	DICE = 3
	KEEP = 1
	PRINTZ = False
	OUTPUT = "output.png"
	EXPLODING = 1
	REROLL = 2
	NONETEN = 3
	TEMPORARY = False


def main(argv):

#Set default values for main config
	runs = Const.RUN
	dice = Const.DICE
	keep = Const.KEEP
	printz = Const.PRINTZ
	fileout = Const.OUTPUT
	escalation = Const.REROLL
	temp = Const.TEMPORARY

#Initialize Buffers
	runDist = {}
	currentRun = []

#Read the commandline arguements
	try:
		opts, args = getopt.getopt(argv, "htr:k:pn:o:e:", ["help", "temp", "roll=", "keep=", "print", "number=", "output="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	if not opts:
		usage()
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			help()
		elif opt in ("-r", "--roll"):
			dice = int(arg)
		elif opt in ("-k", "--keep"):
			keep = int(arg)
		elif opt in ("-p", "--print"):
			printz = True
		elif opt in ("-n", "--number"):
			runs = int(arg)
		elif opt in ("-o", "--output"):
			fileout = arg
		elif opt in ("-t", "--temp"):
			temp = True
		elif opt in ("-e"):
			if arg == "e":
				escalation = Const.EXPLODING
			elif arg == "r":
				escalation = Const.REROLL
			elif arg == "n":
				escalation = Const.NONETEN
			else:
				print "Invalid arguement for exploding ten behaviour \n"
				help()
				sys.exit(4)
	if keep > dice:
		print "Can't have keep be more than the number of dice you roll \n"
		usage()
		sys.exit(5)
	for i in xrange(runs):
		toroll = dice
		k = 0
		result = 0
		while(k < toroll):
			roll = random.randrange(10) + 1
			if roll == 10:
				if escalation == Const.REROLL:
					toroll += 1
				elif escalation == Const.EXPLODING:
					exploding = 10
					while(roll == 10):
						roll = random.randrange(10) + 1
						exploding += roll
					roll = exploding
			currentRun.append(roll)
			k += 1
		sortz = sorted(currentRun, reverse=True)
		for k in xrange(keep):
			result += sortz[k]
		runDist[result] = runDist.get(result, 0) + 1
		currentRun = []
	if printz:
		print runDist
	else:
		labels = []
		frequencies = []
		for a in runDist:
			labels.append(a)
			frequencies.append(runDist[a])
		pos = np.arange(len(runDist))
		width = 1.0
		ax = plt.axes()
		ax.set_xticks(pos + (width /2 ))
		ax.set_xticklabels(labels)
		plt.bar(pos, frequencies, width, color='r')
		if not temp:
			plt.savefig(fileout, bbox_inches=0)
		else:
			plt.show()


#Functions to help people trying to learn how to use the command
def help():
	print "This is a program that is used to roll kep ten dice\n"
	print "Commands \n"
	print "-h --help    Display commands\n"
	print "-r --roll    Choose number of dice to roll\n"
	print "-k --keep    Choose number of dice to keep\n"
	print "-p --print   Output to stdout instead of file\n"
	print "-n --number  Choose the number of times to do roll\n"
	print "-o --output  Choose file to output to\n"
	print "-e [e/r/n]   Set behaviour of exploding tens. (E)xploding, (R)eroll, (N)one \n"
def usage():
	print "You are not using the proper format for input\n"
	help()


#If we are calling main from not the cli we wish to skip 0th argument
if __name__ == "__main__":
	main(sys.argv[1:])
