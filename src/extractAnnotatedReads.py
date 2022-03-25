import sys
import re

class coreKaiju_out:
	def __init__(self,coreKaiju_output):
		self.readName_taxid = {}
		with open(coreKaiju_output,"r")as data:
			for line in data:
				line_trim = line.strip("\n")
				table = line_trim.split("\t")
				if table[0] == "C":
					self.readName_taxid.setdefault(table[1],table[2])
		with open("readName_taxid.tsv","w")as f:
			for k,v in self.readName_taxid.items():
				f.write(k + "\t" + v + "\n")
		with open("taxid.txt","w")as f:
			for k,v in self.readName_taxid.items():
				f.write(v + "\n")

if __name__ == "__main__":
	args = sys.argv
	CoreKaiju_out = coreKaiju_out(args[1])
