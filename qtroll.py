#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import shlex
import subprocess
from PyQt4 import QtGui, QtCore

class Constant:
	EXPLODING = 1
	REROLL = 2
	NONE = 3


class RollDice(QtGui.QWidget):
	def executeRoll(self):
		commandtext = ''
		wantChance = False
		if self.diceEdit.text():
			commandtext = " -r "+self.diceEdit.text()
		if self.keepEdit.text():
			commandtext += " -k "+self.keepEdit.text()
		if self.weightEdit.text():
			commandtext += " -w "+self.weightEdit.text()
		if self.betterEdit.text():
			commandtext += " -b "+self.betterEdit.text()
			wantChance = True
		if self.lesserEdit.text():
			commandtext += " -l "+self.lesserEdit.text()
			wantChance = True
		if self.runsEdit.text():
			commandtext += " -n "+self.lesserEdit.text()
		if self.rolltype != Constant.REROLL:
			if self.rolltype == Constant.EXPLODING:
				commandtext += " -e e"
			else:
				commandtext += " -e n"
		if commandtext:
			commandtext += " -c -v -t"
		command = shlex.split("./roll.py " + str(commandtext))
		stdout_string = subprocess.check_output(command)
		attempt = shlex.split(stdout_string)
		if wantChance:
			self.changeChance(attempt[1])
			self.changeAverage(attempt[3])
		else:
			self.changeAverage(attempt[1])




	def __init__(self):
		super(RollDice, self).__init__()
		self.rolltype = Constant.REROLL
		self.initUI()
	
	def changeAverage(self, target):
		self.averageEdit.setText(str(target))
	
	def changeChance(self, target):
		self.chanceEdit.setText(str(target))

	def rollType(self, pressed):
		source = self.sender()
		if source.text() == 'Exploding':
			self.rolltype = Constant.EXPLODING
		elif source.text() == 'Reroll':
			self.rolltype = Constant.REROLL
		elif source.text() == 'None':
			self.rolltype = Constant.NONE


	def initUI(self):
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

		dice = QtGui.QLabel('Dice')
		keep = QtGui.QLabel('Keep')
		weight = QtGui.QLabel('Weight')
		better = QtGui.QLabel('Better')
		lesser = QtGui.QLabel('Lesser')
		runs = QtGui.QLabel('Runs')
		exploding = QtGui.QPushButton('Exploding')
		exploding.clicked.connect(self.rollType)
		reroll = QtGui.QPushButton('Reroll')
		reroll.clicked.connect(self.rollType)
		none = QtGui.QPushButton('None')
		none.clicked.connect(self.rollType)
		average = QtGui.QLabel('Average:')
		chance = QtGui.QLabel('Chance:')

		self.averageEdit = QtGui.QLabel()
		self.chanceEdit = QtGui.QLabel()
		
		self.diceEdit = QtGui.QLineEdit()
		self.keepEdit = QtGui.QLineEdit()
		self.weightEdit = QtGui.QLineEdit()
		self.betterEdit = QtGui.QLineEdit()
		self.lesserEdit = QtGui.QLineEdit()
		self.runsEdit = QtGui.QLineEdit()

		grid = QtGui.QGridLayout()
		grid.setSpacing(10)

		#First Row plus thier edit box
		grid.addWidget(dice, 1, 0)
		grid.addWidget(self.diceEdit, 1, 1)
		grid.addWidget(keep, 2, 0)
		grid.addWidget(self.keepEdit, 2, 1)
		grid.addWidget(weight, 3, 0)
		grid.addWidget(self.weightEdit, 3, 1)
		grid.addWidget(better, 4, 0)
		grid.addWidget(self.betterEdit, 4, 1)
		grid.addWidget(lesser, 5, 0)
		grid.addWidget(self.lesserEdit, 5, 1)

		#Second Row
		grid.addWidget(runs, 1, 2)
		grid.addWidget(self.runsEdit, 1, 3)
		grid.addWidget(exploding, 2, 2)
		grid.addWidget(reroll, 2, 3)
		grid.addWidget(none, 3, 2)
		grid.addWidget(average, 4, 2)
		grid.addWidget(self.averageEdit, 4, 3)
		grid.addWidget(chance, 5, 2)
		grid.addWidget(self.chanceEdit, 5, 3)


		#Close Button
		qbtn = QtGui.QPushButton('Quit', self)
		qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		grid.addWidget(qbtn, 6, 0, 6, 1)

		#Execute Button
		ebtn = QtGui.QPushButton('Simulate', self)
		ebtn.clicked.connect(self.executeRoll)

		grid.addWidget(ebtn, 6, 2, 6, 3)

		self.setLayout(grid)
		self.move(300, 150)
		self.setWindowTitle('Keep Ten')
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = RollDice()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
