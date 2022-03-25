import sys

class coreKaiju_output:
	def __init__(self,coreKaiju_outFile):
		self.majorSpecies = {}
		with open(coreKaiju_outFile,"r")as data:
			lineNumber = 0
			for line in data:
				lineNumber += 1
				line_trim = line.strip("\n")
				table = line_trim.split("\t")
				if lineNumber >= 3 and lineNumber <= 102:
					self.majorSpecies.setdefault(table[2],lineNumber - 2)
	def outLineage_rank(self):
		for k,v in self.majorSpecies.items():
			print(k.split(";")[-2])

if __name__ == "__main__":
	args = sys.argv
	CoreKaiju_output = coreKaiju_output(args[1])
	CoreKaiju_output.outLineage_rank()

