# Introduction to Bioinformatics 2019/20
# 42 - RNA Splicing

# from h_read import FileReader
from Bio import SeqIO

import re


class Splicing:
    def __init__(self, dataset):
        self.sequences = []
        fasta_sequences = SeqIO.parse(open(dataset), 'fasta')
        for fasta in fasta_sequences:
            name, sequence = fasta.id, str(fasta.seq)
            n_seq = ''
            for x in range(0, len(sequence)):
                if sequence[x] == 'T':
                    n_seq += 'U'
                else:
                    n_seq += sequence[x]
            self.sequences.append(n_seq)

    def splice(self, gene_Sequence):
        print(gene_Sequence)
        regex = r"GU(?:\w{0,}?)AG"
        introns = re.findall(regex, gene_Sequence)
        exon = None

        for intron in introns:
            exon = gene_Sequence.replace(intron, "")

        return introns, exon


if __name__ == '__main__':
    s = Splicing('dataset.txt')
    x = s.splice(s.sequences[0])
    y = s.splice(s.sequences[1])
    z = s.splice(s.sequences[2])
    print(x)
    print(y)
    print(z)

    protein_dict = {
        'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
        'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
        'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
        'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
        'UCU': 'S', 'CCU': 'P', 'ACU': 'U', 'GCU': 'A',
        'UCC': 'S', 'CCC': 'P', 'ACC': 'U', 'GCC': 'A',
        'UCA': 'S', 'CCA': 'P', 'ACA': 'U', 'GCA': 'A',
        'UCG': 'S', 'CCG': 'P', 'ACG': 'U', 'GCG': 'A',
        'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
        'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'UAA': '*', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'UAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
        'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'UGA': 'W', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }
    a = 'AUGGUCUACAUAGCUGACAAACAGCACGUAGCAAUCGGUCGAAUCUCGAGAGGCAUAUGGUCACAUGAUCGGUCGAGCUUUGCGCCUAG'
    p_string = ''
    for x in range(0, len(a), 3):
        try:
            p_string += protein_dict[a[x:x + 3]]
        except Exception as e:
            pass
    print(p_string)
