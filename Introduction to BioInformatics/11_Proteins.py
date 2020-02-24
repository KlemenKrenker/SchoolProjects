# Introduction to Bioinformatics 2019/20
# 11 - Translating RNA into Protein

from h_read import FileReader
# from Bio import SeqIO


class Proteins:
    protein = {
        'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
        'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
        'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
        'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
        'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
        'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
        'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'UAA': '', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'UAG': '', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
        'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'UGA': '', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }

    def __init__(self, dna_sequence):
        self.dna_sequence = dna_sequence
        self.protein_sequence = ''

    # returns protein from dna sequence
    def get_proteins(self):
        try:
            for x in range(0, len(self.dna_sequence), 3):
                codon = self.dna_sequence[x:x + 3]
                self.protein_sequence += self.protein[codon]
            return self.protein_sequence
        except Exception as e:
            print('[ERROR] - exception raised in get_proteins; ' + str(e))


if __name__ == '__main__':
    data = FileReader('dataset.txt')
    data_list = data.e_read()

    pr = Proteins(data_list[0])
    print(pr.get_proteins())
