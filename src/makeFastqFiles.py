import sys

class assignedReads:
	def __init__(self,readName_taxid,taxid_dereplicated,majorSpeciesTaxid_list):
		self.taxidDereplicated = set()
		with open(taxid_dereplicated,"r")as data:
			for line in data:
				line_trim = line.strip("\n")
				self.taxidDereplicated.add(line_trim)
		self.readName_taxID = {}
		self.taxID_readName = {}
		with open(readName_taxid,"r")as data:
			for line in data:
				line_trim = line.strip("\n")
				table = line_trim.split("\t")
				if table[1] in self.taxidDereplicated:
					self.readName_taxID.setdefault(table[0],table[1])
					if table[1] in self.taxID_readName:
						self.taxID_readName[table[1]].append(table[0])
					self.taxID_readName.setdefault(table[1],[table[0]])
		self.majorSpeciesTaxid = set()
		with open(majorSpeciesTaxid_list,"r")as data:
			for line in data:
				line_trim = line.strip("\n")
				self.majorSpeciesTaxid.add(line_trim)
	def make_fastq(self,fastqFile):
		with open(fastqFile,"r")as data:
			temporary_readData = ""
			temporary_readName = ""
			for line in data:
				line_trim = line.strip("\n")
				if line_trim[0] == "@":
					if temporary_readName[1:].split(" ")[0] in self.readName_taxID:
						if self.readName_taxID[temporary_readName[1:].split(" ")[0]] in self.majorSpeciesTaxid:
							fileName = fastqFile.split("/")[-1][:5] + "_" + self.readName_taxID[temporary_readName[1:].split(" ")[0]] + "_selectedByCoreKaiju.fastq"
							with open(fileName, "a")as f:
								f.write(temporary_readData)
					temporary_readData = line
					temporary_readName = line_trim
				if line_trim[0] != "@":
					temporary_readData += line

if __name__ == "__main__":
	args = sys.argv
	AssignedReads = assignedReads(args[1],args[2],args[3])
	AssignedReads.make_fastq(args[4])
	AssignedReads.make_fastq(args[5])

