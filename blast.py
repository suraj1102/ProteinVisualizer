# Import Dependencies
import urllib.request
import os, sys, subprocess
from Bio import SearchIO, SeqIO
from Bio.Blast import NCBIWWW, NCBIXML

# Import Project Files
from protein_scraper import WebScraper

cwd = os.getcwd()
xmlf = cwd + os.sep + 'XMLfiles'+ os.sep
pdbf = cwd + os.sep + 'PDBfiles' + os.sep
fstf = cwd + os.sep + 'FastaFiles' + os.sep
pdbd = 'http://files.rcsb.org/download/'

class Blast():
    def __init__(self, protein_id):
        self.protein = protein_id

    def make_blast(self):
        self.record = SeqIO.read(fstf + f'{self.protein}.fasta', format="fasta")
        print('\nSequence read! Working on BLAST...')

        self.xmlfile = f"blast_{self.protein}.xml"

        if self.xmlfile in os.listdir(xmlf):
            print("BLAST and XML file already exist")

        else:
            self.result_handle = NCBIWWW.qblast("blastp", "pdb", self.record.seq)
            print('BLAST done!')

            with open(xmlf + self.xmlfile, "w") as out_handle:
                out_handle.write(self.result_handle.read())

            print('XML file created!')

    def readxml(self):
        blast_qresult = SearchIO.read(xmlf + self.xmlfile, "blast-xml")
        res_lines = str(blast_qresult).split('\n')
        first_hit = res_lines[7]

        self.PDBid = first_hit[26:30]
        print(f"\nPDB ID: {self.PDBid}")

        file = self.PDBid + '.pdb'
        url = pdbd + file
        urllib.request.urlretrieve(url, pdbf + file)
        if sys.platform == "win32":
            os.startfile(pdbf + file)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, pdbf + file])

# WebScraper = WebScraper()
# WebScraper.get_search_items()
# WebScraper.get_protein_sequence()

# Blast = Blast(WebScraper.protein_id)
# Blast.make_blast()
# Blast.readxml()
