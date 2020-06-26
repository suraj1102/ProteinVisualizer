from Bio import SeqIO
import random, os

fstf = os.getcwd() + os.sep + 'FastaFiles' + os.sep

class SeqTools():
    def __init__(self, protein_id):
        self.protein_id = protein_id

    def read_seq(self):
        self.seq = SeqIO.read(f"{fstf}{self.protein_id}.fasta", format='fasta').seq
        return f'\nProtein Sequence:\n{self.seq}'

    def protein_to_dna(self):
        self.codons = {
            'I': ['ATA', 'ATC', 'ATT'],
            'M': ['ATG'],
            'T': ['ACA', 'ACC', 'ACG', 'ACT'],
            'N': ['AAC', 'AAT'],
            'K': ['AAA', 'AAG'],
            'S': ['AGC', 'AGT'],
            'R': ['AGA', 'AGG'],
            'L': ['CTA', 'CTC', 'CTG', 'CTT'],
            'P': ['CCA', 'CCC', 'CGG', 'CCT'],
            'H': ['CAC', 'CAT'],
            'Q': ['CAA', 'CAG'],
            'R': ['CGA', 'CGC', 'CGG', 'CGT'],
            'V': ['GTA', 'GTC', 'GTG', 'GTT'],
            'A': ['GCA', 'GCC', 'GCG', 'GCT'],
            'D': ['GAC', 'GAT'],
            'E': ['GAA', 'GAG'],
            'G': ['GGA', 'GGC', 'GGG', 'GGT'],
            'S': ['TCA', 'TCC', 'TCG', 'TCT'],
            'F': ['TTC', 'TTT'],
            'L': ['TTA', 'TTG'],
            'Y': ['TAC', 'TAT'],
            'C': ['TGC', 'TGT'],
            'W': ['TGG'],
            '-': ['TAA', 'TAG', 'TGA']
        }

        self.dna_seq = ''
        for i in str(self.seq):
            codon = random.choice(self.codons[i])
            self.dna_seq += codon

        return f'\nDNA Sequence:\n{self.dna_seq}'

    def nucleotide_values(self):
        self.a_count = self.dna_seq.count('A')
        self.t_count = self.dna_seq.count('T')
        self.c_count = self.dna_seq.count('C')
        self.g_count = self.dna_seq.count('G')
        self.gc_ratio = (self.g_count + self.c_count) / (self.a_count + self.t_count + self.c_count + self.g_count)
        
        return f"\nA: {self.a_count} \nT: {self.t_count} \nG: {self.g_count} \nC: {self.c_count} \nGC Ratio: {self.gc_ratio}"

# SeqTools = SeqTools('AAA98529.1')
# print(SeqTools.read_seq())
# print(SeqTools.protein_to_dna())
# print(SeqTools.nucleotide_values())
