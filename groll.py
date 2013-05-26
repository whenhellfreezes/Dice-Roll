#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class RollDice(QtGui.QWidget):
	def __init__(self):
		super(RollDice, self).__init__()
		self.initUI()

	def initUI(self):
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

		dice = QtGui.QLabel('Dice')
		keep = QtGui.QLabel('Keep')
		weight = QtGui.QLabel('Weight')
		better = QtGui.QLabel('Better')
		lesser = QtGui.QLabel('Lesser')
		runs = QtGui.QLabel('Runs')
		exploding = QtGui.QPushButton('Exploding')
		reroll = QtGui.QPushButton('Reroll')
		none = QtGui.QPushButton('None')
		percent = QtGui.QPushButton('Percent')
		average = QtGui.QLabel('Average:')
		chance = QtGui.QLabel('Chance:')

		
		diceEdit = QtGui.QLineEdit()
		keepEdit = QtGui.QLineEdit()
		weightEdit = QtGui.QLineEdit()
		betterEdit = QtGui.QLineEdit()
		lesserEdit = QtGui.QLineEdit()
		runsEdit = QtGui.QLineEdit()
		averageEdit = QtGui.QLineEdit()
		chanceEdit = QtGui.QLineEdit()

		grid = QtGui.QGridLayout()
		grid.setSpacing(10)

		#First Row plus thier edit box
		grid.addWidget(dice, 1, 0)
		grid.addWidget(diceEdit, 1, 1)
		grid.addWidget(keep, 2, 0)
		grid.addWidget(keepEdit, 2, 1)
		grid.addWidget(weight, 3, 0)
		grid.addWidget(weightEdit, 3, 1)
		grid.addWidget(better, 4, 0)
		grid.addWidget(betterEdit, 4, 1)
		grid.addWidget(lesser, 5, 0)
		grid.addWidget(lesserEdit, 5, 1)

		#Second Row
		grid.addWidget(runs, 1, 2)
		grid.addWidget(runsEdit, 1, 3)
		grid.addWidget(exploding, 2, 2)
		grid.addWidget(reroll, 2, 3)
		grid.addWidget(none, 3, 2)
		grid.addWidget(percent, 3, 3)
		grid.addWidget(average, 4, 2)
		grid.addWidget(averageEdit, 4, 3)
		grid.addWidget(chance, 5, 2)
		grid.addWidget(chanceEdit, 5, 3)


		#Close Button
		qbtn = QtGui.QPushButton('Quit', self)
		qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		grid.addWidget(qbtn, 6, 0, 6, 1)

		#Execute Button
		ebtn = QtGui.QPushButton('Simulate', self)

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
