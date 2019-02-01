import sys
import numpy 
import biom


class BIOM2CSVPlugin:
	def input(self, filename):
		self.myfile = filename


	def run(self):
		table = biom.load_table(self.myfile)
		self.df = table.to_dataframe()


	def output(self, filename):
		self.df.to_csv(filename)