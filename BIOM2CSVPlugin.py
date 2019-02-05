import sys
import numpy 
import biom


class BIOM2CSVPlugin:
	def input(self, filename):
		self.myfile = filename


	def run(self):
		table = biom.load_table(self.myfile)
		print table[0,0]
		self.df = table.to_dataframe()
		print dir(self.df)

	def output(self, filename):
		self.df.to_csv(filename, index=False)
